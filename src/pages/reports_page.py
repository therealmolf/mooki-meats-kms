# Import necessary libraries
from dash import html, ctx
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import Input, Output
from utils import db_connect
from app import app

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
                html.Div(
                    [
                        html.Br(),
                        dbc.Col(
                            dbc.Input(
                                id="search-input",
                                placeholder="Type something...", 
                                type="text",
                                valid=True,
                            ),
                            width=30
                        ),
                        html.P(id="output"),
                    ],
                    className="col-12 col-xl-13"
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
                )
              ],
              className="row d-flex align-items-center \
                justify-content-center py-vh-1"
            )
        ],
        className="container py-vh-4 position-relative mt-5 \
            px-vw-5 text-center"
    )],
    className="text-white"
    )
