import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('output/task2.csv')
df = df[['sales', 'date']]
df = df.groupby('date')['sales'].sum().reset_index()

df = df.sort_values('date')
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser'),

    dcc.Graph(
        figure=px.line(
            df,
            x='date',
            y='sales',
            labels={'date': 'Date', 'sales': 'Sales ($)'},
            title='Pink Morsel Sales Over Time'
        )
    )
])

if __name__ == '__main__':
    app.run(debug=True)