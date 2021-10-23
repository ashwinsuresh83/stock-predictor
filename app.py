from _plotly_utils.basevalidators import ImageUriValidator
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import date as dt
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output,State

app=dash.Dash(__name__,external_stylesheets=[dbc.themes.COSMO])
server=app.server

app.layout=html.Div([
    html.Div(
        [
            dbc.Row(dbc.Col(html.H2("Welcome to the stock predictor",className="start"),width={"offset":4})),
            dbc.Row(
                #stock code 
                dbc.Col(html.Label(" Input stock code"))
                
                
            ),
            dbc.Row([
                dbc.Col(dbc.Input(value='', type='text',id='stock-id')),
                dbc.Col(dbc.Button('Submit', id='submit-val', n_clicks=0,color="success"))]),
            html.Div([
                html.P("Select start date"),
                dcc.DatePickerSingle(
                    id='date-picker',
                    max_date_allowed=dt.today(),
                    date=dt.today()
                )
                
            ],className="date"),
            dbc.Row([
                #stock price button
                dbc.Col(dbc.Button('Stock price', id='stock-price-button'),width=2),
                #indicatorss button
                dbc.Col(dbc.Button('Indicators', id='indicators-button'),width={'size':2,"offset":2}),
                #number of days of forecast input
                dbc.Col(dbc.Input(value='', type='text',placeholder="number of days"),width=4),

                #forecast button
                dbc.Col(dbc.Button('Forecast', id='forecast-button'),width=2)

            ]),
        ],
        className=""
    ),
    html.Div(
        [
            html.Div(
                [
                    #logo
                    
                
                    #company name
                ],
                className="header",
                id='company-info'
            ),
            html.Div(#description
            id="Description",className="description_ticker"
            ),
            html.Div(
                [
                    #stock price plot 
                ],id="graphs-content"
            ),
            html.Div([
                #indicator plot

            ],id="main-content"),
            html.Div([
                #forecast plot
            ],id="forecast-content")
        ],
        className="content"
    )
],className="container")


@app.callback(
    Output(component_id='company-info',component_property='children'),
    [Input(component_id='submit-val',component_property='n_clicks')],
    [State(component_id='stock-id',component_property='value')],
    prevent_initial_call=True

)
def update_company_info(n,company):
    print(company)
    ticker=yf.Ticker(company)
    inf=ticker.info
    print(inf)
    return inf['longName']

if __name__== '__main__':
    app.run_server(debug=True)