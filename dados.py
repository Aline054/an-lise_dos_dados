import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\aline\\OneDrive\\Documentos\\eventos_ofertas.csv')

print(df.head())
print(df.describe())
print(df.info())

plt.figure(figsize=(8, 5))
sns.countplot(x='Tipo_evento', data=df, palette='pastel')
plt.xlabel('Tipo de Evento')
plt.ylabel('Contagem de Eventos')
plt.title('Distribuição dos Tipos de Evento')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='Tipo_evento', y='Valor', data=df, palette='pastel', ci=None)
plt.xlabel('Tipo de Evento')
plt.ylabel('Valor Médio Gasto na Compra')
plt.title('Valor Médio Gasto na Compra por Tipo de Evento')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Tipo_evento', y='Tempo_decorrido', data=df, palette='pastel')
plt.xlabel('Tipo de Evento')
plt.ylabel('Tempo Decorrido (horas)')
plt.title('Tempo Decorrido por Tipo de Evento')
plt.show()

clientes_uniq = df['Cliente'].nunique()
clientes_repetidos = df['Cliente'].count() - clientes_uniq
print(f"Total de clientes únicos: {clientes_uniq}")
print(f"Total de clientes com eventos repetidos: {clientes_repetidos}")
plt.figure(figsize=(10, 6))
sns.histplot(df, x='Cliente', y='Valor', bins=30, kde=True, palette='pastel')
plt.xlabel('Cliente')
plt.ylabel('Valor Gasto na Compra')
plt.title('Valor Gasto na Compra por Cliente')
plt.show()
