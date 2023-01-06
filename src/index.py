# Import necessary libraries
from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import home, about_page, proposal_page, approve_page, update_page

# Connect the navbar to the index
from components import navbar

# Define the navbar
nav = navbar.Navbar()

# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])


# Create the callback to handle mutlipage inputs
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout
    if pathname == '/about_page':
        return about_page.layout
    if pathname == '/proposal_page':
        return proposal_page.layout
    if pathname == '/update_page':
        return update_page.layout
    if pathname == '/approve_page':
        return approve_page.layout
    else:
        # if redirected to unknown link
        return "404 Page Error! Please choose a link"


# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)
