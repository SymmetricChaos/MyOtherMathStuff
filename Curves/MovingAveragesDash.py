import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

from MovingAverages import simple_moving_average, weighted_moving_average, moving_median
from WeightFunctions import triangular_weights, exponential_weights
import numpy as np

# Precreate some simple data
x1 = list(np.linspace(0,7,250))
y1 = list(np.cos(x1))
y2 = list(np.cos(x1)+np.random.normal(0,.5,250))

# Create the webapp
app = dash.Dash()

# Simple layout with only a dropdown to select the type of moving average
app.layout = html.Div([
    dcc.Dropdown(
        id='type_dropdown',
        options=[
            {'label': 'simple', 'value': 'simple'},
            {'label': 'triangular', 'value': 'triangular'},
            {'label': 'exponential', 'value': 'exponential'},
            {'label': 'median', 'value': 'median'}
        ],
        value='simple'
    ),
        
    html.Div(id='dd-output-container'),
    
])


# A function that can update the graph based on making callback to the dropdown
@app.callback(
    Output(component_id='dd-output-container', component_property='children'),
    [Input(component_id='type_dropdown', component_property='value')]
)
def update_value(input_data):
    
    U = np.linspace(-1,1,15)
    t_weights = triangular_weights(U)
    e_weights = exponential_weights(U)
    
    Y = {"simple": simple_moving_average(y2,7),
         "triangular": weighted_moving_average(y2,7,t_weights),
         "exponential": weighted_moving_average(y2,7,e_weights),
         "median": moving_median(y2,7)
        }
    
    T = {"simple": "simple moving average",
         "triangular": "triangular weighted moving average",
         "exponential": "exponential weighted moving average",
         "median": "moving median",
        }
    
    
    fig = go.Figure(
            {'layout': 
                {'title': T[str(input_data)],
                 'plot_bgcolor' : 'lightgrey'
                 }
            })
    fig.add_trace(go.Scatter(x=x1, y=y2,line=dict(color='grey', width=2)))
    fig.add_trace(go.Scatter(x=x1, y=Y[str(input_data)],line=dict(color='blue', width=2)))
    
    return dcc.Graph(
        id='example-graph',
        figure=fig
    )



if __name__ == '__main__':
    app.run_server(debug=True)