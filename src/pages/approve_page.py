# Import necessary libraries 
from dash import html, ctx
from dash import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dcc
from utils import db_connect
from app import app
from dash.exceptions import PreventUpdate


approve_search_input = dbc.Row(
    [
        dbc.Label(
            "Title",
            html_for="example-email-row",
            width=2,
            className="form-label fw-bolder"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="approve-search",
                placeholder="What are you looking for?"
            ),
            width=10,
        ),
    ],
    className="mb-4 fs-5",
)


check_row = dbc.Row(
    [
        dbc.Label(
            "Type",
            html_for="example-email-row",
            width=2,
            className="form-label"),
        dbc.Col(
            dcc.Checklist(
                            [
                                'Research',
                                'Tutorial',
                                'News Article',
                                'General'
                            ],
                            # inline=True,
                            className='col-sm-2',
                            id='approve-checklist'
                        ),
            width=10,
        ),
    ],
    className="mb-4 fs-6 row d-flex align-items-center \
                justify-content-center py-vh-1",
)



layout = dbc.Container([
    html.Div(
        [
            html.Div(
                [
                    html.Br(),
                    html.H2(
                        "Awaiting Approval"
                    ),
                    html.P(
                        "",
                        className="lead border-top border-success border-5 pt-5 mt-5 aos-init aos-animate"
                    ),
                    html.Form(
                        [
                            approve_search_input
                        ],
                    ),
                    check_row
                ],
                className="col-12 col-lg-10 col-xl-8"
            ),
            html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                "",
                                id="approve-table"
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
                        id='approve-modal-body'
                    ),
                    dbc.ModalFooter(
                        dbc.Row(
                            [
                                dbc.Button(
                                    "Yes",
                                    href='/approve_page',
                                    id='approve-modal-btn'
                                ),
                                dbc.Button(
                                    "No",
                                    href="/approve_page"
                                )
                            ]
                        )
                        
                    )
                ],
                centered=True,
                id='approve-modal',
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
    className="container bg-black border border-dark border-5 text-white\
    w-100 overflow-hidden position-relative \
    "
)


@app.callback(
    Output("approve-table", "children")
    ,
    Input("url", "pathname"),
    Input('approve-search', 'value'),
    Input('approve-checklist', 'value')
)
def load_approve_table(pathname, 
                    approve_term,
                    approve_checklist):
    if pathname == '/approve_page':
        sql = """
            SELECT 
                know_id,
                know_type,
                know_name,
                prop_date,
                prop_by
            FROM knowledge
            WHERE app_status = 'Waiting'
     
        """
        cols = [
            'ID',
            'Type',
            'Title',
            'Proposal Date',
            'Proposed By'
            ]
     
        if approve_term:
            sql += f"AND know_name ILIKE '%{approve_term}%'"
        
        if approve_checklist:
            for i, approve_type in enumerate(approve_checklist):
                if i == 0:
                    sql += f"AND know_type = '{approve_type}'"
                else:
                    sql += f"OR know_type = '{approve_type}'"

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
                                    "Approve",
                                    # outline=True,
                                    color="success",
                                    id="approve-btn"
                                    ),
                                dbc.Button(
                                    "Reject",
                                    # outline=True,
                                    color="danger",
                                    id="reject-btn"),
                                dbc.Button(
                                    "Edit",
                                    # outline=True,
                                    color="warning",
                                    id="approve-edit-btn"),
                            ],
                        )
                    )
                )

            df['Action'] = buttons
            df.drop('ID', axis=1, inplace=True)

            table = dbc.Table.from_dataframe(
                df,
                className="table table-secondary table-striped \
                    table-bordered table-hover fs-5",
            )
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate


# callback for approve, reject, edit
@app.callback(
    Output('approve-modal', 'is_open'),
    Output('approve-modal-body', 'children'),
    Input('approve-btn', 'n_clicks'),
    Input('reject-btn', 'n_clicks'),
    Input('approve-modal-btn', 'n_clicks')
)
def approval_action(
    approve_btn,
    reject_btn,
    approve_modal_btn
):
    if ctx.triggered:

        event_id = ctx.triggered_id

        if event_id == 'approve-btn' and approve_btn:
            print(event_id)
            modal_val = True
            modal_text = 'Are you sure you want to approve?'
            return [modal_val, modal_text]

        elif event_id == 'reject-btn' and reject_btn:
            print(event_id)
            modal_val = True
            modal_text = 'Are you sure you want to reject?'
            return [modal_val, modal_text]
            
        else:
            raise PreventUpdate