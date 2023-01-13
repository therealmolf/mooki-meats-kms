# Import necessary libraries
from dash import html, ctx, dcc
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import Input, Output
from utils import db_connect
from app import app
from datetime import datetime
import plotly.graph_objs as go
from wordcloud import WordCloud
from io import BytesIO
import base64

knowledge_report = html.Div(
    [
        html.H4(
            "Types of Information",
            className="border-bottom fw-bolder py-vh-1",
        ),
        # VALUE FORMAT
        # --------------------------------------------
        html.Div(
            [
                html.Div(
                    [
                        html.Span(
                            "The numbers",
                            className="h5 text-secondary fw-lighter"
                            ),
                        html.Div(
                            id="gen-knowtype-value",
                            className="display-huge fw-bolder aos-init aos-animate"
                            ),
                        html.P(
                            "Number of General Information",
                            className="h4 fw-lighter text-secondary"
                            )
                    ],
                    className="col-5 offset-1"
                ),
                html.Div(
                    [
                        html.Div(
                            id="tut-knowtype-value",
                            className="display-huge fw-bolder aos-init aos-animate"
                            ),
                        html.P(
                            "Number of Tutorials",
                            className="h4 fw-lighter text-secondary"
                            )
                    ],
                    className="col-5 offset-1"
                ),
                html.Div(
                    [
                        html.Div(
                            id="news-knowtype-value",
                            className="display-huge fw-bolder aos-init aos-animate"
                            ),
                        html.P(
                            "Number of News Articles",
                            className="h4 fw-lighter text-secondary"
                            )
                    ],
                    className="col-5 offset-1"
                ),
                html.Div(
                    [
                        html.Div(
                            id="res-knowtype-value",
                            className="display-huge fw-bolder aos-init aos-animate"
                            ),
                        html.P(
                            "Number of Research Articles",
                            className="h4 fw-lighter text-secondary"
                            )
                    ],
                    className="col-5 offset-1"
                )
            ],
            className="row align-items-center"
        ),
        # --------------------------------------------

        # TABLE FORMAT
        # --------------------------------------------
        html.H4(
            "Proposal Frequency",
            className="border-bottom fw-bolder py-vh-1"
        ),
        html.Br(),
        html.Div(
            [
            html.Br(),
            html.Div(
                id="prop-freq-value",
                className="col-12 col-lg-10 col-xl-8 text-center my-5 py-vh-1"
                )
            ],
            style={
                "background-color": "#224B0C",
                },
            className="row d-flex align-items-center justify-content-center shadow rounded-5"
           ),
        # ----------------------------------------------
        
        html.H4(
            "Shared Knowledge",
            className="border-bottom fw-bolder py-vh-1"
        ),

        # VALUE FORMAT
        # --------------------------------------------
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            id="most-know-value",
                            className="h3 fw-bolder aos-init aos-animate"
                            ),
                        html.P(
                            "Knowledge that Most Employees Know About",
                            className="h4 fw-lighter text-secondary"
                            )
                    ],
                    className="col-5 offset-1"
                ),
                html.Div(
                    [
                        html.Div(
                            id="least-know-value",
                            className="h3 fw-bolder aos-init aos-animate"
                            ),
                        html.P(
                            "Knowledge that Least Employees Know About",
                            className="h4 fw-lighter text-secondary"
                            )
                    ],
                    className="col-5 offset-1"
                ),
            ],
            className="row align-items-center"
        ),
        # --------------------------------------------

        # TABLE FORMAT
        # --------------------------------------------
        html.H4(
            "Word Cloud",
            className="border-bottom fw-bolder py-vh-1"
        ),
        html.Br(),
        html.Div(
            [
            html.Br(),
            html.Div(
                id="word-cloud-value",
                className="col-12 col-lg-10 col-xl-8 text-center my-5 py-vh-1"
                )
            ],
            style={
                "background-color": "#224B0C",
                },
            className="row d-flex align-items-center justify-content-center shadow rounded-5"
           ),
        # ----------------------------------------------

    ],
    className="col align-items-center justify-content-center"
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
                className="row d-flex align-items-center"
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
    [   Output("reports-load-page", "children"),
        Output("reports-title", "children"),
        Output("reports-date", "children")
    ],
    [
        Input("emp-report-btn", "n_clicks"),
        Input("know-report-btn", "n_clicks")
    ]
)
def report_submit(
    emp_report_btn,
    know_report_btn
):
    if ctx.triggered:
        event_id = ctx.triggered_id
        date = datetime.now()
        date_text = f"Results as of: {date}"
        print(event_id)
    else:
        raise PreventUpdate
   
    if event_id == 'know-report-btn':
        output = [
            [knowledge_report],
            "Knowledge Report",
            date_text
        ]
        return output

    elif event_id == "emp-report-btn":
        output = [
            ["No Report to Display yet"],
            "Employee Report",
            date_text
        ]
        return output


# call back for loading each report page
@app.callback(
    [
        Output("gen-knowtype-value", "children"),
        Output("tut-knowtype-value", "children"),
        Output("news-knowtype-value", "children"),
        Output("res-knowtype-value", "children"),
        Output("most-know-value", "children"),
        Output("least-know-value", "children"),
        Output("prop-freq-value", "children"),
        Output("word-cloud-value", "children")
    ],
    [
        Input("url", "pathname")
    ]
)
def load_reports(
    pathname
):
    if pathname == '/reports_page':

        # append type report section
        output_list = []
        for type_name in ['General', 'Tutorial', 'News Article', 'Research']:
            sql = f"""
            SELECT
                COUNT(*)
            FROM
                knowledge
            WHERE
                know_type = '{type_name}'
            AND
                know_delete_ind IS NULL

            """

            curr_num = db_connect.query_db(sql)[0][0]
            output_list.append(curr_num)
        
        # append shared know section
        sql = """

            SELECT t.know_id, k.know_name, t.ce
            FROM
                (SELECT
                    know_id,
                    COUNT(emp_id) as ce
                FROM
                    emp_know
                GROUP BY
                    know_id
                ORDER BY
                    ce) t
            INNER JOIN
                knowledge k
            on
                k.know_id = t.know_id
            WHERE
                know_delete_ind IS NULL
        """

        col = ['know_id', 'know_name', 'emp_count']
        df = db_connect.query_db(sql, df_col=col)

        # most and least know
        output_list.append(df.iloc[-1, 1])
        output_list.append(df.iloc[0, 1])

        # append proposal frequency
        sql = """
            SELECT
                EXTRACT (YEAR FROM prop_date) AS Y,
                EXTRACT (QUARTER FROM prop_date) AS D,
                COUNT(know_id)
            FROM
                knowledge
            GROUP BY
                Y,
                D
            ORDER BY
                Y,
                D

        """
        col = ['Year', 'Quarter', 'Count']
        df = db_connect.query_db(sql, df_col=col)
        fig = go.Figure(
            data=[go.Scatter(x=df['Year'], y=df['Count'])],
            layout={
                "title": "Visualization of the Total Yearly Proposals"
            }
            )

        output_list.append(dcc.Graph(figure=fig))

        # append word cloud
        sql = """
            SELECT know_desc
            FROM
                knowledge
            WHERE
                know_delete_ind IS NULL
        """
        col = ['know_desc']
        df = db_connect.query_db(sql, df_col=col).values.flatten()
        text = ''.join(df)

        buf = BytesIO()
        WordCloud(
            height=500,
            width=500
        ).generate(text).to_image().save(buf, 
            format='png',
            )

        img = html.Img(
            src='data:image/png;base64,{}'.format(base64.b64encode(buf.getvalue()).decode())
        )

        output_list.append(img)

        return output_list

# Input page url
# Output to all fields