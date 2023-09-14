# Visualizing Data
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('RBI DATA states_wise_population_Income.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='2011 Census'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='States_Union Territories', y='2001 -UNEMP', histfunc='avg'))
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)