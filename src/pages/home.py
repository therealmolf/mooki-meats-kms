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
        className="position-absolute w-100 h-100 \
            bg-black opacity-75 top-0 start-0"
    ),
    html.Div(
        [
            html.Div(
              [
                html.Div(
                    [
                        html.H1([
                            "What do you ",
                            html.Span(
                                "need",
                                style={"color": "#224B0C"}),
                            "?"],
                            className="display-huge mt-3 mb-3 lh-1"
                        ),
                        html.Span(
                            "This is a full text search engine that gives you the team, employee,\
                                and knowledge that are related to each other. Give it a try!",
                            className="h5 text-secondary fw-lighter",)
                    ],
                    className="col-12 col-xl-10"
                ),
                html.Div(
                    [
                        html.Br(),
                        dbc.Input(
                            id="search-input",
                            placeholder="Type something...", type="text"),
                        html.P(id="output"),
                    ],
                    className="col-12 col-xl-8"
                ),
                dbc.ButtonGroup(
                    [
                        dbc.Button(
                            "Team",
                            outline=True,
                            color="light",
                            id="team-search-btn"
                            ),
                        dbc.Button(
                            "Employee",
                            outline=True,
                            color="light",
                            id="emp-search-btn"),
                        dbc.Button(
                            "Knowledge",
                            outline=True,
                            color="light",
                            id="know-search-btn"),
                    ],
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
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H5("Search Results:"),
                            html.Div(
                                "",
                                id="search-table"
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
    html.Div(
        className="bg-black py-vh-4"
    )
],
    className="w-100 overflow-hidden position-relative \
        bg-black text-white aos-init aos-animate"
)


# Callback for Team Button
# TODO: Refactor
@app.callback(
    [
        Output('search-table', "children"),
    ],
    [
        Input("team-search-btn", 'n_clicks'),
        Input("emp-search-btn", "n_clicks"),
        Input("know-search-btn", "n_clicks"),
        Input("search-input", "value")
    ]
)
def btn_search(
    team_search_btn,
    emp_search_btn,
    know_search_btn,
    search_input
):
    if ctx.triggered:
        event_id = ctx.triggered_id
        # print(event_id)
    else:
        raise PreventUpdate
    
    if event_id == 'search-input' and search_input:
        sql = f"""
            SELECT
                emp.emp_name,
                emp.team_name,
                knowledge.know_name
            FROM
            emp
            INNER JOIN team
            ON team.team_name = emp.team_name
            INNER JOIN emp_know
            ON emp.emp_id = emp_know.emp_id
            INNER JOIN knowledge
            ON knowledge.know_id = emp_know.know_id
            WHERE to_tsvector(
                'english',
                concat_ws(
                    ' ',
                    know_desc,
                    team_desc,
                    emp_desc,
                    emp_name,
                    emp.team_name,
                    degree,
                    date_hired,
                    know_name
                    )) @@ 
            plainto_tsquery('{search_input}');
            """
        cols = [
            "Employee",
            "Team",
            "Knowledge"
        ]

        df = db_connect.query_db(sql, df_col=cols)

        if not df.empty:
            table = dbc.Table.from_dataframe(
                df,
                bordered=True,
                dark=True,
                hover=True,
                responsive=True,
                striped=True,
                className="table table-primary",
            )
            return [table]
        else:
            return ["No records to display"]

    if event_id == 'team-search-btn' and team_search_btn:
        sql = """
            SELECT * FROM team
        """
        cols = ["Team", "Team Description"]

        df = db_connect.query_db(sql, df_col=cols)

        if not df.empty:
            table = dbc.Table.from_dataframe(
                df,
                bordered=True,
                dark=True,
                hover=True,
                responsive=True,
                striped=True,
                className="table table-primary",
            )
            return [table]
        else:
            return ["No records to display"]

    if event_id == 'emp-search-btn' and emp_search_btn:
        sql = """
            SELECT * FROM emp
        """
        cols = [
            "ID",
            "Employee",
            "Team",
            "Role",
            "SSN",
            "Course",
            "Description",
            "Date Hired",
            "Delete Ind"
            ]

        df = db_connect.query_db(sql, df_col=cols)

        if not df.empty:
            table = dbc.Table.from_dataframe(
                df,
                bordered=True,
                dark=True,
                hover=True,
                responsive=True,
                striped=True,
            )
            return [table]
        else:
            return ["No records to display"]

    if event_id == 'know-search-btn' and know_search_btn:
        sql = """
            SELECT * FROM knowledge
        """
        cols = [
            "Knowledge ID",
            "Type",
            "Title",
            "Content",
            "Proposal Date",
            "Proposed By",
            "Approval Status",
            "Delete Ind"
        ]
        df = db_connect.query_db(sql, df_col=cols)

        if not df.empty:
            table = dbc.Table.from_dataframe(
                df,
                bordered=True,
                dark=True,
                hover=True,
                responsive=True,
                striped=True,
            )
            return [table]
        else:
            return ["No records to display"]
    else:
        raise PreventUpdate


# # Callback for Search
# @app.callback(
#     Output("search-table", "children"),
#     Input("search-input", "value")
# )
# def full_text_search(search_input):
#     return f"This is the input: {search_input}"