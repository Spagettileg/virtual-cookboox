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
        
    return render_template("meat.html", page_title="Meat Recipes", tasks=mongo.db.tasks.find({"category_name": "Meat"}))

@app.route('/get_poultry', methods=['GET'])
def poultry():
        
    return render_template("poultry.html", page_title="Poultry Recipes", tasks=mongo.db.tasks.find({"category_name": "Poultry"}))
    
@app.route('/get_fish', methods=['GET'])
def fish():
    
    return render_template("fish.html", page_title="Fish Recipes", tasks=mongo.db.tasks.find({"category_name": "Fish"}))
    
@app.route('/get_veg', methods=['GET'])
def veg():
    
    return render_template("veg.html", page_title="Vegetable Recipes", tasks=mongo.db.tasks.find({"category_name": "Vegetables"}))
    
@app.route('/get_grains', methods=['GET'])
def grains():
    
    return render_template("grains.html", page_title="Grains Recipes", tasks=mongo.db.tasks.find({"category_name": "Grains"}))
    
@app.route('/get_pasta', methods=['GET'])
def pasta():
    
    return render_template("pasta.html", page_title="Pasta Recipes", tasks=mongo.db.tasks.find({"category_name": "Pasta"}))

@app.route('/get_task/<tasks_id>', methods=['GET', 'POST'])
def task(tasks_id):
    """
    Route for viewing a single recipe in detail.
    """
    a_recipe = mongo.db.tasks.find_one({"_id": ObjectId(tasks_id)})

    return render_template('recipe.html', task=a_recipe, title=a_recipe['recipe_name'])
    
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
    return redirect(url_for('index')) # We then grab the request object, show me the form & convert form to dict for Mongo to understand.

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    # Find a particular task, parameter passed is 'id', looking for a match to 'id' in MongoDB, then wrapped for editing purposes.  
    all_categories = mongo.db.categories.find() # Reuse much of the layout in 'add_tasks' function, but with pre-populated fields.
    return render_template('editrecipe.html', page_title="Edit Recipe", task=task, categories=all_categories)
    
@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    tasks = mongo.db.tasks # Access to the tasks collection in mongo.db
    tasks.update({'_id': ObjectId(task_id)},
    {
        'category_name':request.form.get('category_name'),
        'recipe_name':request.form.get('recipe_name'),
        'author_name':request.form.get('author_name'),
        'prep_time_mins':request.form.get('prep_time_mins'),
        'cook_time_mins':request.form.get('cook_time_mins'),
        'complexity':request.form.get('complexity'),
        'favourite': 'favourite' in request.form,
        'servings':request.form.get('servings'),
        'brief_description':request.form.get('brief_description'),
        'calories':request.form.get('calories'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions'),
        'recipe_image':request.form.get('recipe_image')
    })
    return redirect(url_for('task', tasks_id=task_id))
    
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)}) # We access the tasks collection & call to remove selected task. 
    return redirect(url_for('index'))
    
@app.route('/count_tasks/<task_id>')
def count_tasks(task_id):
    """Function to increment task counter"""
    mongo.db.tasks.count(
        {'_id': ObjectId(task_id)},
        {'$inc': {'count_tasks': 1}})
    return redirect(url_for('index', task_id=task_id))
    
@app.route('/count_favourite')
def count_favourite():
    return render_template("base.html", tasks=mongo.db.tasks.count({'favourite' : 'true'}))

if __name__ == "__main__":
    app.run(host=os.environ.get('IP', "0.0.0.0"),
    port=int(os.environ.get('PORT', "5000")),
    debug=True)
    