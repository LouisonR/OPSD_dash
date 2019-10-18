### OPSD dashboard
**Purpose**: Create a web application displaying German electricity production balance total consumption with viewer and forecast features.

## Data details
Wind, Solar and Consumption in Germany from 2006-01-01 until 20017-12-31.

## Architecture
* graphs_layout.py: generic and specific layouts for graph
* html_components.py: build function for html bricks: banner, menu, graphs
* data_process.py: loading data functions from database
* server.py: core of the dash app: css links, app layout, callbacks
* main.py: running file


## Features and graphs
* Visualization module: timeframe selection
* Prediction module: starting date ans forecasting period inputs

![logo](images/OPSD_dash.png)
