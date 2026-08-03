import pandas as pd

df = pd.read_pickle('./DATA/APR_BAZA_2026.pkl')

print(df.info())

df.drop(columns=['SifraOpstine_x', 'NazivOpstine_x'], inplace=True)
df.rename(columns={'SifraOpstine_y': 'SifraOpstine', 'NazivOpstine_y': 'NazivOpstine'}, inplace=True)

df_delatnosti = pd.read_json('./DATA/klasifikacija_delatnosti.json')

df_delatnosti.rename(columns={'idkd08': 'SifraDelatnosti',
                              'nkd081': 'NazivDelatnosti'}, inplace=True)

df_delatnosti.drop(columns=['rbrkd08', 'idjezik'], inplace=True)

df = pd.merge(df, df_delatnosti, on='SifraDelatnosti', how='left')

df = df[df['SifraDelatnosti'].astype(str).str.startswith('11')]

df.describe().T.to_excel('./OUTPUT/STAT_OPIS.xlsx')

print(df.nunique())

print(df['NazivDelatnosti'].unique())

nase_kategorije = {
'Proizvodnja osvežavajućih pića, mineralne vode i ostale flaširane vode' : 'Bezalkoholno pice',
'Proizvodnja piva' : 'Alkoholno pice',
'Proizvodnja slada' : 'Alkoholno pice',
'Destilacija, prečišćavanje i mešanje pića' : 'Alkoholno pice',
'Proizvodnja vina od grožđa' : 'Alkoholno pice',
'Proizvodnja pića i ostalih voćnih vina' : 'Alkoholno pice',
'Proizvodnja ostalih nedestilovanih fermentisanih pića' : 'Alkoholno pice'
}

df['NasaKategorija'] = df['NazivDelatnosti'].map(nase_kategorije)

df_grouped = df.groupby('NasaKategorija').agg({'UkupniPrihodi' : 'sum', 'ProsecanBrojZaposlenih' : 'sum', 'NetoDobitak' : 'sum', 'NetoGubitak' : 'sum', 'PoslovnoIme' : 'count'})


df_grouped['NetoRezultat'] = df_grouped['NetoDobitak'] - df_grouped['NetoGubitak']

#print(df_grouped.head())

def prebaci_u_m_evre(x):
    return x/117_100

kolone_nad_kojima_cemo_prineniti_funkciju = ['UkupniPrihodi', 'NetoDobitak', 'NetoGubitak', 'NetoRezultat']

for kolona in kolone_nad_kojima_cemo_prineniti_funkciju:
    df_grouped[kolona] = df_grouped[kolona].apply(prebaci_u_m_evre)

print(df_grouped.head())
