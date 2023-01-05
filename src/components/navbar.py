# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Approve", href="/page1")),
                dbc.NavItem(dbc.NavLink("Update", href="/page2")),
                dbc.NavItem(dbc.NavLink("About", href="/page1")),
                dbc.NavItem(dbc.NavLink("Propose Knowledge", href="/page1")),
            ] ,
            brand="Logo Here",
            brand_href="/page1",
            color="dark",
            dark=True,
        ), 
    ])

    return layout