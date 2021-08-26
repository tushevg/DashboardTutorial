import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output

#Load Data
df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

#Initialise the app
app = dash.Dash(__name__)

#Define the app
app.layout = html.Div(
    children=[
        html.Div(className='row', #Define the row element
            children=[
                html.Div(className='four columns div-user-controls', #Define left element
                    children=[
                        html.H2('Dash - Stock Prices'),
                        html.P('Visualizing time series with Plotly - Dash'),
                        html.P('Pick one or more stocks from the dropdown below.'),
                    ]
                ),
            html.Div(className='eight comlumns div-for-charts bg-grey'), #Define right element
            
        ])
])
#Run the app ($ python app.py)
if __name__ == '__main__':
    app.run_server(debug=True)