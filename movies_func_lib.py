# This is a utilities file that will render data to flask app file

# Import dependencies
import pandas as pd 
from pymongo import MongoClient

import os


#Initialize Mongodb connection
conn = "mongodb://localhost:27017/"

#establish connection
client = MongoClient(conn)

#connect to DB and collections
db = client.moviesdb

# connect to the collections
omdb_coll = db.omdb_api
tmdb_coll = db.tmdb_data
comb_coll = db.all_movies_data

# function to render the TMDB data as dataframe
def renderTMDBData():
    tmdb_df = []
    for doc in tmdb_coll.find():
        tmdb_df.append(doc)
    
    # add it to data frame
    tmdb_df = pd.DataFrame(tmdb_df)
    
    return tmdb_df

# function to render the TMDB data as dataframe
def renderTMDBData_html():
    tmdb_df = []
    for doc in tmdb_coll.find():
        tmdb_df.append(doc)
    
    # add it to data frame
    tmdb_df = pd.DataFrame(tmdb_df)
    
    #convert dataframe to HTML
    tmdb_htm = tmdb_df.to_html(classes = ['table table-striped table-hover'])
    return tmdb_htm

# function to render the TMDB data as dataframe
def renderOMDBData():
    omdb_df = []
    for doc in omdb_coll.find():
        omdb_df.append(doc)
    
    # add it to data frame
    omdb_df = pd.DataFrame(omdb_df)
    
    return omdb_df

# function to render the TMDB data as dataframe
def renderOMDBData_html():
    omdb_df = []
    for doc in omdb_coll.find():
        omdb_df.append(doc)
    
    # add it to data frame
    omdb_df = pd.DataFrame(omdb_df)
    
    #convert dataframe to HTML
    omdb_htm = omdb_df.to_html(classes = ['table table-striped table-hover'])
    return omdb_htm

# function to render the TMDB data as dataframe
def renderCombData():
    comb_df = []
    for doc in comb_coll.find():
        comb_df.append(doc)
    
    # add it to data frame
    comb_df = pd.DataFrame(comb_df)
    
    return comb_df

# function to render the TMDB data as dataframe
def renderCombData_html():
    comb_df = []
    for doc in comb_coll.find():
        comb_df.append(doc)
    
    # add it to data frame
    comb_df = pd.DataFrame(comb_df)
    
    #convert dataframe to HTML
    comdb_htm = comb_df.to_html(classes = ['table table-striped table-hover'])
    return comdb_htm