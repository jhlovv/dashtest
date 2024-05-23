from dash import Dash, html, dcc, callback, Input, Output, State
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("./project.csv")

# https://icon-sets.iconify.design/?query=bread

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

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

breads = df[df['분류'] == '식빵'].reset_index(drop=True)['과제명']
baguettes = df[df['분류'] == '바게트'].reset_index(drop=True)['과제명']
minis = df[df['분류'] == '단과자빵'].reset_index(drop=True)['과제명']

def get_question1(name):
    if name :
        targetname = html.H1(name)
    else:
        targetname = html.H1("Please select")
    
    return dbc.Container([dbc.Row(dbc.Col(targetname)),
                                  dbc.Row([
                                          dbc.Col(dbc.Container([
                                              html.H4("1차발효"),
                                              dcc.RangeSlider(0,90,10, id='s11'),
                                              html.H4("중간발효"),
                                              dcc.RangeSlider(0,30,5, id='s12'),
                                              html.H4("2차발효"),
                                              dcc.RangeSlider(0,50,5, id='s13')
                                                                ])),
                                          dbc.Col(dbc.Container([
                                              html.H4("1차굽기"),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.RadioItems(options=df['1차굽기시간'].unique(), inline=True),
                                              html.H4("2차굽기"),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.RadioItems(options=df['2차굽기시간'].unique(), inline=True),
                                              html.Button("Submit", n_clicks=0, id='submit1')
                                              
                                                                ])),        
                                                      ]),
                             ],
                            )

def get_question2(name):
    if name :
        targetname = html.H1(name)
    else:
        targetname = html.H1("Please select")
    
    return dbc.Container([dbc.Row(dbc.Col(targetname)),
                                  dbc.Row([
                                          dbc.Col(dbc.Container([
                                              html.H4("1차발효"),
                                              dcc.RangeSlider(0,90,10, id='s21'),
                                              html.H4("중간발효"),
                                              dcc.RangeSlider(0,30,5, id='s22'),
                                              html.H4("2차발효"),
                                              dcc.RangeSlider(0,50,5, id='s23')
                                                                ])),
                                          dbc.Col(dbc.Container([
                                              html.H4("1차굽기"),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.RadioItems(options=df['1차굽기시간'].unique(), inline=True),
                                              html.H4("2차굽기"),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.RadioItems(options=df['2차굽기시간'].unique(), inline=True),
                                              html.Button("Submit", n_clicks=0, id='submit2')
                                              
                                                                ])),        
                                                      ]),
                             ],
                            )
def get_question3(name):
    if name :
        targetname = html.H1(name)
    else:
        targetname = html.H1("Please select")
    
    return dbc.Container([dbc.Row(dbc.Col(targetname)),
                                  dbc.Row([
                                          dbc.Col(dbc.Container([
                                              html.H4("1차발효"),
                                              dcc.RangeSlider(0,90,10, id='s31'),
                                              html.H4("중간발효"),
                                              dcc.RangeSlider(0,30,5, id='s32'),
                                              html.H4("2차발효"),
                                              dcc.RangeSlider(0,50,5, id='s33')
                                                                ])),
                                          dbc.Col(dbc.Container([
                                              html.H4("1차굽기"),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.RadioItems(options=df['1차굽기시간'].unique(), inline=True),
                                              html.H4("2차굽기"),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.Dropdown(options=[i for i in range(150, 210, 10)]),
                                              dcc.RadioItems(options=df['2차굽기시간'].unique(), inline=True),
                                              html.Button("Submit", n_clicks=0, id='submit3')
                                              
                                                                ])),        
                                                      ]),
                             ],
                            )
    
task_tab = [dcc.Tabs(id='tabs', value='tabs', children=[
    dcc.Tab([get_question1("")], id='tab1', label='식빵'),
    dcc.Tab([get_question2("")], id='tab2', label='바게트'),
    dcc.Tab([get_question3("")], id='tab3', label='단과자빵')
                 ]),
                 html.Div(id='result')]

#untask_tab = [html.H3("please select 1 per category")]

app.layout = html.Div([
    html.H1('Make Bread!', className='bg-warning text-center m-2 p-2'),
    dbc.Row([dbc.Col(dbc.Container([html.Div(bread_b, className='text-center', id='bread_image'),
                                   dcc.Dropdown(options=breads, id='1')])),
             dbc.Col(dbc.Container([html.Div(baguette_b, className='text-center', id='baguette_image'),
                                   dcc.Dropdown(options=baguettes, id='2')])),
             dbc.Col(dbc.Container([html.Div(mini_b, className='text-center', id='minis_image'),
                                   dcc.Dropdown(options=minis, id='3')])),
            ]),
    dbc.Card(children=task_tab
                ,id = 'tab',
                 body=True)
                 
])


@callback( Output('tab1', 'children'),
          Input('1', 'value'),
         prevent_initial_call=True , suppress_callback_exceptions=True)
def get_state(value1):
    return get_question1(value1)

@callback( Output('tab2', 'children'),
          Input('2', 'value'),
         prevent_initial_call=True , suppress_callback_exceptions=True)
def get_state2(value1):
    return get_question2(value1)

@callback( Output('tab3', 'children'),
          Input('3', 'value'),
         prevent_initial_call=True, suppress_callback_exceptions=True)
def get_state3(value1):
    return get_question3(value1)


@callback(Output('bread_image', 'children'),
          Input('submit1', 'n_clicks'),
          State('1', 'value'),
          State('s11', 'value'),
          State('s12', 'value'),
          State('s13', 'value'),
         prevent_initial_call=False, suppress_callback_exceptions=True)
def get_test1(clicks, name, s11, s12, s13):
    if clicks:
        values = df[df['과제명'] == name].reset_index(drop=True)
        if s11[0] == values['1S'][0] and s11[-1] == values['1E'][0] and s12[0] == values['중S'][0]:
            return bread_a
        else: return bread_b
    else: return bread_b

@callback(Output('baguette_image', 'children'),
          Input('submit2', 'n_clicks'),
         prevent_initial_call=False, suppress_callback_exceptions=True)
def get_test2(clicks):
    if clicks:
        return baguette_a
    else: return baguette_b

@callback(Output('minis_image', 'children'),
          Input('submit3', 'n_clicks'),
         prevent_initial_call=False, suppress_callback_exceptions=True)
def get_test3(clicks):
    if clicks:
        return mini_a
    else: return mini_b


if __name__ == '__main__':
    app.run_server(debug=True)
