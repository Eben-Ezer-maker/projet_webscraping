# ImmoDecision – Analyse du marché immobilier

ImmoDecision est un pipeline complet d'analyse du marché immobilier en France, structuré autour de quatre composants :

1. **Nettoyage des données brutes**
2. **Analyses statistiques et économétriques**
3. **Dashboard interactif Streamlit**
4. **Outils avancés : corrélations, modèles prédictifs et analyse énergétique (DPE)**

Ce projet offre une vue complète du marché, de la donnée brute jusqu’à la visualisation professionnelle.

---

## 📁 1. Structure du projet

Nettoyage des données (CLEAN_DATA.py)

Le script prend le fichier brut ANNONCES_GLOBAL_V18.csv et génère data_cleaned.csv.

Il réalise notamment :

conversion des colonnes prix, surface, terrain en numérique

filtrage des valeurs aberrantes

extraction robuste de la lettre du DPE

calcul du prix_m2

suppression des lignes incohérentes

normalisation et nettoyage des colonnes textuelles

sortie d'une base propre prête pour l’analyse

Exécution :
python CLEAN_DATA.py


Le fichier généré data_cleaned.csv est utilisé dans le dashboard Streamlit.

📊 4. Étape 2 – Analyse descriptive (ANALYSE.py)

Ce script produit les analyses statistiques essentielles :

statistiques globales

statistiques par ville

matrice de corrélation (CSV + Heatmap PNG)

histogrammes et boxplots

rapports exportés (CSV + graphiques)

Arborescence générée :
resultats_analyse/
    ├── stats_descriptives_globales.csv
    ├── stats_prix_m2_par_ville.csv
    ├── matrice_correlation.csv
    └── figures/
        ├── heatmap_correlation.png
        ├── hist_prix.png
        ├── hist_prix_m2.png
        ├── hist_surface.png
        └── box_prix_m2_par_ville_top10.png

Exécution :
python ANALYSE.py

📘 5. Étape 3 – Analyse économétrique (ANALYSES_ET_TESTS.ipynb)

Le notebook contient :

création des variables transformées (log_prix_m2, log_surface, etc.)

estimation d’un modèle hédonique :

log(prix_m2) = f(surface, pièces, type, ville)


tests statistiques :

Shapiro–Wilk (normalité des résidus)

Breusch–Pagan (hétéroscédasticité)

VIF (multicolinéarité)

Durbin–Watson (autocorrélation)

visualisation des résidus et diagnostics graphiques

À ouvrir dans VS Code ou Jupyter Notebook.

📊 6. Étape 4 – Dashboard Streamlit (DASHBOARD.py)

Le tableau de bord interactif ImmoDecision permet d’explorer le marché immobilier de manière visuelle et intuitive.

Lancer l’application :
streamlit run DASHBOARD.py

🖥️ Pages du Dashboard
🔹 1. Accueil & KPI

Prix moyen

Prix/m² médian

Surface moyenne

Nombre d’annonces

Carte interactive Folium

Top 5 des biens (prix total / prix/m²)

🔹 2. Analyses & Marché

Boxplots des prix/m² par ville

Histogrammes du prix/m²

Analyse Surface ↔ Prix (corrélation + régression linéaire)

Analyse énergétique (DPE) :

interprétation A → G

comparaison prix/m² par classe

calcul automatique de la “prime verte”

🌟 Avec commentaires automatiques pour guider l’utilisateur non spécialiste.

🔹 3. Corrélations & Statistiques

Statistiques descriptives (moyenne, médiane, écart-type, etc.)

Matrice de corrélation interactive (Plotly Heatmap)

Détection automatique de la corrélation la plus forte

Explications en langage simple

🔹 4. Modélisation (IA et Économétrie)
Régression linéaire (OLS)

modèle : log(prix) ~ log(surface) + C(type)

R² ajusté

rapport complet Statsmodels

Random Forest

importance des caractéristiques

graphique horizontal

explication de l’impact des variables

🔹 5. Le Conseiller (assistant d’achat)

Simulation personnalisée selon :

ville choisie

budget maximal

surface minimale souhaitée

Le module retourne :

prix/m² médian

surface achetable estimée

faisabilité du projet

liste des annonces proches de vos critères



🧑‍💻 7. Version recommandée

Python 3.10+

📝 8. Bonnes pratiques d'utilisation

Toujours exécuter CLEAN_DATA.py avant toute analyse si les données brutes changent

Vérifier que data_cleaned.csv se trouve au même emplacement que DASHBOARD.py

Utiliser un environnement virtuel pour réduire les conflits de dépendances

Limiter l’affichage à 300–500 points maximum pour des performances optimales dans la carte
