from dash import html, dcc, ctx
from dash import Output, Input, State
import dash_bootstrap_components as dbc
from utils import db_connect
from dash.exceptions import PreventUpdate
from app import app
from datetime import datetime
from urllib.parse import urlparse, parse_qs

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
                id="edit-propby-input",
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
                id="edit-knowtype-dropdown",
                style={
                    "color": "black"
                },
                value="",
                placeholder="What kind of knowledge is this?"
            ),
                html.Div(
                id="edit-knowtype-text"
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
                id="edit-knowname-input",
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
                id="edit-knowdesc-input",
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
                id="edit-empknow-dropdown",
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
            "Edit and Approve",
            outline=True,
            color="light",
            id="edit-submit-btn",
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
                    html.Div(
                        [
                            dcc.Store(
                                id='edit_to_load',
                                storage_type='memory',
                                data=0
                            )
                        ],
                    ),
                    html.H2(
                        "Knowledge Update Form"
                    ),
                    dbc.Alert(
                        id="edit-form-alert",
                        is_open=False),
                    html.P(
                        "",
                        className="lead border-top border-warning border-5 pt-5 mt-5 aos-init aos-animate"
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
                    html.Br(),
                    html.Div(
                dbc.Row(
                    [dbc.Label(
                        "Do you wish to reject instead?",
                        color='danger',
                        style={
                            'fontWeight': 'bold'
                        }
                    ),
                    dbc.Col(
                        dbc.Checklist(
                            id='reject-know',
                            options=[
                                {
                                    'label': "Reject",
                                    'value': 1
                                }
                            ],
                            style={
                                'fontWeight': 'bold',
                            }
                        ),
                        width=13
                    )],
                    className="mb-4 fs-5 row d-flex align-items-center \
                justify-content-center py-vh-2",
                )
            ),
                    prop_submit_btn
                ],
                className="col-12 col-lg-10 col-xl-8"
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader(
                        html.H4('Updated!')
                    ),
                    dbc.ModalBody(
                        'You just edited a piece of knowledge!'
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Proceed",
                            href='/approve_page'
                        )
                    )
                ],
                centered=True,
                id='form-edit-modal',
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
        Output('edit-empknow-dropdown', 'options')
    ],
    [
        Input('url', 'pathname')
    ]
)
def populate_edit_tag(pathname):
    if pathname == '/approve_page/know_edit_page':
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



# on submit this should also update approval
# Callback for knowledge proposal submission
@app.callback(
    Output('edit-form-alert', 'color'),
    Output('edit-form-alert', 'children'),
    Output('edit-form-alert', 'is_open'),
    Output('form-edit-modal', 'is_open'),
    Input('edit-submit-btn', 'n_clicks'),
    Input('url', 'search'),
    State('edit-propby-input', 'value'),
    State('edit-knowtype-dropdown', 'value'),
    State('edit-knowname-input', 'value'),
    State('edit-knowdesc-input', 'value'),
    State('edit-empknow-dropdown', 'value'),
    State('reject-know', 'value')
)
def submit_proposal(
    edit_submit_btn,
    search,
    edit_propby_input,
    edit_knowtype_dropdown,
    edit_knowname_input,
    edit_knowdesc_input,
    edit_empknow_dropdown,
    reject_know
):
    if ctx.triggered:
        event_id = ctx.triggered_id
        if event_id == 'edit-submit-btn' and edit_submit_btn:
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

            app_status = "Approved"

            if reject_know:
                reject_bool = True
                app_status = "Rejected"

            if not edit_propby_input:
                return new_list
            elif not edit_knowtype_dropdown:
                return new_list
            elif not edit_knowname_input:
                return new_list
            elif not edit_knowdesc_input:
                return new_list
            elif not edit_empknow_dropdown:
                return new_list
            else:
                print("All inputs work!")

                print(reject_know)


                parsed = urlparse(search)
                current_know_id = parse_qs(parsed.query)['id'][0]

                sql = f"""
                    UPDATE knowledge
                    SET
                    know_type = '{edit_knowtype_dropdown}',
                    know_name = '{edit_knowname_input}',
                    know_desc = '{edit_knowdesc_input}',
                    prop_by = '{edit_propby_input}',
                    app_status = '{app_status}',
                    know_delete_ind = '{reject_bool}'
                    WHERE
                        know_id = {current_know_id}
                    """

                print(sql)
                db_connect.modify_db(sql)
                  
                sql = f"""
                    DELETE FROM
                    emp_know
                    WHERE
                    know_id = {current_know_id}
                """

                db_connect.modify_db(sql)

                # Need to update emp know
                print(edit_empknow_dropdown)
                # For each value here
                for name in edit_empknow_dropdown:
                    sql = f"""
                        SELECT emp_id
                        FROM emp
                        WHERE
                        emp_name = '{name}'
                    """
                    emp_id = db_connect.query_db(sql).values[0][0]

                    sql = f"""
                        INSERT INTO emp_know
                        (
                            emp_id,
                            know_id
                        )
                        VALUES
                        (
                            '{emp_id}',
                            '{current_know_id}'
                        )
                    """

                    db_connect.modify_db(sql)

                    print(f"{emp_id} , {current_know_id}")

                alert_list[3] = True

                return alert_list
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate


@app.callback(
    Output('edit-propby-input', 'value'),
    Output('edit-knowtype-dropdown', 'value'),
    Output('edit-knowname-input', 'value'),
    Output('edit-knowdesc-input', 'value'),
    Output('edit-empknow-dropdown', 'value'),
    Input('url', 'search')
)
def load_edit_data(search):
    if search:
        parsed = urlparse(search)
        current_id = parse_qs(parsed.query)['id'][0]

        sql = f"""
            SELECT
                know_type,
                know_name,
                know_desc,
                prop_by
            FROM
                knowledge
            WHERE
                know_id = {current_id}
        
        """

        know_list = db_connect.query_db(sql).values.flatten()

        sql = f"""
            SELECT
                emp_id
            FROM
                emp_know
            WHERE
                know_id = {current_id}
        """

        emp_id_list = db_connect.query_db(sql).values.flatten()
        emp_name_list = []

        for emp_val in emp_id_list:
            sql = f"""
                SELECT
                    emp_name
                FROM
                    emp
                WHERE
                    emp_id = {emp_val}
            """
            emp_name_list.append(db_connect.query_db(sql)[0][0])
        
        return know_list[3], know_list[0], know_list[1], know_list[2], emp_name_list
    else:
        raise PreventUpdate
