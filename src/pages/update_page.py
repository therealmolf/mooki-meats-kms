# Import necessary libraries 
from dash import html, ctx
from dash import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dcc
from utils import db_connect
from app import app
from dash.exceptions import PreventUpdate


update_search_input = dbc.Row(
    [
        dbc.Label(
            "Name",
            html_for="example-email-row",
            width=2,
            className="form-label fw-bolder"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="update-search",
                placeholder="Who are you looking for?"
            ),
            width=10,
            className="py-vh-1"
        ),
    ],
    className="mb-3 col-13 fs-5",
)


up_submit_btn = dbc.Row(
    [
        dbc.Button(
            "Add Employee",
            outline=True,
            color="light",
            id="up-submit-btn",
            href='/update_page/up_edit_page?mode=add',
            className="btn fs-6 fw-bolder"
        )
    ],
    className="mb-5 col-13 align-items-center pt-2",
)


layout = dbc.Container([
    html.Div(
        [
            html.Div(
                [
                    html.Br(),
                    html.H2(
                        "Employees"
                    ),
                    html.P(
                        "",
                        className="lead border-top border-success border-5 col-13 pt-5 mt-5 aos-init aos-animate"
                    ),
                    html.Form(
                        [
                            update_search_input
                        ],
                    ),
                    up_submit_btn
                ],
                className="col-13 col-lg-10 col-xl-8"
            ),
            html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                "",
                                id="update-table"
                                )
                        ],
                        className="row d-flex align-items-center"
                    )
                ],
                className="container px-vw-5 py-vh-5"
                )
            ],
            className="bg-dark"
            ),   
            dbc.Modal(
                [
                    dbc.ModalHeader(
                        html.H4('Are you sure?')
                    ),
                    dbc.ModalBody(
                        'Do you want to make these changes?',
                        id='update-modal-body'
                    ),
                    dbc.ModalFooter(
                        dbc.Row(
                            [
                                dbc.Button(
                                    "Yes",
                                    href='/update_page',
                                    id='update-modal-btn'
                                ),
                                dbc.Button(
                                    "No",
                                    href="/update_page"
                                )
                            ]
                        )
                        
                    )
                ],
                centered=True,
                id='update-modal',
                backdrop='static',
            )
        ],
        className="row d-flex justify-content-center py-vh-5 pb-0"
    ),
    html.Div(
        [],
        className="row d-flex align-items-start justify-content-center py-vh-3 text-muted aos-init"
    )
    ],
    className="container bg-black border border-dark border-5 text-white\
    w-100 overflow-hidden position-relative \
    "
)


@app.callback(
    Output("update-table", "children"),
    Input("url", "pathname"),
    Input('update-search', 'value'),
)
def load_approve_table(pathname, update_term,):
    if pathname == '/update_page':
        sql = """
            SELECT
                emp_id,
                emp_name,
                team_name,
                role_name,
                ssn,
                degree,
                date_hired
            FROM emp
            WHERE emp_delete_ind IS NULL
     
        """
        cols = [
            'ID',
            'Name',
            'Team',
            'Role',
            'SSN',
            'Degree',
            'Date Hired'
            ]
     
        if update_term:
            sql += f"AND emp_name ILIKE '%{update_term}%'"

        df = db_connect.query_db(sql, df_col=cols)

        # Add buttons 
        if not df.empty:
            buttons = []
            for id in df['ID']:
                buttons.append(
                    html.Div(
                        dbc.ButtonGroup(
                            [
                                dbc.Button(
                                    "Add, Edit, or Remove",
                                    # outline=True,
                                    color="warning",
                                    href=f"/update_page/up_edit_page?mode=edit&id={id}",
                                    id="update-edit-btn",)
                            ],
                        )
                    )
                )

            df['Action'] = buttons
            df.drop('ID', axis=1, inplace=True)

            table = dbc.Table.from_dataframe(
                df,
                className="table table-secondary table-striped \
                    table-bordered table-hover fs-6",
            )
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate
