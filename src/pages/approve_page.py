# Import necessary libraries 
from dash import html
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
                            className='col-sm-2'
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
                        'Do you want to make these changes?'
                    ),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Yes",
                            href='/home'
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
    className="container bg-black border border-dark border-5 text-white"
)


@app.callback(
    Output("approve-table", "children")
    ,
    Input("url", "pathname"),
    Input('approve-search', 'value')
)
def moviehome_loadmovielist(pathname, approve_term):
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

        df = db_connect.query_db(sql, df_col=cols)

        if not df.empty:
            table = dbc.Table.from_dataframe(
                df,
                className="table table-secondary table-striped \
                    table-bordered table-hover fs-4",
            )
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate
