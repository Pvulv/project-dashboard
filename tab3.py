from dash import dcc, html, dash_table

def render_tab(df):
    layout = html.Div([
        html.H1('Kanały Sprzedaży', style={'text-align': 'center'}),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='store_dropdown',
                    options=[{'label': Store, 'value': Store} for Store in df['Store_type'].unique()],
                    value=df['Store_type'].unique()[0]
                ),
                dcc.Graph(id='bar-sales2')
                ], style={'width': '50%', 'margin': '0 auto', 'margin-bottom': '20px'}),
            
            html.Div([
                dcc.Dropdown(
                    id = 'day',
                    options=[{'label': day, 'value': day} for day in df['days'].unique()],
                    value= df['days'].unique()[0]
                ),
                html.Br(),
                dash_table.DataTable(
                    id='info',
                    data= df.to_dict('records'),
                    columns=[{'name': col, 'id': col} for col in df[['cust_id', 'DOB','Gender','country']]],
                    style_table= {'maxHeight': '300px','overflowY': 'auto','border': 'thin lightgrey solid'},
                    style_cell= {'textAlign': 'center', 'whiteSpace': 'normal', 'height': 'auto'}
                )
            ], style={'width': '50%'})
        ],style= {'display':'flex', 'flex-direction' : 'row'})
    ])
    return layout