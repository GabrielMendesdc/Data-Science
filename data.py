from msilib.schema import Component
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# dcc = dash core Component


app = Dash(__name__)

df = pd.read_excel('Vendas.xlsx')
lojas = list(df['ID Loja'].unique())
lojas.append('Todas')

fig = px.bar(df, x= 'Produto', y= 'Quantidade', color = 'ID Loja', barmode= 'group')


app.layout = html.Div(children=[
    html.H1(children= 'Faturamento das Lojas da Base de dados'),
    html.H2(children='Gráfico de Vendas Produto x Loja'),
    html.Div(children = 'Observações extras:'),

    dcc.Dropdown(lojas, value='Todas', id='lista_lojas'),

    dcc.Graph(
        id = 'Gráfico de qtd de vendas/prod',
        figure=fig
    )
])

@app.callback(
    Output('Gráfico de qtd de vendas/prod', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == 'Todas':
        fig = px.bar(df, x= 'Produto', y= 'Quantidade', color = 'ID Loja', barmode= 'group')
    else:
        tabela = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela, x= 'Produto', y= 'Quantidade', color = 'ID Loja', barmode= 'group')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
