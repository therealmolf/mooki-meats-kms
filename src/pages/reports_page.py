# Import necessary libraries
from dash import html, ctx
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import Input, Output
from utils import db_connect
from app import app


knowledge_report = html.Div(
    [html.Div(
        [
            html.Div(),
            html.Div(
                "This is the knowledge text box",
                className="col-12 col-lg-10 col-xl-8 text-center my-5"
                )
        ],
        style={
            "background-color": "#224B0C",
            },
            className="col-6 d-flex align-items-center shadow rounded-5 p-0 aos-init aos-animate"
        ),
    html.Div(
        [
            html.Span(
                "The numbers",
                className="h5 text-secondary fw-lighter"
                ),
            html.H2(
                "Value",
                className="display-huge fw-bolder aos-init aos-animate"
                ),
            html.P(
                "This is a sample paragraph",
                className="h4 fw-lighter text-secondary"
                )
        ],
        className="col-5 offset-1"
        )
    ],
    className="row d-flex align-items-center"
    )




# Define the page layout
layout = html.Div([
    html.Div(
        [],
        # className="position-absolute w-100 h-100 \
        #     bg-black opacity-75 top-0 start-0"
    ),
    html.Div(
        [
            html.Div(
              [
                html.Div(
                    [
                        html.H1([
                            html.Span(
                                "Employee ",
                                style={"color": "#224B0C"}),
                            "and ",
                            html.Span(
                                "Knowledge ",
                                style={"color": "#224B0C"}),
                            "Report "],
                            className="display-large mt-3 mb-3 lh-1"
                        ),
                        html.Span(
                            """This is the managerial report that highlights
                                statistics related to the employee and 
                                knowledge data""",
                            className="h5 text-secondary fw-lighter",)
                    ],
                    className="col-12 col-xl-10"
                ),
                dbc.ButtonGroup(
                    [
                        dbc.Button(
                            "Employee",
                            outline=True,
                            color="light",
                            id="emp-report-btn"),
                        dbc.Button(
                            "Knowledge",
                            outline=True,
                            color="light",
                            id="know-report-btn"),
                    ],
                    className="py-vh-3"
                )
              ],
              className="row d-flex align-items-center \
                justify-content-center py-vh-1"
            )
        ],
        className="container py-vh-4 position-relative mt-5 \
            px-vw-5 text-center"
        ),
    html.Div(
        html.Div(
            html.Div(
                [
                    html.Div(
                        dbc.Row(
                            [
                                html.Div(
                                    "Click the buttons above to show the reports!",
                                    id="reports-title",
                                    className="h3 fw-bolder aos-init aos-animate"
                                ),
                                html.Div(
                                    id="reports-date",
                                    className="h4 fw-lighter text-secondary"
                                )
                            ]
                        ),
                        className="border-bottom py-vh-1"
                    ),
                    html.Div(
                        id="reports-load-page"
                    )
                ],
            ),
            className="container bg-dark px-vw-5 py-vh-4 rounded-5 shadow"
        ),
        className="position-relative py-vh-1 bg-cover bg-center rounded-5"
    ),
    html.Div(
        className="bg-black py-vh-3"
        )
    ],
    className="text-white"
    )


# callback for loading front page and button
@app.callback(
    Output("reports-load-page", "children"),
    Output("reports-title", "children"),
    Output("reports-date", "children"),
    Input("emp-report-btn", "n_clicks"),
    Input("know-report-btn", "n_clicks")
)
def report_submit(
    emp_report_btn,
    know_report_btn
):
    if ctx.triggered:
            event_id = ctx.triggered_id
            print(event_id)
    else:
        raise PreventUpdate
        
    if event_id == 'know-report-btn':
        return [knowledge_report], "Knowledge Report", "Results as of"
    elif event_id == "emp-report-btn":
        return ["No Report to Display"], "No Report", "Results as of"


# call back for loading each report page 
# Input page url
# Output to all fields