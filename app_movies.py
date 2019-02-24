from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# from mission_to_mars import scrape
import movies_func_lib as mfn
import os

# Create an instance of Flask
app = Flask(__name__)

app.config["CACHE_TYPE"] = "null"
# change to "redis" and restart to cache again



# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/moviesdb")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # db_data = mongo.db.mars_news.find_one()

        
    # Return template and data
    return render_template("index.html")


# Route that will trigger the TMDB data page
@app.route("/TMDB_data")
def tmdb_data():

    # Run the scrape function and save the results to a variable
    htm = mfn.renderTMDBData_html()

    return render_template("TMDB-Data.htm", tmdb_htm = htm)

# Route that will trigger the TMDB data page
@app.route("/OMDB_data")
def omdb_data():

    # Run the scrape function and save the results to a variable
    htm = mfn.renderOMDBData_html()

    return render_template("OMDB-Data.htm", omdb_htm = htm)

# Route that will trigger the TMDB data page
@app.route("/COMB_data")
def comdb_data():

    # Run the scrape function and save the results to a variable
    htm = mfn.renderCombData_html()

    return render_template("COMDB-Data.htm", comdb_htm = htm)
    
# Route that will trigger the TMDB data page
@app.route("/process")
def process():

    # Run the scrape function and save the results to a variable
    #htm = mfn.renderTMDBData_html()

    return render_template("Process.html")

if __name__ == "__main__":
    app.run(debug=True)
