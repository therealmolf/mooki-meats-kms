# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc


# Define the page layout
layout = html.Div([
    html.Div(
        [],
        className="position-absolute w-100 h-100 bg-black opacity-75 top-0 start-0"
    ),
    html.Div(
        [
            html.Div(
              [
                html.Div(
                    [
                        html.H1([
                            "What do you ",
                            html.Span("need", style={"color":"green"}),
                            "?"],
                            className="display-huge mt-3 mb-3 lh-1"
                        ),
                        html.Span(
                            "Type whatever you need to get!",
                            className="h5 text-secondary fw-lighter")
                    ],
                    className="col-12 col-xl-10"
                ),
                html.Div(
                    [
                        html.Br(),
                        dbc.Input(id="input", placeholder="Type something...", type="text"),
                        html.P(id="output"),
                    ],
                    className="col-12 col-xl-8"
                ),
                dbc.ButtonGroup(
                    [
                        dbc.Button("Team", outline=True, color="light"),
                        dbc.Button("Employee", outline=True, color="light"),
                        dbc.Button("Knowledge", outline=True, color="light"),
                    ],
                )
              ],
              className="row d-flex align-items-center justify-content-center py-vh-1"
            )
        ],
        className="container py-vh-4 position-relative mt-5 px-vw-5 text-center"
    )
],
    className="w-100 overflow-hidden position-relative \
        bg-black text-white aos-init aos-animate"
)
