import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np


X = np.linspace(-2,2,200)
Y = np.sin(X)


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),



    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': X, 'y': Y, 'type': 'line', 'name': 'SF'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)