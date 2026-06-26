import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('output/task2.csv')

app = dash.Dash(__name__)

app.layout = html.Div(style={
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': '#f9f4f0',
    'padding': '40px',
    'maxWidth': '900px',
    'margin': '0 auto'
}, children=[

    html.H1('Pink Morsel Sales Visualiser', style={
        'textAlign': 'center',
        'color': '#c2185b',
        'marginBottom': '10px'
    }),

    html.P('Filter by region:', style={
        'textAlign': 'center',
        'color': '#555',
        'marginBottom': '5px'
    }),

    dcc.Checklist(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
        ],
        value=['north', 'east', 'south', 'west'],
        inline=True,
        style={'textAlign': 'center', 'marginBottom': '30px'}
    ),

    dcc.Graph(id='sales-chart')
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(regions):
    filtered = df[df['region'].isin(regions)]
    filtered = filtered.groupby('date')['sales'].sum().reset_index()
    filtered = filtered.sort_values('date')

    fig = px.line(
        filtered,
        x='date',
        y='sales',
        labels={'date': 'Date', 'sales': 'Sales ($)'},
        title='Pink Morsel Sales Over Time'
    )
    fig.update_traces(line_color='#e91e8c', line_width=2.5)
    fig.update_layout(
        plot_bgcolor='#fff0f6',
        paper_bgcolor='#f9f4f0',
        font_color='#333'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)