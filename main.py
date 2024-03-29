import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

df_filtered['reviews'].describe().round(2)
df_filtered.loc[df_filtered['reviews'].idxmax()]

df_filtered['reviews'].value_counts() / df_filtered['reviews'].sum()*100

df_filtered[['categoryName','stars']].value_counts().sort_index().sort_values(ascending=False)

#======== INTERPRETAÇÃO DE GRÁFICOS ========
sns.set()
sns.set_context('poster')

df[df['isBestSeller']==True].describe().round(2)
fig,ax=plt.subplots(figsize=(15,8))
fig.suptitle('Estrelas por grupo de vendedor')
sns.boxplot(y='stars',x='isBestSeller',data=df,palette='rainbow',whis=8.0)

# HISTOGRAMA
fig,ax=plt.subplots()
sns.histplot(data=df,ax=ax,x='stars',binwidth=1.0)






