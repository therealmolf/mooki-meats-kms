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
                id="update-empname-input",
                placeholder="What is the name of the employee?",
                valid=True
            ),
            width=10,
        ),
    ],
    className="mb-4 fs-5",
)


team_input = dbc.Row(
    [
        dbc.Label("Team", html_for="example-email-row", width=2),
        dbc.Col(
            [dcc.Dropdown(
                [
                    "Hydration",
                    "Cooking",
                    "Packaging",
                    "Coating",
                    "Cooling",
                    "ESLP",
                    "TVP"
                ],
                id="update-team-dropdown",
                style={
                    "color": "black"
                },
                value="",
                placeholder="What is the team of the employee?"
            ),
                html.Div(
                id="know-type-text"
            )
            ],
            width=10,
        ),
    ],
    className="mb-5 fs-6",
)


role_input = dbc.Row(
    [
        dbc.Label("Role", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="update-role-input",
                placeholder="What is the role of the employee?",
                valid=True
            ),
            width=10,
        ),
    ],
    className="mb-5 fs-5",
)


ssn_input = dbc.Row(
    [
        dbc.Label("SSN", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="update-ssn-input",
                placeholder="What is the SSN of the employee?",
                valid=True
            ),
            width=10,
        ),
    ],
    className="mb-5 fs-5",
)


deg_input = dbc.Row(
    [
        dbc.Label("Degree", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text",
                id="update-deg-input",
                placeholder="What is the degree of the employee?",
                valid=True
            ),
            width=10,
        ),
    ],
    className="mb-5 fs-5",
)


content_input = dbc.Row(
    [
        dbc.Label("Employee Description", html_for="example-email-row", width=2),
        dbc.Col(
            dbc.Textarea(
                id="update-empdesc-input",
                size="m",
                placeholder="Who is the employee? What does he/she do?",
                className="textarea",
                style={"width": "100%", "height": 300}
            ),
            width=10,
        ),
    ],
    className="mb-5 fs-5 flex-grow",
)


# date_hired


emp_submit_btn = dbc.Row(
    [
        dbc.Button(
            "Add, Edit, or Delete Employee",
            outline=True,
            color="light",
            id="emp-submit-btn",
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
                        "Employee Form"
                    ),
                    dbc.Alert(
                        id="update-emp-alert",
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
                            team_input,
                            role_input,
                            ssn_input,
                            deg_input,
                            content_input,
                        ],
                    ),
                    dbc.Row(
                    [dbc.Label(
                        "Do you wish to remove this employee instead?",
                        color='danger',
                        style={
                            'fontWeight': 'bold'
                        }
                    ),
                    dbc.Col(
                        dbc.Checklist(
                            id='reject-emp',
                            options=[
                                {
                                    'label': "Remove",
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
                ),
                    emp_submit_btn
                ],
                className="col-12 col-lg-10 col-xl-8"
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader(
                        html.H4('Nice One')
                    ),
                    dbc.ModalBody(
                        'You just edited/added/deleted an employee.'
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Proceed",
                            href='/update_page'
                        )
                    )
                ],
                centered=True,
                id='update-emp-modal',
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


# Call back for loading the employee data


# Callback for knowledge proposal submission
@app.callback(
    Output('update-emp-alert', 'color'),
    Output('update-emp-alert', 'children'),
    Output('update-emp-alert', 'is_open'),
    Output('update-emp-modal', 'is_open'),
    Input('emp-submit-btn', 'n_clicks'),
    State('update-empname-input', 'value'),
    State('update-team-dropdown', 'value'),
    State('update-role-input', 'value'),
    State('update-ssn-input', 'value'),
    State('update-deg-input', 'value'),
    State('update-empdesc-input', 'value'),
    State('url', 'search'),
    State('reject-emp', 'value')
)
def submit_proposal(
    emp_submit_btn,
    update_empname_input,
    update_team_dropdown,
    update_role_input,
    update_ssn_input,
    update_deg_input,
    update_empdesc_input,
    search,
    reject_emp
):
    if ctx.triggered:
        event_id = ctx.triggered_id
        if event_id == 'emp-submit-btn' and emp_submit_btn:
            print(event_id)

            # initial alert list for color, text, alert, modal
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

            if reject_emp:
                reject_bool = True

            if not update_empname_input:
                return new_list
            elif not update_team_dropdown:
                return new_list
            elif not update_role_input:
                return new_list
            elif not update_ssn_input:
                return new_list
            elif not update_deg_input:
                return new_list
            elif not update_empdesc_input:
                return new_list
            else:
                print("All inputs work!")

                parsed = urlparse(search)
                mode = parse_qs(parsed.query)['mode'][0]
                print(mode)

                date_hired = datetime.now()

                if mode == 'add':
                    sql = f"""
                        INSERT INTO emp
                        (
                            emp_name,
                            team_name,
                            role_name,
                            ssn,
                            degree,
                            emp_desc,
                            date_hired
                        )
                        VALUES
                        (
                            '{update_empname_input}',
                            '{update_team_dropdown}',
                            '{update_role_input}',
                            '{update_ssn_input}',
                            '{update_deg_input}',
                            '{update_empdesc_input}',
                            '{date_hired}'
                            )"""

                    print(sql)
                    db_connect.modify_db(sql)

                    alert_list[3] = True
                    return alert_list
                
                elif mode == 'edit':
                    parsed = urlparse(search)
                    current_id = parse_qs(parsed.query)['id'][0]

                    sql = f"""
                        UPDATE emp
                        SET
                            emp_name = '{update_empname_input}',
                            team_name = '{update_team_dropdown}',
                            role_name = '{update_role_input}',
                            ssn = '{update_ssn_input}',
                            degree = '{update_deg_input}',
                            emp_desc = '{update_empdesc_input}',
                            emp_delete_ind = '{reject_bool}'
                        WHERE
                        emp_id = {current_id}

                    """

                    db_connect.modify_db(sql)

                    alert_list[3] = True
                    return alert_list
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate



@app.callback(
    Output('update-empname-input', 'value'),
    Output('update-team-dropdown', 'value'),
    Output('update-role-input', 'value'),
    Output('update-ssn-input', 'value'),
    Output('update-deg-input', 'value'),
    Output('update-empdesc-input', 'value'),
    Input('url', 'pathname'),
    State('url', 'search')
)
def load_edit_data(
    pathname,
    search):

    if pathname == '/update_page/up_edit_page':
        parsed = urlparse(search)
        mode = parse_qs(parsed.query)['mode'][0]

    if pathname == '/update_page/up_edit_page' and mode == 'edit':
        parsed = urlparse(search)
        current_id = parse_qs(parsed.query)['id'][0]

        sql = f"""
            SELECT
                emp_name,
                team_name,
                role_name,
                ssn,
                degree,
                emp_desc
            FROM
                emp
            WHERE
                emp_id = {current_id}
        
        """

        emp_list = db_connect.query_db(sql).values.flatten()
        print(emp_list)
        
        return emp_list[0], emp_list[1], emp_list[2], emp_list[3], emp_list[4], emp_list[5]
    else:
        raise PreventUpdate