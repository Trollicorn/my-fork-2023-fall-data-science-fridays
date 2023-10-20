import dash
from dash import dcc, html
import pandas as pd
import numpy as np

# Generate random data for the visualization
np.random.seed(0)
x_values = ['Category A', 'Category B', 'Category C', 'Category D']
y_values = np.random.randint(1, 100, size=len(x_values))

# Create a Pandas DataFrame
data = {'Category': x_values, 'Value': y_values}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Simple Bar Chart Example'),
    dcc.Graph(
        id='bar-chart',
        figure={
            'data': [
                {'x': df['Category'], 'y': df['Value'], 'type': 'bar', 'name': 'Category Value'},
            ],
            'layout': {
                'title': 'Bar Chart Visualization',
                'xaxis': {'title': 'Categories'},
                'yaxis': {'title': 'Values'}
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)