import dash
import logging
# import dash_bootstrap_components as dbc


app = dash.Dash(__name__,
                external_stylesheets=["/home/therealmolf/mooki_meats/src/\
                    /css/theme.css"])
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.title = 'Mooki Meats KMS'

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
