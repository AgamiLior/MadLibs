from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


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
    
    story1 = Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

    story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """I just love to go to {place}, there is a lot of {adjective} {noun}.
    I am interested in {verb} {plural_noun}."""
    )

    if option == 'Story1':
        text = story1.generate({
            'place': place, 
            'noun': noun, 
            'verb': verb, 
            'adjective': adjective, 
            'plural_noun': plural_noun
        })
    else:
        text = story2.generate({
            'place': place, 
            'noun': noun, 
            'verb': verb, 
            'adjective': adjective, 
            'plural_noun': plural_noun
        })
    

    return render_template("form.html", story = text)

