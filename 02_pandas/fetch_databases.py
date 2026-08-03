import pandas as pd
import requests
import urllib3

REG_PODACI = 'https://data.gov.rs/sr/datasets/r/f5c28e0f-6782-4c78-bd51-0c40ec2a51f8'
FIN_IZVESTAJI = 'https://data.gov.rs/sr/datasets/r/52e1ec4c-d7a1-4e78-896c-9cd129acac0c'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response_reg = requests.get(REG_PODACI, verify=False)
response_reg.raise_for_status()

response_fin = requests.get(FIN_IZVESTAJI, verify=False)
response_fin.raise_for_status()

df_reg = pd.DataFrame(response_reg.json())
df_fin = pd.DataFrame(response_fin.json())

df_reg_podaci = pd.json_normalize(df_reg['Podaci'])
df_fin_podaci = pd.json_normalize(df_fin['Podaci'])


# Merge on 'PoslovnoIme' column
df_merged = pd.merge(df_reg_podaci, df_fin_podaci, on='PoslovnoIme', how='inner')
df_merged.to_pickle('./DATA/APR_BAZA_2026.pkl')