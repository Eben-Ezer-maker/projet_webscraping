import pandas as pd 
import numpy as np
#On importe les données 


df=pd.read_csv(r"C:\Users\ebene\Desktop\DU Sorbonne Data Analytics\python_avancé\ANNONCES_RAW.csv")
df
df.shape


# On commence le nettoyage des données 
# on enleve \n et espaces parasites
df['ville'] = df['ville'].str.strip()

# on extrait ville + code postal à partir de chaînes du type "— Brest 29200 —"
df[['city', 'postcode']] = df['ville'].str.extract(r'—\s*([A-Za-zÉÉÈÈÙÂÊÎÔÛÀÇàçéèîïôû\- ]+)\s+(\d{5})\s*—')

# optionnel : mettre en forme
df['city'] = df['city'].str.strip().str.title()
df['postcode'] = df['postcode'].astype('int')


##on crée une nouvelle variable afin de donner seulement le prix du bien immobilier
df['price_eur'] = (
    df['price']
    .str.replace(r'[^\d]', '', regex=True)   # garde seulement les chiffres
    .replace('', pd.NA)                      # au cas où vide
    .astype('Int64')                         # entier nullable
)

#on crée deux nouvelles variables (area_m2: la surface habitable et land_m2: la surface qui n'est pas habitée et surface_totale qui est la surface totale occupée par le bien immobilier)


df[['area_m2', 'land_m2']] = df['area'].str.extract(
    r'(\d+)\s*m²(?:/(\d+)\s*m²)?'
)

df['area_m2'] = df['area_m2'].astype('float')
df['land_m2'] = df['land_m2'].astype('float')   # restera NaN quand pas de terrain
df['surface_totale'] = df['area_m2'] + df['land_m2']

#Nouvelle varible rooms qui donne seulement le nombre de pièce de la maison


df['rooms'] = (
    df['room']
    .str.extract(r'(\d+)')   # on prend juste le nombre
    .astype('Int64')
)

#on crée aussi une variable pour le titre de l'annonce 

df['titles'] = df['title'].str.replace(r'\s+', ' ', regex=True).str.strip()


df1=df[['city', 'postcode', 'titles', 'price_eur', 'area_m2', 'land_m2', 'rooms']]

#on va va l'imputaion des valeurs manquantes



# 1. price_eur → médiane
df1['price_eur'] = df1['price_eur'].fillna(df1['price_eur'].median())

# 2. area_m2 → médiane
df1['area_m2'] = df1['area_m2'].fillna(df1['area_m2'].median())

# 3. land_m2 → remplacer NaN par 0 (aucun terrain)
df1['land_m2'] = df1['land_m2'].fillna(0)

# 4. rooms → mode (valeur la plus fréquente)
df1['rooms'] = df1['rooms'].fillna(df1['rooms'].mode()[0])



#On va vérifier si on a encore des valeurs manquantes
# mais on remarques que on a plus de valeurs manquantes
df1.isna().sum()

#Sauvegarde de la nouvelle base:
 
df1.to_csv("ANNONCES_CLEAN.CSV", index=False)

#Creation d'une nouvelle variable qui donne le prix au m2
df1['price_m2'] = df1['price_eur'] / df1['area_m2']

#On supprime certaines valeurs telle que 0 pour area_m2.
df1_clean = df1[(df1['area_m2'] > 10) & (df1['area_m2'] < 500)]
df1_clean = df1_clean[(df1_clean['price_m2'] > 500) & (df1_clean['price_m2'] < 15000)]

df1.loc[df1['area_m2'] < 10, 'area_m2'] = np.nan
df1.loc[df1['area_m2'] > 300, 'area_m2'] = np.nan
df1.loc[df1['price_m2'] < 500, 'price_m2'] = np.nan
df1.loc[df1['price_m2'] > 15000, 'price_m2'] = np.nan

df1['area_m2'] = df1.groupby('city')['area_m2'].transform(lambda x: x.fillna(x.median()))
df1['price_m2'] = df1.groupby('city')['price_m2'].transform(lambda x: x.fillna(x.median()))




