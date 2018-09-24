# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    player_dictionary = [{"dog": "barky mcbarkface",
                         "dog": "the dogfather",
                         "dog":},
    return render_template("index.html", dict=player_dictionary)


if __name__ == "__main__":
    app.run(debug=True)
