# ============================================
# Dashboard Streamlit - Projet immobilier
# Auteur : toi :)
# Niveau : débutant (mais propre et commenté)
# ============================================

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
# --------------------------------------------------
# 1. Configuration de la page Streamlit
# --------------------------------------------------
st.set_page_config(
    page_title="Analyse du marché immobilier",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Analyse du marché immobilier en France")
st.write(
   st.write(
    "Bienvenue sur votre tableau de bord immobilier ! "
    "Explorez les annonces, analysez les prix au mètre carré, comparez les villes "
    "et obtenez des informations utiles pour mieux comprendre le marché."
)

)

# --------------------------------------------------
# 2. Chargement des données
#    ⚠️ ADAPTE LE CHEMIN SI BESOIN ⚠️
# --------------------------------------------------

@st.cache_data
def load_data():
    # Chemin complet vers ton CSV sur ton PC
    # Si le nom du fichier est juste ANNOUNCES_CLEAN.CSV,
    # modifie la ligne ci-dessous en conséquence.
    path = r"C:\Users\ebene\Desktop\DU Sorbonne Data Analytics\python_avancé\ANNONCES_CLEAN.CSV.csv"
    
    df = pd.read_csv(path)

    # On crée une colonne prix au m² (price_m2) si possible
    if "price_eur" in df.columns and "area_m2" in df.columns:
        # On évite les divisions par zéro
        df = df[df["area_m2"] > 0]
        df["price_m2"] = df["price_eur"] / df["area_m2"]
    else:
        st.warning("Les colonnes 'price_eur' ou 'area_m2' manquent dans le fichier.")
    
    return df

data = load_data()

# On fait une copie pour manipuler les filtres
df = data.copy()

# --------------------------------------------------
# 3. Barre latérale : filtres utilisateur
# --------------------------------------------------
st.sidebar.header("🧰 Filtres")

# Filtre sur la ville
if "city" in df.columns:
    villes = sorted(df["city"].unique().tolist())
    villes_choisies = st.sidebar.multiselect(
        "Ville(s)",
        options=villes,
        default=villes  # Par défaut, toutes les villes
    )
    if len(villes_choisies) > 0:
        df = df[df["city"].isin(villes_choisies)]

# Filtre sur le prix
if "price_eur" in df.columns and not df.empty:
    prix_min = int(df["price_eur"].min())
    prix_max = int(df["price_eur"].max())
    prix_min_sel, prix_max_sel = st.sidebar.slider(
        "Prix (€)",
        min_value=prix_min,
        max_value=prix_max,
        value=(prix_min, prix_max)
    )
    df = df[(df["price_eur"] >= prix_min_sel) & (df["price_eur"] <= prix_max_sel)]

# Filtre sur la surface
if "area_m2" in df.columns and not df.empty:
    surf_min = float(df["area_m2"].min())
    surf_max = float(df["area_m2"].max())
    surf_min_sel, surf_max_sel = st.sidebar.slider(
        "Surface (m²)",
        min_value=float(round(surf_min)),
        max_value=float(round(surf_max)),
        value=(float(round(surf_min)), float(round(surf_max)))
    )
    df = df[(df["area_m2"] >= surf_min_sel) & (df["area_m2"] <= surf_max_sel)]

# Filtre sur le nombre de pièces
if "rooms" in df.columns and not df.empty:
    rooms_min = int(df["rooms"].min())
    rooms_max = int(df["rooms"].max())
    rooms_min_sel, rooms_max_sel = st.sidebar.slider(
        "Nombre de pièces",
        min_value=rooms_min,
        max_value=rooms_max,
        value=(rooms_min, rooms_max)
    )
    df = df[(df["rooms"] >= rooms_min_sel) & (df["rooms"] <= rooms_max_sel)]

st.sidebar.markdown("---")
st.sidebar.write(f"Nombre d'annonces après filtres : **{len(df)}**")

# Si plus aucune ligne après filtres, on arrête
if df.empty:
    st.error("Aucune annonce ne correspond aux filtres sélectionnés. Diminue les contraintes.")
    st.stop()

# --------------------------------------------------
# 4. Indicateurs de base (KPI)
# --------------------------------------------------
st.subheader("📊 Indicateurs globaux")

col1, col2, col3 = st.columns(3)

with col1:
    if "price_m2" in df.columns:
        st.metric("Prix moyen au m²", f"{df['price_m2'].mean():.0f} €/m²")
    else:
        st.metric("Prix moyen au m²", "N/A")

with col2:
    if "price_eur" in df.columns:
        st.metric("Prix moyen", f"{df['price_eur'].mean():.0f} €")
    else:
        st.metric("Prix moyen", "N/A")

with col3:
    if "area_m2" in df.columns:
        st.metric("Surface moyenne", f"{df['area_m2'].mean():.1f} m²")
    else:
        st.metric("Surface moyenne", "N/A")

# --------------------------------------------------
# 5. Graphiques principaux (avec des onglets)
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "Prix au m² par ville",
    "Surface vs prix",
    "Tableau des annonces"
])


# Sélection uniquement des variables numériques
corr = df.select_dtypes(include=['int64', 'float64']).corr()

st.subheader("🔗 Matrice de corrélation")

fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)
# ====== Onglet 1 : prix au m² par ville ======
with tab1:
    st.markdown("### 📍 Distribution du prix au m² par ville")

    if "price_m2" in df.columns and "city" in df.columns:
        # Histogramme
        fig_hist = px.histogram(
            df,
            x="price_m2",
            color="city",
            nbins=40,
            labels={"price_m2": "Prix au m² (€)", "city": "Ville"},
            title="Histogramme du prix au m²"
        )
        st.plotly_chart(fig_hist, use_container_width=True)

        # Boxplot
        fig_box = px.box(
            df,
            x="city",
            y="price_m2",
            labels={"city": "Ville", "price_m2": "Prix au m² (€)"},
            title="Boxplot du prix au m² par ville"
        )
        st.plotly_chart(fig_box, use_container_width=True)
    else:
        st.warning("Colonnes 'price_m2' ou 'city' manquantes pour ces graphiques.")

# ====== Onglet 2 : corrélation surface / prix ======
with tab2:
    st.markdown("### 📐 Corrélation entre surface et prix")

    if "area_m2" in df.columns and "price_eur" in df.columns:
        fig_scatter = px.scatter(
            df,
            x="area_m2",
            y="price_eur",
            color="city" if "city" in df.columns else None,
            hover_data=["rooms", "postcode"] if "rooms" in df.columns else None,
            labels={"area_m2": "Surface (m²)", "price_eur": "Prix (€)"},
            title="Nuage de points : surface vs prix"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("Colonnes 'area_m2' ou 'price_eur' manquantes pour ce graphique.")

# ====== Onglet 3 : tableau des annonces ======
with tab3:
    st.markdown("### 📋 Tableau détaillé des annonces")

    colonnes_affichees = [col for col in [
        "city", "postcode", "titles",
        "rooms", "area_m2", "land_m2",
        "price_eur", "price_m2"
    ] if col in df.columns]

    st.dataframe(
        df[colonnes_affichees].sort_values("price_eur", ascending=True),
        use_container_width=True
    )

st.caption(
    "Merci pour votre visite! "
    "Continuez vos analyses afin de mieux décidez de votre investissement."
)
