from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "something"
debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/form")
def form():
    option = request.args.get("stories")
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    return render_template("form.html",place=place, noun = noun, verb = verb, adjective = adjective, plural_noun = plural_noun, option = option)

