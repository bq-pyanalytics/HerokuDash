#!/usr/bin/python
# -*- coding: utf-8 -*-

import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd

VALID_USERNAME_PASSWORD_PAIRS = {
    'ryakub': '123'
}

analytics = pd.read_csv("data/analytics.csv")
analytics['date'] = pd.to_datetime(analytics['date'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        "C:\\Users\\yakub\\Desktop\\practicum\\assets\\assets.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
    children=[
        html.H1(children='Тригонометрические функции', style={'textAlign': 'center',
                                                              'color': colors['text'],
                                                              'plot_bgcolor': colors['background'],
                                                              'backgroundColor': colors['background'],
                                                              'paper_bgcolor': colors['background'], }
                ),
        html.Div([
            html.Div([
                dcc.DatePickerRange(
                    minimum_nights=5,
                    clearable=True,
                    with_portal=True,
                    start_date_placeholder_text='Дата старта',
                    end_date_placeholder_text='Дарта окончания',
                    display_format='YYYY-MM-DD',
                    start_date='2020-10-01',
                    end_date='2020-12-31',
                    style=dict(display='flex',
                               justifyContent='center',
                               plot_bgcolor=colors['background'],
                               paper_bgcolor=colors['background'],
                               color=colors['text'],
                               backgroundColor=colors['background'],
                               font={'color': colors['text']}),

                    id='dt_selector'),
            ], className='four columns'),

            html.Div([
                dcc.Dropdown(
                    options=[
                        {'label': str(x), 'value': str(x)} for x in list(analytics['utm_source'].astype('str').unique())
                    ],
                    value=['yandex', 'google'],
                    multi=True,
                    style=dict(plot_bgcolor=colors['background'],
                               paper_bgcolor=colors['background'],
                               backgroundColor=colors['background'],
                               color=colors['text'],
                               font={'color': colors['text']}),
                    id='continent_selector_drop'),
            ], className='four columns', ),

            html.Div([
                dcc.Checklist(
                    options=[
                        {'label': 'cpo', 'value': 'cpo'},
                        {'label': 'cpa', 'value': 'cpa'},
                        {'label': 'cpc', 'value': 'cpc'}
                    ],
                    value=['cpc'],
                    labelStyle={"display": "inline"},
                    style=dict(display='flex', justifyContent='center'),
                    id='continent_selector_check'),

            ], className='four columns'),

        ], className='row'),
        html.Div([
            dcc.Graph(
                # параметр figure определяется динамически
                id='trig_func',
                style=dict(display='flex', justifyContent='center', hight='200px'),
            ),

        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    figure={
                        'data': [go.Bar(
                            x=[20, 14, 23],
                            y=['giraffes', 'orangutans', 'monkeys'],
                            name='Животные',
                            orientation='h')],
                        'layout': go.Layout(xaxis={'title': 'Страна'},
                                            yaxis={'title': 'Макс. % городского населения'},
                                            title={'text': 'DISPLAY ME!'},
                                            plot_bgcolor=colors['background'],
                                            paper_bgcolor=colors['background'],
                                            font={
                                                'color': colors['text']
                                            }

                                            )
                    },
                    # параметр figure определяется динамически
                    id='trig_func1',
                    style=dict(display='flex', justifyContent='center'),
                ),
            ], className='six columns', ),

            html.Div([
                dcc.Graph(
                    figure={
                        'data': [go.Bar(
                            x=[20, 14, 23],
                            y=['giraffes', 'orangutans', 'monkeys'],
                            name='Животные',
                            orientation='h')],
                        'layout': go.Layout(xaxis={'title': 'Страна'},
                                            yaxis={'title': 'Макс. % городского населения'},
                                            title={'text': 'DISPLAY ME!'},
                                            plot_bgcolor=colors['background'],
                                            paper_bgcolor=colors['background'],
                                            font={
                                                'color': colors['text']
                                            })
                    },
                    # параметр figure определяется динамически
                    id='trig_func2',
                    style=dict(display='flex', justifyContent='center'),
                ),

            ], className='six columns'),

        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    figure={
                        'data': [go.Bar(
                            x=[20, 14, 23],
                            y=['giraffes', 'orangutans', 'monkeys'],
                            name='Животные',
                            orientation='h')],
                        'layout': go.Layout(xaxis={'title': 'Страна'},
                                            yaxis={'title': 'Макс. % городского населения'},
                                            title={'text': 'DISPLAY ME!'},
                                            plot_bgcolor=colors['background'],
                                            paper_bgcolor=colors['background'],
                                            font={
                                                'color': colors['text']
                                            })
                    },
                    # параметр figure определяется динамически
                    id='trig_func3',
                    style=dict(display='flex', justifyContent='center'),
                ),
            ], className='six columns', ),

            html.Div([
                dcc.Graph(
                    figure={
                        'data': [go.Bar(
                            x=[20, 14, 23],
                            y=['giraffes', 'orangutans', 'monkeys'],
                            name='Животные',
                            orientation='h')],
                        'layout': go.Layout(xaxis={'title': 'Страна'},
                                            yaxis={'title': 'Макс. % городского населения'},
                                            title={'text': 'DISPLAY ME!'},
                                            plot_bgcolor=colors['background'],
                                            paper_bgcolor=colors['background'],
                                            font={
                                                'color': colors['text']
                                            })
                    },
                    # параметр figure определяется динамически
                    id='trig_func4',
                    style=dict(display='flex', justifyContent='center'),
                ),

            ], className='six columns'),

        ], className='row'),
        html.Div([
            dcc.Graph(
                figure={
                    'data': [
                        go.Bar(
                            x=['giraffes', 'orangutans', 'monkeys'],
                            y=[25, 20, 20],
                            marker=dict(
                                color='red',
                                line=dict(color='orange', width=3)),
                            name='Животные'),
                        go.Bar(
                            x=['giraffes', 'orangutans', 'monkeys'],
                            y=[10, 5, 54],
                            marker=dict(
                                color='green',
                                line=dict(color='orange', width=3)),
                            name='Животные'),

                    ],

                    'layout': go.Layout(xaxis={'title': 'Страна'},
                                        yaxis={'title': 'Макс. % городского населения'},
                                        title={'text': 'DISPLAY ME!'},
                                        barmode='stack',
                                        plot_bgcolor=colors['background'],
                                        paper_bgcolor=colors['background'],
                                        font={
                                            'color': colors['text']
                                        },
                                        )
                },
                # параметр figure определяется динамически
                id='trig_func5',
                style=dict(display='flex',
                           justifyContent='center',
                           plot_bgcolor=colors['background'],
                           paper_bgcolor=colors['background'],
                           font={
                               'color': colors['text']
                           },
                           ),
            ),

        ], className='row'),
    ],
    style={
        'plot_bgcolor': colors['background'],
        'paper_bgcolor': colors['background'],
        'backgroundColor': colors['background'],
        'color': colors['text'],
        'font': {'color': colors['text']},
    },
)


@app.callback(
    [Output('trig_func', 'figure'),
     ],
    [Input('dt_selector', 'start_date'),
     Input('dt_selector', 'end_date'),
     Input('continent_selector_drop', 'value'),
     Input('continent_selector_check', 'value'),

     ])
def update_figures(start_date, end_date, drop_values, check_values):
    # приводим строки дат к типу datetime
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # применяем фильтрацию
    analytics_with_filter = analytics[(analytics['date'] >= start_date) &
                                      (analytics['date'] <= end_date) &
                                      (analytics["utm_source"].isin(drop_values)) &
                                      (analytics["utm_medium"].isin(check_values))]

    # формируем графики для отрисовки с учётом фильтров
    data = [go.Bar(x=analytics_with_filter['utm_source'],
                   y=analytics_with_filter['order_sum'],
                   textposition='auto',
                   name='Сельское население'),
            # go.Scatter(x=analytics_with_filter['utm_source'],
            #            y=analytics_with_filter['order_sum'],
            #            mode='lines+markers',
            #            marker_color='crimson',
            #            name='sin(x)'),
            ]

    # формируем результат для отображения
    return (
        {
            'data': data,
            'layout': go.Layout(xaxis={'title': 'Год'},
                                yaxis={'title': '% городского населения'},
                                plot_bgcolor=colors['background'],
                                paper_bgcolor=colors['background'],
                                font={
                                    'color': colors['text']
                                }
                                ),

        },
    )


if __name__ == '__main__':
    app.run_server(debug=True)
