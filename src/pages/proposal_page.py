# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc


name_input = dbc.Row(
    [
        dbc.Label(
            "Name", 
            html_for="example-email-row", 
            width=2,
            className="form-label"),
        dbc.Col(
            dbc.Input(
                type="text", id="prop-by-input", placeholder="Enter name"
            ),
            width=10,
        ),
    ],
    className="mb-3",
)


know_type_input = dbc.Row(
    [
        dbc.Label("Knowledge Type", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text", id="know-type-input", placeholder="Enter Type"
            ),
            width=10,
        ),
    ],
    className="mb-3",
)


know_name_input = dbc.Row(
    [
        dbc.Label("Title", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text", id="know-name-input", placeholder="Enter Title"
            ),
            width=10,
        ),
    ],
    className="mb-3",
)


# Define the page layoutage layout
layout = dbc.Container([
    html.Div(
        [
            html.Div(
                [
                    html.Br(),
                    html.H3(
                        "Knowledge Proposal Form"
                    ),
                    html.P(
                        "",
                        className="lead border-top pt-5 mt-5 aos-init aos-animate"
                    ),
                    html.Form(
                        [
                            name_input,
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            know_type_input,
                            know_name_input
                        ],
                    )
                ],
                className="col-12 col-lg-10 col-xl-8"
            )
        ],
        className="row d-flex justify-content-center py-vh-5 pb-0"
    ),
    html.Div(
        [],
        className="row d-flex align-items-start justify-content-center py-vh-3 text-muted aos-init"
    )
    ],
    className="container bg-black border text-white"
)