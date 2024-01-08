import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

#TRATAMENTO
df = pd.read_csv('amz_br_total_products_data_processed.csv')
df.info()
df.drop('boughtInLastMonth', inplace=True,axis=1)


# % DE DADOS VAZIOS 
df_none_percent=df.replace(0,pd.NA)
none_percent=df_none_percent.isna().sum() / len(df)*100

#PLOTANDO A QUANTIDADE DE VALORES VAZIOS NAS COLUNAS QUE TEM VALOR VAZIO
aux_none=none_percent[none_percent!=0]
min_value= aux_none.idxmin()
aux_none['textpositon'] = np.where(aux_none.index == min_value, 'outside','inside')

fig_none= px.pie(aux_none, values=aux_none.values, names=aux_none.index)
fig_none.update_traces(textposition=aux_none['textpositon'], textinfo='percent+label')

aux_none.drop('textpositon',inplace=True)


# % DE DADOS NÃO VAZIOS
df_value_percent=df.replace(0,pd.NA)
value_percent=df_value_percent.notna().sum() / len(df)*100
value_percent.notna().sum() / len(df)*100 + none_percent.isna().sum() / len(df)*100

#REMOVENDO TODOS OS VALORES IGUAIS A 0
df_filtered=df.replace(0,pd.NA)
df_filtered=df_filtered.dropna()
df_filtered.info()

# RECOVERTENDO
df_filtered[['price', 'listPrice', 'stars']] = df_filtered[['price', 'listPrice', 'stars']].astype(float)
df_filtered['reviews'] = df_filtered['reviews'].astype(int)
df_filtered.info()


