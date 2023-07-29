import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_portfolio = pd.read_csv('C:\\Users\\aline\\OneDrive\\Documentos\\portfolio_ofertas.csv')
print(df_portfolio.head())
print(df_portfolio.describe())
print(df_portfolio.info())
print(df_portfolio.columns)

plt.figure(figsize=(8, 5))
sns.countplot(x='Oferta', data=df_portfolio, palette='pastel')
plt.xlabel('Tipo de Oferta')
plt.ylabel('Contagem de Ofertas')
plt.title('Distribuição dos Tipos de Oferta')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Canal', data=df_portfolio, palette='pastel')
plt.xlabel('Canal de Envio')
plt.ylabel('Contagem de Ofertas')
plt.title('Distribuição dos Canais de Envio das Ofertas')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df_portfolio, x='Valor mínimo', bins=30, kde=True, palette='pastel')
plt.xlabel('Valor Mínimo')
plt.ylabel('Contagem de Ofertas')
plt.title('Distribuição do Valor Mínimo Necessário para Aproveitar as Ofertas')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df_portfolio, x='Recompensa', bins=30, kde=True, palette='pastel')
plt.xlabel('Pontuação de Recompensa')
plt.ylabel('Contagem de Ofertas')
plt.title('Distribuição da Pontuação de Recompensa por Oferta')
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df_portfolio, x='Duração', bins=30, kde=True, palette='pastel')
plt.xlabel('Duração (dias)')
plt.ylabel('Contagem de Ofertas')
plt.title('Distribuição da Duração das Ofertas')
plt.show()
