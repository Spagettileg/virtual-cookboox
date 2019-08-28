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
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks = mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
        
    return render_template("poultry.html", task=tasks, current_page=current_page, pages=pages, page_title="Poultry Recipes", tasks=mongo.db.tasks.find({"category_name": "Poultry"}))
    
@app.route('/get_fish', methods=['GET'])
def fish():
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks = mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
        
    return render_template("fish.html", task=tasks, current_page=current_page, pages=pages, page_title="Fish Recipes", tasks=mongo.db.tasks.find({"category_name": "Fish"}))
    
@app.route('/get_veg', methods=['GET'])
def veg():
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks = mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
        
    return render_template("veg.html", task=tasks, current_page=current_page, pages=pages, page_title="Vegetable Recipes", tasks=mongo.db.tasks.find({"category_name": "Vegetables"}))
    
@app.route('/get_grains', methods=['GET'])
def grains():
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks = mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
        
    return render_template("grains.html", task=tasks, current_page=current_page, pages=pages, page_title="Grains Recipes", tasks=mongo.db.tasks.find({"category_name": "Grains"}))
    
@app.route('/get_pasta', methods=['GET'])
def pasta():
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.recipe.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks = mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
        
    return render_template("pasta.html", task=tasks, current_page=current_page, pages=pages, page_title="Pasta Recipes", tasks=mongo.db.tasks.find({"category_name": "Pasta"}))

@app.route('/get_task/<tasks_id>', methods=['GET', 'POST'])
def task(tasks_id):
    """
    Route for viewing a single recipe in detail.
    """
    a_recipe = mongo.db.tasks.find_one({"_id": ObjectId(tasks_id)})

    return render_template('recipe.html', task=task, tasks=a_recipe, title=a_recipe['recipe_name'])
    
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())
    
@app.route('/add_task')
def add_tasks():
    return render_template('addrecipe.html', page_title="Add New Recipe",
    categories=mongo.db.categories.find()) # Allows task categories in MongoDB to connect with addtask.html file
    
@app.route('/insert_tasks', methods=['POST'])
def insert_tasks():
    tasks = mongo.db.tasks # This is the tasks collection 
    tasks.insert_one(request.form.to_dict()) # when submitting info to URI, its submmited in form of a request object
    return redirect(url_for('get_tasks')) # We then grab the request object, show me the form & convert form to dict for Mongo to understand.

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    tasks = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    # Find a particular task, parameter passed is 'id', looking for a match to 'id' in MongoDB, then wrapped for editing purposes.  
    all_categories = mongo.db.categories.find() # Reuse much of the layout in 'add_tasks' function, but with pre-populated fields.
    return render_template('editrecipe.html', task=tasks, categories=all_categories)
    


if __name__ == "__main__":
    app.run(host=os.environ.get('IP', "0.0.0.0"),
    port=int(os.environ.get('PORT', "5000")),
    debug=True)
    