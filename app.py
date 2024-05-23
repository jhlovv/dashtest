from dash import Dash, html, dcc, callback, Input, Output
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

# https://icon-sets.iconify.design/?query=bread

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

baguette_b = DashIconify(
        icon="mdi:bread",
        width=150)
baguette_a =  DashIconify(
        icon="noto:baguette-bread",
        width=150)

mini_b = DashIconify(
        icon="fluent-emoji-high-contrast:flatbread",
        width=150)

mini_a = DashIconify(
        icon="twemoji:flatbread",
        width=150)

bread_b = DashIconify(
        icon="emojione-monotone:bread",
        width=150)
bread_a = DashIconify(
        icon="emojione:bread",
        width=150)


app.layout = html.Div([
    html.H1('Make Bread!', className='bg-warning text-center m-2 p-2'),
    dbc.Container([dbc.Col(html.Div(baguette_b)),
                  dbc.Col(html.Div(mini_b)),
                  dbc.Col(html.Div(bread_b))])  
])
app.run_server(debug=True, port=8050)
