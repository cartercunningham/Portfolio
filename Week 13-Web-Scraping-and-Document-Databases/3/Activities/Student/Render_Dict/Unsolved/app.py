# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app=Flask(__name__)

# @TODO: Create a list of dictionaries

adoption_list = [{"Name": "Jessica","Animal": "Dog"},
                         {"Name": "Mark","Animal":"Dog"},
                         {"Name": "Sam","Animal":"Toucan"}]

# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
@app.route("/")
def index():
    return render_template("index.html", list=adoption_list)


if __name__ == "__main__":
    app.run(debug=True)
