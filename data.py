import plotly.express as px
import pandas as pd

df = pd.read_csv('telecom_users.csv') #abre o arquivo como um dataframe
df = df.drop(['Unnamed: 0'], axis=1) #exclue coluna (axis=1) ['Unnamed: 0'] pq ela n foi identificada
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors = 'coerce') #converte a coluna toda pra int pq ela é só numero
df = df.dropna(how='all', axis=1) #dropa (exclui) todas colunas (axis1) com todos valores vazios (NaN)
df = df.dropna() #dropa as linhas (axis0 implicito) com alguma coluna vazia (any implicito)
lista = [] #cria lista vazia
for coluna in df: #percorre o dataframe e suas colunas
    if coluna != 'IDCliente': #ignora a coluna ['IDCliente']
        fig = px.histogram(df, x=coluna, color= "Churn") #cria um histograma da coluna pelos cancelamentos (['Churn'])
        lista.append(fig) #joga esse gráfico na lista criada
for i in lista: #percorre a lista
    i.show() #cria o sie pra mostrar o gráfico


print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) #mostra a porcentagem de cancelamentos de serviço (churns) do df o .map serve pra formatar a lista inteira sem um iterador
print(df.info()) #printa infos do df

# # criar dashboard
# # dcc = dash core Component

# from msilib.schema import Component
# from dash import Dash, html, dcc, Input, Output
# app = Dash(__name__)
# app.layout = html.Div(children=[
#     html.H1(children= 'Faturamento das Lojas da Base de dados'),
#     html.H2(children='Gráfico de Vendas Produto x Loja'),
#     html.Div(children = 'Observações extras:'),
#     dcc.Dropdown(lojas, value='Todas', id='lista_lojas'),
#     dcc.Graph(
#         id = 'Gráfico de qtd de vendas/prod',
#         figure=fig)])
# @app.callback(
#     Output('Gráfico de qtd de vendas/prod', 'figure'),
#     Input('lista_lojas', 'value'))
# def update_output(value):
#     if value == 'Todas':
#         fig = px.bar(df, x= 'Produto', y= 'Quantidade', color = 'ID Loja', barmode= 'group')
#     else:
#         tabela = df.loc[df['ID Loja']==value, :]
#         fig = px.bar(tabela, x= 'Produto', y= 'Quantidade', color = 'ID Loja', barmode= 'group')
#     return fig
# if __name__ == '__main__':
#     app.run_server(debug=True)
