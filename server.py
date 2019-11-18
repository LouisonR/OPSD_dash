from collections import OrderedDict
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from datetime import datetime as dt
from dateutils import relativedelta
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from fbprophet import Prophet
from graphs_layout import layout_graph, layout_pie
from html_component import build_header, build_viz_header, build_pred_header, build_graphs, build_options, build_traces, build_pie
from data_process import load_data, create_model, make_prediction, make_pred_df, fill_model_dict, make_labels

#Inputs
csv_filepath = 'data/opsd_germany_daily.csv'

labels = ["Wind", "Solar", "Consumption"]
labels_pie = ["Wind", "Solar", "Others"]
colors = ["#424bf5", "#42f551", "#f44242"]
colors_pred = ["#8D93F9", "#B3FBB9", "#FAB3B3"]
colors_pie = ["#424bf5", "#42f551", "#dbde47"]
options = build_options(labels)

#Data
#Visualization module
start_date_viz = dt.today() - relativedelta(years=7)
df = load_data(csv_filepath, start_date_viz)
end_date_viz = df.index[-1]
#Prediction module
periods = 365
start_date_pred = end_date_viz - relativedelta(years=1)
end_date_pred = end_date_viz + relativedelta(days=periods)
model_dict = fill_model_dict(df, labels)
df_forecast = make_pred_df(periods, model_dict)

#css links
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css","/assets/style.css",]

#app
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

server = app.server

app.layout = html.Div(
    [
        build_header(),
        build_viz_header(start_date_viz, end_date_viz),
        build_graphs(id1="viz_line", id2="viz_balance"),
        build_pred_header(start_date_pred, end_date_viz, end_date_pred, options),
        build_graphs(id1="pred_line", id2="pred_balance"),
    ]
)


#Callbacks
#Visualization callback
@app.callback(  [Output("viz_line", "figure"), Output("viz_balance", "figure")],
                [Input('submit-visu-button', "n_clicks")],
                [State('starting-date', "date"), State('ending-date', "date")],
                )

def update_viz_graph(n_clicks, starting_date, ending_date):
    """ Returns a figures type: tuple of dict.

    Parameters:
        n_clicks (int): 0 | 1
        starting_date (datetime): the starting date of the timeframe selected
        ending_date (datetime): the ending date of the timeframe selected

    Returns:
        figures: tuple of figure (dict)

    """
    df_sel = df.loc[starting_date:ending_date]

    traces = build_traces(df_sel, labels, colors)
    trace_pie = build_pie(df_sel, labels_pie, colors_pie)

    figure_consumption = dict(data=traces, layout=layout_graph)
    figure_pie = dict(data=trace_pie, layout=layout_pie)

    return (figure_consumption, figure_pie)

#Prediction callback
@app.callback(  [Output("pred_line", "figure"), Output("pred_balance", "figure")],
                [Input('submit-pred-button', "n_clicks")],
                [State('var-id', "value"), State('starting-date-pred', "date"), State('ending-date-pred', "date")],
             )

def update_pred_graph(n_clicks, var_id, starting_date, ending_date):
    """ Returns a figure type: dict(data, layout).

    Parameters:
        n_clicks (int): 0 | 1
        var_id (int): variable selection 0 | 1 | 2
        periods (string): the period in days we want to predict
        starting_date (datetime): the starting date of the timeframe selected

    Returns:
        figures: tuple of figure (dict)

    """
    label = labels[var_id]
    labels_pred = make_labels(label)

    df_hist = df.loc[starting_date:]
    df_pred = df_forecast.loc[starting_date:ending_date]
    df_full = pd.concat([df_hist, df_pred], axis=0, sort=True)

    traces_viz = build_traces(df_hist, [label], [colors[var_id]])
    traces_pred = build_traces(df_pred, labels_pred, 3*[colors_pred[var_id]])
    trace_pie = build_pie(df_full, labels_pie, colors_pie)

    figure_consumption = dict(data=traces_viz + traces_pred, layout=layout_graph)
    figure_pie = dict(data=trace_pie, layout=layout_pie)

    return (figure_consumption, figure_pie)
