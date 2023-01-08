from dash import html, dcc, ctx
from dash import Output, Input, State
import dash_bootstrap_components as dbc
from utils import db_connect
from dash.exceptions import PreventUpdate
from app import app
from datetime import datetime

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
                placeholder="What is your name?",
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
                value="",
                placeholder="What kind of knowledge is this?"
            ),
                html.Div(
                id="know-type-text"
            )
            ],
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
                placeholder="What is the title?",
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
                id="emp-know-dropdown",
                style={
                    "color": "black"
                },
                placeholder="Who is associated with this knowledge?"
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
                    dbc.Alert(
                        id="form-alert",
                        is_open=False),
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
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader(
                        html.H4('Nice One')
                    ),
                    dbc.ModalBody(
                        'You just submitted a knowledge proposal. Time to wait for approval!'
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Proceed",
                            href='/home'
                        )
                    )
                ],
                centered=True,
                id='form-proposal-modal',
                backdrop='static'
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
        Output('emp-know-dropdown', 'options')
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


# Callback for knowledge proposal submission
@app.callback(
    Output('form-alert', 'color'),
    Output('form-alert', 'children'),
    Output('form-alert', 'is_open'),
    Output('form-proposal-modal', 'is_open'),
    Input('prop-submit-btn', 'n_clicks'),
    State('prop-by-input', 'value'),
    State('know-type-dropdown', 'value'),
    State('know-name-input', 'value'),
    State('know-desc-input', 'value'),
    State('emp-know-dropdown', 'value')
)
def submit_proposal(
    prop_submit_btn,
    prop_by_input,
    know_type_dropdown,
    know_name_input,
    know_desc_input,
    emp_know_dropdown
):
    if ctx.triggered:
        event_id = ctx.triggered_id
        if event_id == 'prop-submit-btn' and prop_submit_btn:
            print(event_id)

            # initial alert list for open, color, text, modal
            alert_list = [
                '',
                '',
                False,
                False
                ]

            # if missing input, this should be returned
            new_list = [
                'danger',
                'Check your inputs.',
                True,
                False
            ]

            if not prop_by_input:
                return new_list
            elif not know_type_dropdown:
                return new_list
            elif not know_name_input:
                return new_list
            elif not know_desc_input:
                return new_list
            elif not emp_know_dropdown:
                return new_list
            else:
                print("All inputs work!")

                prop_date = datetime.now()

                sql = f"""
                    INSERT INTO knowledge
                    (
                        know_type,
                        know_name,
                        know_desc,
                        prop_date,
                        prop_by,
                        app_status
                    )
                    VALUES
                    (
                        '{know_type_dropdown}',
                        '{know_name_input}',
                        '{know_desc_input}',
                        '{prop_date}',
                        '{prop_by_input}',
                        'Waiting'
                        )"""

                print(sql)
                db_connect.modify_db(sql)

                # Need to update emp know
                print(emp_know_dropdown)
                # For each value here
                for name in emp_know_dropdown:
                    sql = f"""
                        SELECT emp_id
                        FROM emp
                        WHERE
                        emp_name = '{name}'
                    """
                    emp_id = db_connect.query_db(sql).values[0][0]

                    sql = f"""
                        SELECT know_id
                        FROM knowledge
                        WHERE
                        know_name = '{know_name_input}'
                    """

                    know_id = db_connect.query_db(sql).values[0][0]

                    sql = f"""
                        INSERT INTO emp_know
                        (
                            emp_id,
                            know_id
                        )
                        VALUES
                        (
                            '{emp_id}',
                            '{know_id}'
                        )
                    """

                    db_connect.modify_db(sql)

                    print(f"{emp_id} , {know_id}")

                alert_list[3] = True

                return alert_list
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate
