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

#Run the app 
if __name__ == '__main__':
    app.run_server(debug=True)

