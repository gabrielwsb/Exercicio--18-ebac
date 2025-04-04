
 # código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Gerando o DataFrame
gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

# Gerando o gráfico
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico.set(title='Variação do preço da gasolina', xlabel='Dia', ylabel='Preço');

# Salvando o gráfico
plt.savefig('gasolina.png', dpi=300, bbox_inches='tight')