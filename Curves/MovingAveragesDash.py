import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from MovingAverages import simple_moving_average, weighted_moving_average
from WeightFunctions import triangular_weights, exponential_weights
import numpy as np


x1 = list(np.linspace(2,7,200))
y1 = list(np.cos(x1)+np.random.normal(0,.3,200))


app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Type of Average:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    U = np.linspace(-1,1,22)
    t_weights = triangular_weights(U)
    e_weights = exponential_weights(U)
    
    Y = {"simple": simple_moving_average(y1,10),
         "triangular": weighted_moving_average(y1,10,t_weights),
         "exponential": weighted_moving_average(y1,10,e_weights)
        }
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x1, 'y': y1, 'type': 'line', 'name': "data"},
                {'x': x1, 'y': Y[str(input_data)], 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)