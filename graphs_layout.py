
layout_pie = dict(  title = "Graph 2: Production balance over the selected timeframe",
                    #margin = dict(l=20, r=20, t=20, b=20),
                    showlegend = True,
                    paper_bgcolor = "rgba(0,0,0,0)",
                    plot_bgcolor = "rgba(0,0,0,0)",
                    font = {"color": "black"},
                    autosize = False,)


layout_graph = dict(title="Graph 1: Electricity production and consumption",
                    autosize=False,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    xaxis=dict(rangeselector=dict(
                                                buttons=list([
                                                    dict(count=1,
                                                         label="1m",
                                                         step="month",
                                                         stepmode="backward"),
                                                    dict(count=6,
                                                         label="6m",
                                                         step="month",
                                                         stepmode="backward"),
                                                    dict(count=1,
                                                         label="YTD",
                                                         step="year",
                                                         stepmode="todate"),
                                                    dict(count=1,
                                                         label="1y",
                                                         step="year",
                                                         stepmode="backward"),
                                                    dict(step="all")
                                                ])
                                            ),
                            rangeslider=dict(visible=True),
                            type="date"
                            )
        )
