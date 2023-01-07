# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.Navbar(
            children=[
                html.A([
                    html.Span("Mooki Meats",
                              className="ms-md-1 mt-1 fw-bolder me-md-5",
                              style={
                                    "color": "#224B0C",
                              }
                              ),
                ],
                    className="navbar-brand pe-md-4 fs-4 col-12 \
                        col-md-auto text-center",
                    href="/home",
                    style={
                        "textAlign": 'left'
                    }
                        ),
                html.Ul([
                    dbc.NavItem(
                        dbc.NavLink(
                            "Approve",
                            href="/approve_page",
                            className="nav-link fs-5"),
                        className="nav-item"
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            "Update",
                            href="/update_page",
                            className="nav-link fs-5"),
                        className="nav-item"
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            "About",
                            href="/about_page",
                            className="nav-link fs-5"),
                        className="nav-item"
                    ),
                ],
                    className="navbar-nav mx-auto mb-2 mb-lg-0 \
                        list-group list-group-horizontal"
                ),
                dbc.Button(
                    "Propose Knowledge",
                    outline=True,
                    href="/proposal_page",
                    color="light",
                    className="btn btn-success fw-bolder"),
            ],
            className="navbar navbar-dark bg-black fixed-top px-vw-5",
        ),
    ])

    return layout
