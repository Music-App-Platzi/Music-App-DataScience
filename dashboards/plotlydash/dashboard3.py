import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import psycopg2
import sqlalchemy
import matplotlib as plt

def create_data_table(df):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), 10))
        ])
    ])

def init_dashboard3(server, df):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard3/')

    # Create Layout
    dash_app.layout = html.Div(children=[
        html.H1(children='Dashboar Top Music'),
            html.Div(children=[dcc.Graph(
                id='histogram-graph',
                figure={
                    'data': [{
                        'x': df['name'],
                        'text': df['name'],
                        'y': df['sum'],
                        'name': 'Song hear by user',
                        'type': 'bar'
                    }],
                    'layout': {
                        'title': 'Top song hear',
                        'height': 500,
                        'padding': 150
                    }
                })
            ],
            id='dash-container'
        ),
        html.Div(children=create_data_table(df))
    ])
    return dash_app