import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np

def simple_moving_average(Y,width=1):
    
    # Number of values considered at each step
    N = 2*width+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*width + y + [y[-1]]*width

    m_av = []
    for i in range(len(Y)):
        m_av.append(sum(y[i:N+i])/N)
    
    return m_av

x1 = np.linspace(2,7,200)
y1 = list(np.cos(x1)+np.random.normal(0,.3,200))
y2 = simple_moving_average(y1,5)

app = dash.Dash()


app.layout = html.Div(children=[
    html.H1(children='This Is My Dash Page'),



    html.Div(children='''
        Simple Moving Average of Sine Wave Data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x1, 'y': y1, 'type': 'line', 'name': 'base'},
                {'x': x1, 'y': y2, 'type': 'line', 'name': 'fitted'},
            ],
            'layout': {
                'title': 'Simplest Visualiztion I Could Think Of'
            }
        }
    )
])

    



if __name__ == '__main__':
    app.run_server(debug=False)