#Controls and Callbacks


from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('RBI DATA states_wise_population_Income.csv')

# Initialize the app - incorporate CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    html.Div(className='row', children='App with Data, Graph, and Controls',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    html.Div(className='row', children=[
        dcc.RadioItems(options=['2001 -UNEMP', '2011 -UNEMP', '2000-01-INC'], value='2001 -UNEMP',
                       inline=True,
                       id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
        dcc.Input(id='state-search-input', type='text', placeholder='Search for a State'),
    ]),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(id='datatable',
                                 page_size=11,
                                 style_table={'overflowX': 'auto'})
        ]),
    ]),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='histo-chart-final')
        ])
    ])
])


# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Output(component_id='datatable', component_property='data'),
    Input(component_id='my-radio-buttons-final', component_property='value'),
    Input(component_id='state-search-input', component_property='value')
)
def update_graph_and_table(col_chosen, search_value):
    if search_value is None or len(search_value) == 0:
        # If search_value is empty or None, show the entire dataset
        filtered_df = df
    else:
        # Filter the DataFrame only if search_value is a non-empty string
        filtered_df = df[df['States_Union Territories'].str.contains(search_value, case=False, na=False)]

    fig = px.histogram(filtered_df, x='States_Union Territories', y=col_chosen, histfunc='avg')
    return fig, filtered_df.to_dict('records')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
