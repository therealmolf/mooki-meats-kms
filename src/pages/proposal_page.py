from dash import html, dcc
from dash import Output, Input, State
import dash_bootstrap_components as dbc
from utils import db_connect
from dash.exceptions import PreventUpdate
from app import app


name_input = dbc.Row(
    [
        dbc.Label(
            "Name",
            html_for="example-email-row", 
            width=2,
            className="form-label fw-bolder"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="prop-by-input", 
                placeholder="Enter your name here",
                valid=True
            ),
            width=10,
        ),
    ],
    className="mb-4 fs-5",
)


know_type_input = dbc.Row(
    [
        dbc.Label("Type", html_for="example-email-row", width=2),
        dbc.Col(
            [dcc.Dropdown(
                [
                    "Research",
                    "Tutorial",
                    "News Article",
                    "General"
                ],
                id="know-type-dropdown",
                style={
                    "color": "black"
                },
                value=""
            ),
            html.Div(
                id="know-type-text"
            )],
            width=10,
        ),
    ],
    className="mb-5",
)


know_name_input = dbc.Row(
    [
        dbc.Label("Title", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text", 
                id="know-name-input", 
                placeholder="Enter Title",
                valid=True
            ),
            width=10,
        ),
    ],
    className="mb-5 fs-5 fw-bolder",
)


content_input = dbc.Row(
    [
        dbc.Label("Content", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Textarea(
                id="know-desc-input", 
                size="m",
                placeholder="What is it about?",
                className="textarea",
                style={"width": "100%", "height": 400}
            ),
            width=10,
        ),
    ],
    className="mb-5 flex-grow",
)


emp_know_input = dbc.Row(
    [
        dbc.Label("Tag", html_for="example-email-row", width=2),
        dbc.Col(
            dcc.Dropdown(
                multi=True,
                id="emp_know_input",
                style={
                    "color": "black"
                }
            ),
            width=10,
        ),
    ],
    className="mb-5",
)


prop_submit_btn = dbc.Row(
    [
        dbc.Button(
            "Submit Form",
            outline=True,
            color="light",
            id="prop-submit-btn",
            className="btn btn-success fs-5 fw-bolder"
        )
    ],
    className="mb-5 col-13 align-items-center border-top border-4 border-dark pt-5 mt-5",
)


# Define the page layoutage layout
layout = dbc.Container([
    html.Div(
        [
            html.Div(
                [
                    html.Br(),
                    html.H2(
                        "Knowledge Proposal Form"
                    ),
                    html.P(
                        "",
                        className="lead border-top border-success border-5 pt-5 mt-5 aos-init aos-animate"
                    ),
                    html.Form(
                        [
                            name_input,
                            html.Br(),
                            html.Br(),
                            know_type_input,
                            know_name_input,
                            content_input,
                            emp_know_input
                        ],
                    ),
                    prop_submit_btn
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
    className="container bg-black border border-dark border-5 text-white"
)


@app.callback(
    [
        Output('emp_know_input', 'options')
    ],
    [
        Input('url', 'pathname')
    ]
)
def populate_tag(pathname):
    if pathname == '/proposal_page':
        sql = """
            SELECT emp_name
            FROM emp
            WHERE
             emp_delete_ind IS NULL
            """

        df = db_connect.query_db(sql)

        return [df.values.flatten()]

    else:
        raise PreventUpdate



# @app.callback(
#     Output('know-type-text', 'children'),
#     Input('know-type-dropdown', 'value')
# )
# def update_knowtype_text(value):
#     return value