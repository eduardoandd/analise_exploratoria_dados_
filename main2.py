import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_country = pd.read_csv('world_country_stats.csv')
df_population_c=pd.read_csv('world_population_by_country_2023.csv')
df_population_y=pd.read_csv('world_population_by_year_1950_2023.csv')

#TRATAMENTO
df_country.info()
df_country.isna().sum()
na_pct=df_country.isna().sum() / len(df_country)*100
#plot
cores= sns.color_palette('husl',len(na_pct))
fig, ax = plt.subplots(figsize=(18,5))
ax.bar(na_pct.index,na_pct.values,label=na_pct.index,color=cores)
ax.legend(loc='upper left')

df_population_c.info()
df_population_c.isna().sum()
na_pct=df_population_c.isna().sum() / len(df_population_c)*100
#plot
fig, ax = plt.subplots(figsize=(18,5))
ax.bar(na_pct.index,na_pct.values,label=na_pct.index,color=cores)
ax.legend(loc='upper left')


df_population_y.info()
df_population_y.isna().sum()
df_population_y.isna().sum() / len(df_population_y)*100
#plot
fig, ax = plt.subplots(figsize=(18,5))
ax.bar(na_pct.index,na_pct.values,label=na_pct.index,color=cores)
ax.legend(loc='upper left')