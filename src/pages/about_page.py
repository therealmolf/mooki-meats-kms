# Import necessary libraries 
from dash import html
import dash_bootstrap_components as dbc


# Define the page layout
layout = dbc.Container([
    html.Div(
        [
            html.Div(
                [
                    html.Div(
                        html.Div(
                            [
                                html.H1(
                                    [
                                        "What is ",
                                        html.Span(
                                            "Mooki Meats",
                                            style={
                                                "color": "#224B0C"
                                                }),
                                        "?"
                                    ],
                                    className="display-1 fw-bold"
                                ),
                                html.P(
                                    [
                                        """
                                        Mooki Meats,""",
                                        html.Span(
                                            """a plant-based meat company
                                            based
                                            in the Philippines""",
                                            style={
                                                "color": "#224B0C",
                                            }
                                        ),
                                        """, is a medium-sized
                                        start-up
                                        with less than 50 million in assets
                                        exclusive of the
                                        land in which the business is situated.
                                         It
                                        is composed
                                        of less than 80 employees, with little
                                        market share.
                                        According to Republic Act No. 9178,""",
                                        """ Mooki Meats
                                        is considered a small business
                                        given the aforementioned
                                        facts. Aside from these, the
                                        organization has also recently
                                        received Series A funding from
                                        international venture
                                        capitalists to potentially
                                        increase market share,
                                        on top of having real-time
                                         scaling issues (a common problem in
                                         most
                                         alternative protein
                                        companies). Thus, the start-up is 
                                        looking to expedite sales and scale up by 
                                        improving internal systems and processes.""",
                                        html.Br(),
                                        html.Br(),
                                        """Mooki Meats is a company that 
                                        strives to reduce the effects of 
                                        factory farming (antibiotic resistance, 
                                        inefficient land and water use, 
                                        environmental problems, ethical 
                                        violations against animals,
                                         etc.) while delivering tasty
                                          alternatives to animal-based
                                           meat. The start-up
                                            primarily sells whole
                                         muscle plant-based products,
                                         produced via post-extrusion 
                                         techniques, to Filipinos from 
                                         socioeconomic classes A and B. 
                                         To create these, the start-up 
                                         was divisionally organized to 
                                         have multiple departments: : 
                                         Manufacturing, Research and 
                                         Development, Marketing and 
                                         Sales, and Finance.
                                        """,
                                        html.Br(),
                                        html.Br(),
                                        """
                                        This project focuses on the
                                        knowledge management of
                                        the manufacturing team only.
                                        There is only one manager and
                                        one database administrator for the team.
                                        Moreoverm the manufacturing team can be
                                        broken down into parts of the process.
                                        The process is the following:
                                        """
                                    ],
                                    className="lead border-top pt-5 mt-5 aos-init aos-animate"
                                ),
                                html.Br(),
                                html.Img(
                                    src=r"assets/team.png",
                                    alt="image",
                                    width="913",
                                    height="340"
                                    )
                            ],
                            className="col-12"
                        ),
                        className="row"
                    )
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
    className="container bg-black text-white"
)
