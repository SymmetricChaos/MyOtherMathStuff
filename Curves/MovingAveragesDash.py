import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from MovingAverages import simple_moving_average, weighted_moving_average
from WeightFunctions import triangular_weights, exponential_weights
import numpy as np

# Precreate some simple data
x1 = list(np.linspace(0,7,150))
y1 = list(np.cos(x1))
y2 = list(np.cos(x1)+np.random.normal(0,.4,150))

# Create the webapp
app = dash.Dash()

# Simple layout with only a dropdown to select the type of moving average
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
    

    
    html.Div(id='dd-output-container'),
    
])


# A function that can update the graph based on making callback to the dropdown
@app.callback(
    Output(component_id='dd-output-container', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_value(input_data):
    
    U = np.linspace(-1,1,14)
    t_weights = triangular_weights(U)
    e_weights = exponential_weights(U)
    
    Y = {"simple": simple_moving_average(y2,6),
         "triangular": weighted_moving_average(y2,6,t_weights),
         "exponential": weighted_moving_average(y2,6,e_weights)
        }
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x1, 'y': y2, 'type': 'line', 'name': "data"},
                {'x': x1, 'y': Y[str(input_data)], 'type': 'line', 'name': "model"},
            ],
            'layout': {
                'title': f"{input_data} moving average"
            }
        }
    )



if __name__ == '__main__':
    app.run_server(debug=True)