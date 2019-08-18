import os
import math
import re
import json
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo # enables Flask to connect to MongoDB Atlas
from bson.objectid import ObjectId 
from werkzeug.utils import secure_filename

"""
MongoDB represents JSON documents in binary-encoded format called BSON behind the scenes.
BSON extends the JSON model to provide additional data types, ordered fields, and to be
efficient for encoding and decoding within different languages.
"""

app = Flask(__name__)

# Environment variables SECRET and MONGO_URI set in Heroku dashboard in production

app.secret_key = os.getenv("SECRET")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = "virtual_cookbook"            

mongo = PyMongo(app)

@app.route('/')
def index():
    """
    Route decorator allows users to view all the food genres held within the
    mongodb database collection. Users can then proceed to view and create
    recipes.
    """
    return render_template('index.html')

@app.route('/get_meat', methods=['GET'])
def meat():
    return render_template("meat.html", page_title="Meat Recipes", tasks=mongo.db.tasks.find({"_id": "Meat"}))

@app.route('/get_poultry', methods=['GET'])
def poultry():
    return render_template("poultry.html", page_title="Poultry Recipes", tasks=mongo.db.tasks.find({"_id": "Poultry"}))
    
@app.route('/get_fish', methods=['GET'])
def fish():
    return render_template("fish.html", page_title="Fish Recipes", tasks=mongo.db.tasks.find({"_id": "Fish"}))
    
@app.route('/get_veg', methods=['GET'])
def veg():
    return render_template("veg.html", page_title="Vegetable Recipes", tasks=mongo.db.tasks.find({"_id": "Vegetables"}))
    
@app.route('/get_grains', methods=['GET'])
def grains():
    return render_template("grains.html", page_title="Grains Recipes", tasks=mongo.db.tasks.find({"_id": "Grains"}))
    
@app.route('/get_pasta', methods=['GET'])
def pasta():
    return render_template("pasta.html", page_title="Pasta Recipes", tasks=mongo.db.tasks.find({"_id": "Pasta"}))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP', "0.0.0.0"),
    port=int(os.environ.get('PORT', "5000")),
    debug=True)
    