import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import plotly.graph_objs as go

def build_header():
    return html.Div(
                id="header",
                children=[
                    html.Div(
                        [
                            html.H1("GERMAN ELECTRICITY ANALYSIS"),
                            dcc.Link('Open Power System Data (OPSD)', href="https://data.open-power-system-data.org/time_series"),
                        ],
                        className="twelve columns",
                    ),
                    html.Img(id="logo_header", src="/assets/opsd_logo_small.png", style={'height':'10%','width':'10%'})
                ],
                className="row",
            )

def build_graphs(id1, id2):
    return html.Div(
                [
                    html.Div(
                        children =
                        [
                            dcc.Graph(id1),
                            html.Span(children=[" "]),
                        ],
                        className="eight columns",
                    ),
                    html.Div(
                        children =
                        [
                            dcc.Graph(id=id2),
                            html.Span(children=[" "]),
                        ],
                        className="three columns",
                    )
                ],
                className="column",
            )



def build_viz_header(start_date, end_date):
    return html.Div(
                id="header_viz",
                children=[
                    html.Span(children=[" "]),
                    html.H3("1. Visualization Module"),
                    html.H5("Select the timeframe you want to display"),
                    dcc.DatePickerSingle(   id='starting-date',
                                            min_date_allowed=start_date,
                                            max_date_allowed=end_date,
                                            initial_visible_month=start_date,
                                            date=str(start_date)
                                            ),
                    html.Span(children=[" "]),
                    dcc.DatePickerSingle(   id='ending-date',
                                            min_date_allowed=start_date,
                                            max_date_allowed=end_date,
                                            initial_visible_month=end_date,
                                            date=str(end_date)
                                            ),
                    html.Span(children=[" "]),
                    html.Button(id="submit-visu-button", n_clicks=0, children="Submit"),
                ],
                className="column",
            )


def build_pred_header(start_date, end_date):
    return html.Div(
                id="header_pred",
                children=[
                    html.Span(children=[" "]),
                    html.H3("   2. Prediction Module"),
                    html.H5("Period (in days) you want to forecast"),
                    dcc.DatePickerSingle(   id='starting-date-pred',
                                            min_date_allowed=start_date,
                                            max_date_allowed=end_date,
                                            initial_visible_month=start_date,
                                            date=str(start_date)
                                            ),
                    html.Span(children=[" "]),
                    dcc.Input(id="forecasting-period", value="90", type="text", style={'width': '130px'}),
                    html.Span(children=[" "]),
                    html.Button(id="submit-pred-button", n_clicks=0, children="Submit")
                ],
                className="column",
            )




def build_traces(df_sel, labels, colors):
    #define the different traces
    trace_consumption = go.Scatter( x=list(df_sel.index),
                                    y=list(df_sel.Consumption),
                                    name=labels[0],
                                    line=dict(color=colors[0]))

    trace_solar = go.Scatter(   x=list(df_sel.index),
                                y=list(df_sel.Solar),
                                name=labels[1],
                                line=dict(color=colors[1]))

    trace_wind = go.Scatter(   x=list(df_sel.index),
                                y=list(df_sel.Wind),
                                name=labels[2],
                                line=dict(color=colors[2]))

    return (trace_consumption, trace_solar, trace_wind)

def build_pie(df_sel, labels, colors):
    values = [df_sel.Wind.sum(), df_sel.Solar.sum(), df_sel.Consumption.sum()-df_sel.Wind.sum()-df_sel.Solar.sum()]
    trace_pie = go.Pie(labels=labels, values=values, hole=.3, marker_colors=colors)
    return trace_pie
