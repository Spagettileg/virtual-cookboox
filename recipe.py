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
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks = mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
        
    return render_template("meat.html", task=tasks, current_page=current_page, pages=pages, page_title="Meat Recipes", tasks=mongo.db.tasks.find({"category_name": "Meat"}))

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

@app.route('/get_task/<tasks_id>', methods=['GET', 'POST'])
def task(tasks_id):
    """
    Route for viewing a single recipe in detail.
    """
    a_recipe = mongo.db.tasks.find_one({"_id": ObjectId(tasks_id)})

    return render_template('recipe.html', task=task, tasks=a_recipe, title=a_recipe['recipe_name'], page_title="Recipe Detail")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP', "0.0.0.0"),
    port=int(os.environ.get('PORT', "5000")),
    debug=True)
    