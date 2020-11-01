"""Instantiate a Dash app."""
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc


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

def init_dashboard1(server, df):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard1/')

    # Create Layout
    dash_app.layout = html.Div(children=[
        html.H1(children='Dashboard Popularity Music'),
            html.Div(children=[dcc.Graph(
                id='histogram-graph',
                figure={
                    'data': [{
                        'x': df['name'],
                        'y': df['popularity'],
                        'name': 'Popularity Music',
                        'type': 'bar'
                    }],
                    'layout': {
                        'title': 'Popularity Music',
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


