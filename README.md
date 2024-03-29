### OPSD dashboard
**Purpose**: Create a web application displaying German electricity production balance total consumption with viewer and forecast features.

## Data details
Wind, Solar and Consumption in Germany from 2006-01-01 until 20017-12-31 (source: https://open-power-system-data.org/)

## Architecture
* graphs_layout.py: generic and specific layouts for graph
* html_components.py: build function for html bricks: banner, menu, graphs
* data_process.py: loading data functions from database
* server.py: core of the dash app: css links, app layout, callbacks
* main.py: running file


## Features and graphs
* Visualization module: timeframe selection

  ![logo](images/visu_module.png)

* Prediction module: feature and timeframe selection, predictions done with a prophet model (https://facebook.github.io/prophet/). On each curve you can observe: actual data, mean prediction, upper and lower prediction with 95% confidence (interval_width).

  - Prediction viewer for electricity consumption forecast over 30 days
  ![logo](images/pred_module_cons.png)

  - Prediction viewer for wind production forecast over 90 days
  ![logo](images/pred_module_wind.png)

  - Prediction viewer for solar production forecast over 180 days
  ![logo](images/pred_module_solar.png)
