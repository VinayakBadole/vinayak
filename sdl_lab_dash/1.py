##app with hello world
from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])

if __name__ == '__main__':
    app.run(debug=True)
    
    
# to run use    C:\Users\LENOVO\AppData\Local\Programs\Python\Python39\python.exe 1.py 