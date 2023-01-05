# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.Navbar(
            children=[
                html.A([
                    html.Span("Mooki",
                              className="ms-md-1 mt-1 fw-bolder me-md-5",
                              style={
                                    "color": "green",
                              }
                              ),
                ],
                    className="navbar-brand pe-md-4 fs-4 col-12 col-md-auto text-center",
                    href="/page1",
                    style={
                        "textAlign": 'left'
                    }
                        ),
                html.Ul([
                    dbc.NavItem(
                        dbc.NavLink(
                            "Approve", 
                            href="/page1",
                            className="nav-link fs-5"),
                        className="nav-item"
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            "Update", 
                            href="/page2",
                            className="nav-link fs-5"),
                        className="nav-item"
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            "About", 
                            href="/page1",
                            className="nav-link fs-5"),
                        className="nav-item"
                    ),
                ],
                    className="navbar-nav mx-auto mb-2 mb-lg-0 list-group list-group-horizontal"
                ),
                dbc.Button(
                    "Propose Knowledge",
                    outline=True,
                    href="/page2",
                    color="light",
                    className="me-1"),
            ],
            className="navbar navbar-dark bg-black fixed-top px-vw-5",
        ), 
    ])

    return layout