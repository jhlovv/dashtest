from dash import Dash, html, dcc, callback, Input, Output
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

# ==== 쥬피터 노트북에 127.0.0.1 링크 주소 표시 설정 옵션 ====
# 아래 두 줄 주석을 해제시 : app.run_server() 내 jupyter_mode="external" 옵션이 default로 됨 (브라이져에서 링크 주소로 보기)
# 아래 두 줄 주석을 사용시 : app.run_server() 내 jupyter_mode 옵션이 원래 defulat인 "internal"이 사용됨 (Jupyter에서 바로 보기)
# 개인의 선호에 따라 옵션을 변경하여 사용하면 됨
#jupyter_dash.default_mode="external"

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
app.run_server()