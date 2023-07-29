import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\aline\\OneDrive\\Documentos\\dados_clientes.csv')
print(df.head())
print(df.describe())
print(df.info())

segmento_jovens = df[df['idade'] < 30]
segmento_adultos = df[(df['idade'] >= 30) & (df['idade'] < 60)]
segmento_idosos = df[df['idade'] >= 60]

plt.figure(figsize=(10, 6))
sns.histplot(df['idade'], bins=20, kde=True, color='blue', label='Todos')
sns.histplot(segmento_jovens['idade'], bins=20, kde=True, color='red', label='Jovens')
sns.histplot(segmento_adultos['idade'], bins=20, kde=True, color='green', label='Adultos')
sns.histplot(segmento_idosos['idade'], bins=20, kde=True, color='orange', label='Idosos')
plt.xlabel('Idade')
plt.ylabel('Contagem de Clientes')
plt.title('Distribuição de Idade nos Segmentos')
plt.legend()
plt.show()

segmento_masculino = df[df['genero'] == 'Masculino']
segmento_feminino = df[df['genero'] == 'Feminino']


plt.figure(figsize=(8, 5))
sns.countplot(x='genero', data=df, palette='pastel')
plt.xlabel('Gênero')
plt.ylabel('Contagem de Clientes')
plt.title('Distribuição de Gênero nos Segmentos')
plt.show()

correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Variáveis Numéricas')
plt.show()
