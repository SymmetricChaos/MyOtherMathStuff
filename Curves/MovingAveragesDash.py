import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from MovingAverages import simple_moving_average, weighted_moving_average
from WeightFunctions import triangular_weights, exponential_weights
import numpy as np


x1 = list(np.linspace(0,7,300))
y1 = list(np.cos(x1)+np.random.normal(0,.4,300))


app = dash.Dash()


app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'simple', 'value': 'simple'},
            {'label':  'triangular', 'value': 'triangular'},
            {'label': 'exponential', 'value': 'exponential'}
        ],
        value='simple'
    ),
    html.Div(id='dd-output-container')
])




@app.callback(
    Output(component_id='dd-output-container', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_value(input_data):
    U = np.linspace(-1,1,14)
    t_weights = triangular_weights(U)
    e_weights = exponential_weights(U)
    
    Y = {"simple": simple_moving_average(y1,6),
         "triangular": weighted_moving_average(y1,6,t_weights),
         "exponential": weighted_moving_average(y1,6,e_weights)
        }
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x1, 'y': y1, 'type': 'line', 'name': "data"},
                {'x': x1, 'y': Y[str(input_data)], 'type': 'line', 'name': "model"},
            ],
            'layout': {
                'title': f"{input_data} moving average"
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)