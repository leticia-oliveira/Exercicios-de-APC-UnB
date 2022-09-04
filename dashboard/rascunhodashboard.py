# -*- coding: utf-8 -*-
"""rascunhodashboard.ipynb

Automatically generated by Colaboratory.

"""

#GRÁFICO 2

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
#importa/lê a base de dados
df = pd.read_csv ('https://raw.githubusercontent.com/leticia-oliveira/Exercicios-de-APC-UnB/main/dashboard/datasets/medalhaspaises.csv')
dados = df.values.tolist()#enumera as células como lista
#prepara uma lista para receber os valores de *continentes, *medalhas de ouro, *prata e *bronze
c = [] 
o = []
p = []
b = []

#laço de repetição que coleta os dados da planilha e "entrega" eles para as listas
for cell in dados: 
  continent = cell[17]
  ouro = int(df.loc[df['continente']==continent]['total_gold'].sum())#reúne os dados de cada continente
  prata = df.loc[df['continente']==continent]['total_silver'].sum()#reúne os dados de cada continente
  bronze = df.loc[df['continente']==continent]['total_bronze'].sum()#reúne os dados de cada continente
#coloca os dados coletados em suas respectivas listas, sem repetí-los
  if cell[17] not in c:
    c.append(cell[17])
  if ouro not in o:
    o.append(ouro)
  if prata not in p:
    p.append(prata)
  if bronze not in b:

fig = px.bar(template="plotly_white")#define o formato do gráfico
#adiciona cada barra do gráfico
fig.add_trace(go.Bar(x=c, y=p, name='Medalhas de prata', marker_color='#BBBFC9', text = p, texttemplate = '%{text:.2s}', textposition='outside'))
fig.add_trace(go.Bar(x=c, y=o, name='Medalhas de ouro', marker_color='#FFDF00', text = o, texttemplate = '%{text:.2s}', textposition='outside'))
fig.add_trace(go.Bar(x=c, y=b, name='Medalhas de bronze', marker_color='#FFA366', text = b, texttemplate = '%{text:.2s}', textposition='outside'))

#edita a aparência do gráfico
fig.add_layout_image(
        x=0.25,
        sizex=4500,
        y=4590,
        sizey=4500,
        xref="x",
        yref="y",
        opacity=0.3,
        layer="below",
        source="https://cdn-icons-png.flaticon.com/512/523/523676.png"
)
fig.update_layout(
    title = 'Continentes e suas medalhas olímpicas',
    xaxis_tickfont_size=14,
    yaxis=dict(title='Quantidade de medalhas', titlefont_size=16, tickfont_size=14
    ),
    legend=dict(
        x=0.87, y=0.5
    ),
    barmode='group',
    bargroupgap=0.1 # Espaço entre as barras do mesmo continente
    )
fig.show()
