from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)
print(app)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)




@app.route("/")
def index():
    mars_db = mongo.db.listings.find_one()
    return render_template('index.html', mars_db=mars_db)



@app.route("/scrape")
def scrape():
   
    return render_template('scrape.html', mars_db=mars_db)


if __name__ == "__main__":
    app.run()
