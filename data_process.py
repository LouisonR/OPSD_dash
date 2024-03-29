from datetime import datetime as dt
from dateutils import relativedelta
import pandas as pd
import numpy as np
from fbprophet import Prophet


def load_data(csv_filepath, start_date):
    """ Returns a dataframe.

    Parameters:
        csv_filepath: string
        start_date: datetime
    Returns:
        df: pd.DataFrame
    """
    df = pd.read_csv(csv_filepath, parse_dates=['Date'], index_col="Date")
    df = df.loc[start_date:]
    return df

def make_labels(label):
    return [label + "_forecast", label + "_upper", label + "_lower"]


def create_model(df, column_name):
    """ Returns a prophet model.

    Parameters:
        df: pd.DataFrame
    Returns:
        model: fbprophet.Prophet
    """
    #DataFrame dedicated to Prophet
    df_input = pd.DataFrame(df[column_name].dropna()).reset_index().rename(columns={'Date': 'ds', column_name: 'y'})
    #Instanciation and fitting of the model
    model = Prophet(interval_width=0.95)
    model.fit(df_input[-1000:])
    return model

def fill_model_dict(df, label_lst):
    model_dict = {}
    for label in label_lst:
        model_dict[label] = create_model(df, label)
    return model_dict


def make_prediction(model, periods):
    """ Returns a prophet model forecast over a period of time.

    Parameters:
        model: fbprophet.Prophet
        periods: int
    Returns:
        forecast: pd.DataFrame
    """
    periods = int(periods)
    forecast = model.make_future_dataframe(periods=periods, freq='D', include_history=True)
    forecast = model.predict(forecast)
    return forecast

def make_pred_df(periods, model_dict):
    df_output = pd.DataFrame()
    for key in model_dict.keys():
        forecast = make_prediction(model_dict[key], periods)
        df_output[key + "_forecast"] = forecast.yhat
        df_output[key + "_upper"] = forecast.yhat_upper
        df_output[key + "_lower"] = forecast.yhat_lower.apply(lambda x: max(x, 0))
    df_output.index = forecast.ds
    return df_output
