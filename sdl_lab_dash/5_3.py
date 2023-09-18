#Dash Mantine Components
#Dash Mantine is a community-maintained library built off of the Mantine component system. Dash Mantine is another powerful way of customizing 
# app layouts. The Dash Mantine Components uses the Grid module to structure the layout. Instead of defining a row, we define a dmc.
# Grid, within which we insert dmc.Cols and define their 
# width by assigning a number to the span property



from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# Incorporate data
df = pd.read_csv('RBI DATA states_wise_population_Income.csv')

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dmc.Container([
    dmc.Title('App with Data, Graph, and Controls', color="blue", size="h3"),
    dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in ['2001 -UNEMP', '2011 -UNEMP', '2000-01-INC']],
            id='my-dmc-radio-item',
            value='2001 -UNEMP',
            size="sm"
        ),
    dmc.Grid([
        dmc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=12),
        dmc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=12),
    ]),

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='States_Union Territories', y=col_chosen, histfunc='avg')
    return fig

# Run the App
if __name__ == '__main__':
    app.run(debug=True)

