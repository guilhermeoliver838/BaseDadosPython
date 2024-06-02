import os
import pandas as pd
import plotly.express as px

lista_arquivos = os.listdir("C:/Users/guilh/OneDrive/Área de Trabalho/Estudos/Python/CursoPy/Vendas")

dataframes = []

for arquivo in lista_arquivos:
    if "Vendas" in arquivo:
        
        tabela = pd.read_csv(f"C:/Users/guilh/OneDrive/Área de Trabalho/Estudos/Python/CursoPy/Vendas/{arquivo}")
        dataframes.append(tabela)

tabela_total = pd.concat(dataframes, ignore_index=True)

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos [['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)


tabela_total ['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()


tabela_Lojas = tabela_total.groupby('Loja').sum()
tabela_Lojas = tabela_Lojas [['Faturamento']]
print(tabela_total)

grafico = px.bar(tabela_Lojas, x= tabela_Lojas.index, y= 'Faturamento')
grafico.show()


