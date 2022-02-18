from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd

data = pd.read_csv("https://vega.github.io/vega-lite/data/seattle-weather.csv")

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.layout = html.Div([
    html.Iframe(
        id='line',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='ycol-widget',
        value='precipitation',
        options=[{'label': 'precipitation', 'value': 'precipitation'},
                 {'label': 'wind', 'value': 'wind'}])])

# Set up callbacks/backend
@app.callback(
    Output('line', 'srcDoc'),
    Input('ycol-widget', 'value'))
def plot_altair(ycol):
    chart = alt.Chart(data).mark_line().encode(
        x='date',
        y=ycol).interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)