import pandas as pd

#Load Data
df = pd.read_csv('data/stockdata2.csv', index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

import dash
import dash_html_components as html

#Initialise the app
app = dash.Dash(__name__)

#Define the app
app.layout = html.Div()

#Run the app ($ python app.py)
if __name__ == '__main__':
    app.run_server(debug=True)

#app layout
app.layout = html.Div(children=[
    html.Div(className='row', #Define the row element
        children=[
            html.Div(className='four columns div-user-controls'), #Define left element

            html.Div(className='eight columns div-for-charts bg-grey') #Define right element

        ])
])

children = [
    html.H2('Dashboard for Stockprises'),
    html.P('Visualizing time series with Plotly - Dash'),
    html.P('Pick one or more stocks from the dropdown below.')
]