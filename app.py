"""app.py
Starts a webserver which serves server-rendered dashboards containing an embedded access token."""
from flask import Flask, render_template
from service_account import get_access_token
app = Flask(__name__)


@app.route('/')
def main():
    """Renders an HTML template with an embedded access_token for authenticating client-side AJAX calls."""
    access_token = get_access_token()

    return render_template('index.html', ACCESS_TOKEN=access_token)