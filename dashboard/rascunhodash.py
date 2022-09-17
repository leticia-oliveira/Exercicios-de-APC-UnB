import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from dash import Dash, dcc, html, Output, Input

#leitura do dados do dataFrame
data = pd.read_csv('https://raw.githubusercontent.com/leticia-oliveira/Exercicios-de-APC-UnB/main/dashboard/datasets/medalhaspaises.csv')
df = pd.DataFrame(data)
dados = df.values.tolist()

#inicio do grafico de raling individual de paises --------------------------------------------------------------------

def cria_grafico_mais_medalha_ouro(qtd_paises):

    #importa/lê a base de dados
    df = pd.read_csv('https://raw.githubusercontent.com/leticia-oliveira/Exercicios-de-APC-UnB/main/dashboard/datasets/medalhaspaises.csv')
    df_ordenado = df.sort_values(by='total_gold', ascending=False)
    dados = df_ordenado.values.tolist()  # enumera as células como lista

    #prepara uma lista para receber os valores de *países e *medalhas de ouro
    p = []
    o = []

    #laço de repetição que coleta os dados da planilha e "entrega" eles para as listas
    for i in range(qtd_paises):  #valor quantidade de paises a ser mostrado
        p.append(dados[i][0])  #agrupando todos os paises
        o.append(dados[i][-5])  #agrupando todos os valores de medalha

    fig = px.bar(template="plotly_white")  #define o formato do gráfico

    #adiciona cada barra do gráfico
    fig.add_trace(go.Bar(x=o, y=p, name='Medalhas de ouro', marker_color='#FFDF00',
                marker_pattern_shape="x", text=o, texttemplate='%{text}', textposition='outside', orientation='h'))

    #edita a aparência do gráfico
    titulo='Os '+ str(qtd_paises) + ' países com mais medalhas de ouro'
    fig.update_layout(
        title=titulo,
        xaxis_tickfont_size=14,
        yaxis=dict(title='Quantidade de medalhas',
        titlefont_size=16, tickfont_size=14),
    )
    
    return fig

#fim do grafico de raling individual de paises --------------------------------------------------------------------



#inicio do grafico de continentes --------------------------------------------------------------------

#prepara uma lista para receber os valores dos *continentes
continente = []

#seleciona lista de continentes
for coluna in dados:
  if coluna not in continente:
    continente.append(coluna[-1])  # coluna de continentes
# remove os valores repetidos da lista
continente = list(dict.fromkeys(continente))


#função que coleta os dados de cada continente e os coloca em listas
def cria_grafico_continente(edicoes_olimpicas):

    ouros = [0, 0, 0, 0, 0, 0, 0, 0]
    pratas = [0, 0, 0, 0, 0, 0, 0, 0]
    bronzes = [0, 0, 0, 0, 0, 0, 0, 0]


    if edicoes_olimpicas == "Todas":
        id_ouro = -5
        id_prata = -4
        id_bronze = -3  
                
    if edicoes_olimpicas == "Verão":
        id_ouro = -15
        id_prata = -14
        id_bronze = -13
       
    if edicoes_olimpicas == "Inverno":
        id_ouro = -10
        id_prata = -9
        id_bronze = -8
        

    for coluna_continente in dados:
        if coluna_continente[-1] == continente[0]:
            ouros[0] = ouros[0]+coluna_continente[id_ouro]
            pratas[0] = pratas[0]+coluna_continente[id_prata]
            bronzes[0] = bronzes[0]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[1]:
            ouros[1] = ouros[1]+coluna_continente[id_ouro]  
            pratas[1] = pratas[1]+coluna_continente[id_prata]
            bronzes[1] = bronzes[1]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[2]:
            ouros[2] = ouros[2]+coluna_continente[id_ouro]
            pratas[2] = pratas[2]+coluna_continente[id_prata]
            bronzes[2] = bronzes[2]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[3]:
            ouros[3] = ouros[3]+coluna_continente[id_ouro]
            pratas[3] = pratas[3]+coluna_continente[id_prata]
            bronzes[3] = bronzes[3]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[4]:
            ouros[4] = ouros[4]+coluna_continente[id_ouro]
            pratas[4] = pratas[4]+coluna_continente[id_prata]
            bronzes[4] = bronzes[4]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[5]:
            ouros[5] = ouros[5]+coluna_continente[id_ouro]
            pratas[5] = pratas[5]+coluna_continente[id_prata]
            bronzes[5] = bronzes[5]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[6]:
            ouros[6] = ouros[6]+coluna_continente[id_ouro]
            pratas[6] = pratas[6]+coluna_continente[id_prata]
            bronzes[6] = bronzes[6]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[7]:
            ouros[7] = ouros[7]+coluna_continente[id_ouro]
            pratas[7] = pratas[7]+coluna_continente[id_prata]
            bronzes[7] = bronzes[7]+coluna_continente[id_bronze]
       

    #define o formato do gráfico
    fig = px.bar(template="plotly_white", barmode='group')

    #adiciona cada barra do gráfico
    fig.add_trace(go.Bar(x=continente, y=pratas, name='Medalhas de prata',
              marker_color='#BBBFC9', text=pratas, texttemplate='%{text:.2s}', textposition='outside'))
    fig.add_trace(go.Bar(x=continente, y=ouros, name='Medalhas de ouro', marker_color='#FFDF00',
              text=ouros, texttemplate='%{text:.2s}', textposition='outside'))
    fig.add_trace(go.Bar(x=continente, y=bronzes, name='Medalhas de bronze',
              marker_color='#FFA366', text=bronzes, texttemplate='%{text:.2s}', textposition='outside'))

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
    source="https://cdn-icons-png.flaticon.com/512/523/523676.png"  # imagem das olimpíadas
    )

    fig.update_layout(
    title='Continentes e suas medalhas olímpicas',
    xaxis_tickfont_size=14,
    yaxis=dict(title='Quantidade de medalhas', titlefont_size=16, tickfont_size=14),
    legend=dict(x=0.87, y=0.5),
    barmode='group',
    bargroupgap=0.1  #espaço entre as barras do mesmo continente
    )

    return fig

#fim do grafico de continentes --------------------------------------------------------------------




#inicio do grafico de pizza --------------------------------------------------------------------

def cria_grafico_pizza(edicao_olimpica):
    #criar listas
    paises = []
    valores = []
    estrutura = []

    #Variáveis ----------------------------------
    listsummertot = []
    listsummern = []
    listwintertot = []
    listwintern = []
    estrutura2 = []
    estrutura3 = []
    # -------------------------------------------

    def seleciona_valor(indice_estrutura): #buscando os valores de medalha relacionado a um pais
        return indice_estrutura[1] 

    def seleciona_valor2(indice_estrutura):
        return indice_estrutura[1]

    def seleciona_valor3(indice_estrutura):
        return indice_estrutura[1]

#gráfico de pizza (total de medalhas) ----------------------------------

    if edicao_olimpica == 'Todas':
    
        for coluna in dados:
            pais_valor = []  #lista que armazena o pais e o valor da repetição da coluna
            pais_valor.append(coluna[0])  #coluna de paises
            pais_valor.append(coluna[-2])  #coluna de valores totais
            estrutura.append(pais_valor)  #lista de lista para armazenar pais e valor de todas iteraçoes
                                          #para ordenar baseado no parametro valor mantendo a conexão com o n
                                          #e retorna o valor de medalhas como um criterio de ordenaçao

        estrutura.sort(reverse=True,key=seleciona_valor) #ordenando de forma decrescente atraves do atributo valor_total da lista

        for i in range(15):  #15 paises e 1 se5 valores
            paises.append(estrutura[i][0])  #agrupando todos os paises
            valores.append(estrutura[i][1])  #agrupando todos os valores de medalha

        grafico = px.pie(template="plotly_white", values=valores, names=paises,
                    title='15 países que mais conquistaram medalhas em todas as edições das Olimpíadas')

#gráfico de pizza (medalhas de verão) ----------------------------------

    if edicao_olimpica == 'Verão':

        for coluna in dados:
            pais_valor2 = []
            pais_valor2.append(coluna[0])
            pais_valor2.append(coluna[6])
            estrutura2.append(pais_valor2)

        estrutura2.sort(reverse=True, key=seleciona_valor2)

        for i in range(15):
            listsummern.append(estrutura2[i][0])
            listsummertot.append(estrutura2[i][1])

        grafico = px.pie(df, values=listsummertot, names=listsummern,
                    hole=.2, color_discrete_sequence=px.colors.sequential.OrRd,
                    title='15 países que mais conquistaram medalhas em edições de Verão das Olimpíadas')

#gráfico de pizza (medalhas de inverno) ----------------------------------

    if edicao_olimpica == 'Inverno':
        for coluna in dados:
            pais_valor3 = []
            pais_valor3.append(coluna[0])
            pais_valor3.append(coluna[11])
            estrutura3.append(pais_valor3)

        estrutura3.sort(reverse=True, key=seleciona_valor3)

        for i in range(15):
            listwintern.append(estrutura3[i][0])
            listwintertot.append(estrutura3[i][1])

        grafico = px.pie(df, values=listwintertot, names=listwintern,
                    hole=.2, color_discrete_sequence=px.colors.sequential.PuBu, 
                    title='15 países que mais conquistaram medalhas em edições de Inverno das Olimpíadas')

    return grafico

opcoes_grafico_pizza = ['Inverno', 'Verão', 'Todas']    

#fim do gráfico de pizza --------------------------------------------------------------------




#inicio do Grafico quadro de medalhas --------------------------------------------------------------------

def list_siglas(): 
    list_sigla = []    
    for coluna in dados:
      list_sigla.append(coluna[1])  #lista que armazena o pais e o valor da repetição da coluna
    return list_sigla

def name_pais(values):
    nome_do_pais = ' '
    for coluna in dados:
      if coluna[1]==values:
        nome_do_pais=coluna[0]
    return nome_do_pais


#cria o opções da lista drop Down
opcoes = list(list_siglas())

def quadroMedalhas(nome_pais):
    
  #Variáveis ----------------------------------
  gold = []   #
  silver = [] #
  bronze = [] #talvez isso possa ser apagado!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
  cat_gold = []#
  cat_silver = []#
  cat_bronze = []#
  # --------------------------------------------

  #estrutura de repetição que vai escanear o Dataframe e capturar os valores
  for i in dados:
      if i[0] == nome_pais:
          sum_gold = int(i[3])
          sum_silver = int(i[4])
          sum_bronze = int(i[5])

  #tratamento dos dados para transformá-los em lista
  medalhas = sum_gold, sum_silver, sum_bronze
  lst_medalhas = list(medalhas)
  return lst_medalhas

def cria_grafico_quadro_medalhas(value):

    fig = px.bar(template="plotly_white")

    if value == "BRA":
        lst_medalhas = quadroMedalhas('Brazil')

    else:
        lst_medalhas= quadroMedalhas(name_pais(value))

    #armazenamento dos dados capturados ----------------------------------
    cat_medalhas = ['Ouro', 'Prata', 'Bronze']  
    gold = [lst_medalhas[0]]
    silver = [lst_medalhas[1]]
    bronze = [lst_medalhas[2]]
    cat_gold = [cat_medalhas[0]]
    cat_silver = [cat_medalhas[1]]
    cat_bronze = [cat_medalhas[2]]
    #---------------------------------------------------------------------

    fig = px.bar(template="plotly_white")

    fig.add_trace(go.Bar(x=cat_gold, y=gold, name='Medalhas de Ouro', marker_color='#FFDF00', text = gold, texttemplate = '%{text}', textposition='outside'))
    fig.add_trace(go.Bar(x=cat_silver, y=silver, name='Medalhas de Prata', marker_color='#BBBFC9', text = silver, texttemplate = '%{text}', textposition='outside'))
    fig.add_trace(go.Bar(x=cat_bronze, y=bronze, name='Medalhas de Bronze', marker_color='#FFA366', text = bronze, texttemplate = '%{text}', textposition='outside'))

    fig.update_layout(
        title='Medalhas Olímpicas conquistadas pelo '+ name_pais(value)  +' (1896-2016)',
            title_font_size=32,
            xaxis_tickfont_size=28,
            yaxis=dict(title='Quantidade de Medalhas', titlefont_size=28, tickfont_size=18),
            legend=dict(x=0, y=1.0)
            )

    return fig   

#fim de todos os gráficos --------------------------------------------------------------------


#daqui pra cima nenhum gráfico aparece ainda, eles são apenas definidos ----------------------


#INICIO DO DASH -------------------------------------------------------------------- 

app = Dash(__name__)

#detalhar o que acontece aqui!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fig = cria_grafico_quadro_medalhas("USA")
fig1 = cria_grafico_pizza("Todas")
fig2 = cria_grafico_continente("Verão")
fig4 =  cria_grafico_mais_medalha_ouro(15)

#cor de fundo e texto padrão
colors = {'background': '#fffff', 'text': '#7FDBFF'}

app.layout = html.Div(
    style={'backgroundColor': colors['background']}, 
    children=[
        html.H1(
            children='Grupo A - Medalhas Olímpicas', #título
            style={'textAlign': 'center', 'color': '#000000'}
        ),

        html.Div(
            children='Os gráficos abaixo tem como objetivo apresentar ao público uma visão ampla e analítica sobre dados relacionados aos Jogos Olímpicos de 1896 a 2016, especificamente sobre as medalhas distribuídas neste período.', 
            style={'textAlign': 'center', 'color': colors['text']}
        ),

        #apresenta as opções do *gráfico de continentes com o valor 'Verão' selecionado como padrão
        dcc.RadioItems(
            options=[
            {'label': 'Todas', 'value': 'Todas'},
            {'label': 'Verão', 'value': 'Verão'},
            {'label': 'Inverno', 'value': 'Inverno'},
            ],
            value='Verão',
            id='edicao_olimpicas'
        ),
        #apresenta o gráfico de *continentes
        dcc.Graph(id='grafico_continente', figure=fig2),
        

        #apresenta o dropdown do *gráfico de pizza com o valor 'Verão' selecionado como padrão
        dcc.Dropdown(opcoes_grafico_pizza, value='Verão', id='summ_wint'),
        #apresenta o gráfico de pizza
        dcc.Graph(id='grafico_setor', figure=fig1),


        #texto acima do terceiro gráfico
        html.Div(children='Dash: Grafico de medalhas.', 
            style={'textAlign': 'center', 'color': colors['text']}),

        #dropdown do gráfico *quadro de medalhas com o valor 'BRA' selecionado como padrão
        dcc.Dropdown(opcoes, value='BRA', id='siglas_pais'),
        #apresenta o gráfico *quadro de medlahas
        dcc.Graph(id='quadro_de_medalhas', figure=fig),

        #adiciona o slider acima do gráfico de *ranking de medalhas de ouro
        dcc.Slider(0, 15, 1, value=15, marks=None, id='slider_qtd_medalhas',
                tooltip={"placement": "bottom", "always_visible": True}),
        #apresenta o gráfico *ranking de medalhas de ouro
        dcc.Graph(id='medalhas_de_ouro', figure=fig4)
        ]
    )

#callbacks --------------------------------------------------------------------

#o que torna a dashboard interativa. sempre que mudamos alguma informação de 
#entrada, o callback chama a função novamente, atualizando a saída *#*# foi o que eu entendi. corrija e me avise se estiver errado :)

@app.callback(
    Output('grafico_continente', 'figure'),
    Input('edicao_olimpicas', 'value'),
)
def update_output1(value):
    fig2 = cria_grafico_continente(value)
    return  fig2

@app.callback(
    Output('grafico_setor', 'figure'),
    Input('summ_wint', 'value'),
)
def update_output2(value):    
    fig1 = cria_grafico_pizza(value) 
    return  fig1

@app.callback(
    Output('quadro_de_medalhas', 'figure'),
    Input('siglas_pais', 'value')
)
def update_output3(value):
    fig = cria_grafico_quadro_medalhas(value)
    return  fig 

@app.callback(
    Output('medalhas_de_ouro', 'figure'),
    Input('slider_qtd_medalhas', 'value')
)
def update_output4(value):
    fig4 = cria_grafico_mais_medalha_ouro(value)
    return  fig4 


if __name__ == '__main__':
    app.run_server(debug=False)
