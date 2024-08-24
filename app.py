from operator import methodcaller
from flask import Flask, request, redirect, render_template, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "super_cool_super_fly"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# app.debug = True

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Show homepage."""

    # Keep a count of how many times the page is visited.
    session['count'] = session.get('count', 0)+1

    return render_template("index.html")


@app.route('/fav-color', methods=['POST'])
def fav_color():
    """Show favorite color."""

    fav_color = request.form.get('color')

    return render_template("color.html", fav_color=fav_color)


@app.route('/redirect-me')
def redirect_me():
    """Redirect user to homepage."""
    return redirect("/")
