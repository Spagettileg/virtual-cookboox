import os
import math
import re
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo  # Flask connect to MongoDB Atlas
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
"""
MongoDB represents JSON documents in binary-encoded format called
BSON behind the scenes. BSON extends the JSON model to provide
additional data types, ordered fields, and to be efficient
for encoding and decoding within different languages.
"""

app = Flask(__name__)

"""
Environment variables SECRET and MONGO_URI set in Heroku
dashboard in production.
"""
app.secret_key = os.getenv("SECRET")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = "virtual_cookbook"
mongo = PyMongo(app)


@app.route('/')
def index():
    """
    Route decorator allows users to register to website.
    """
    return render_template('index.html')


@app.route('/portfolio')
def portfolio():
    """
    Route decorator allows users to view all the food genres held within the
    mongodb database collection. Users can then proceed to view and create
    recipes.
    """
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template('portfolio.html',
                           count_tasks=count_tasks,
                           favourite_count=favourite_count)


@app.route('/get_meat', methods=['GET'])
def meat():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("meat.html",
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Meat Recipes",
                           tasks=mongo.db.tasks.find
                           ({"category_name": "Meat"}))


@app.route('/get_poultry', methods=['GET'])
def poultry():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("poultry.html",
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Poultry Recipes",
                           tasks=mongo.db.tasks.find
                           ({"category_name": "Poultry"}))


@app.route('/get_fish', methods=['GET'])
def fish():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("fish.html",
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Fish Recipes",
                           tasks=mongo.db.tasks.find
                           ({"category_name": "Fish"}))


@app.route('/get_veg', methods=['GET'])
def veg():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("veg.html",
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Vegetable Recipes",
                           tasks=mongo.db.tasks.find
                           ({"category_name": "Vegetables"}))


@app.route('/get_grains', methods=['GET'])
def grains():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("grains.html",
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Grains Recipes",
                           tasks=mongo.db.tasks.find
                           ({"category_name": "Grains"}))


@app.route('/get_pasta', methods=['GET'])
def pasta():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("pasta.html",
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Pasta Recipes",
                           tasks=mongo.db.tasks.find
                           ({"category_name": "Pasta"}))


@app.route('/get_task/<tasks_id>', methods=['GET', 'POST'])
def task(tasks_id):
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    """
    Route for viewing a single recipe in detail.
    """
    a_recipe = mongo.db.tasks.find_one({"_id": ObjectId(tasks_id)})

    return render_template('recipe.html',
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           task=a_recipe,
                           title=a_recipe['recipe_name'])


@app.route('/get_tasks')
def get_tasks():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("tasks.html",
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_tasks():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    # Allows task categories in MongoDB to connect with addtask.html file
    return render_template('addrecipe.html',
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Add New Recipe",
                           categories=mongo.db.categories.find())


@app.route('/insert_tasks', methods=['POST'])
def insert_tasks():
    tasks = mongo.db.tasks  # This is the tasks collection
    tasks.insert_one(request.form.to_dict())
    # when submitting info to URI, its submmited in form of a request object
    return redirect(url_for('portfolio'))
    """
    We then grab the request object, show me the form & convert
    form to dict for Mongo to understand.
    """


@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    """
    Find a particular task, parameter passed is 'id', looking
    for a match to 'id' in MongoDB, then wrapped for editing
    purposes.
    """
    all_categories = mongo.db.categories.find()
    """
    Reuse much of the layout in 'add_tasks' function,
    but with pre-populated fields.
    """
    return render_template('editrecipe.html',
                           count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           page_title="Edit Recipe",
                           task=task,
                           categories=all_categories)


@app.route('/update_task/<task_id>', methods=['POST'])
def update_task(task_id):
    tasks = mongo.db.tasks  # Access to the tasks collection in mongo.db
    tasks.update({'_id': ObjectId(task_id)}, {
                'category_name': request.form.get('category_name'),
                'recipe_name': request.form.get('recipe_name'),
                'author_name': request.form.get('author_name'),
                'prep_time_mins': request.form.get('prep_time_mins'),
                'cook_time_mins': request.form.get('cook_time_mins'),
                'complexity': request.form.get('complexity'),
                'favourite': 'favourite' in request.form,
                'servings': request.form.get('servings'),
                'brief_description': request.form.get('brief_description'),
                'calories': request.form.get('calories'),
                'ingredients': request.form.get('ingredients'),
                'instructions': request.form.get('instructions'),
                'recipe_image': request.form.get('recipe_image')
                })
    return redirect(url_for('task', tasks_id=task_id))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    """
    We access the tasks collection & call to remove selected task.
    """
    return redirect(url_for('portfolio'))


@app.route('/count_tasks')
def count_tasks():
    count_tasks = mongo.db.tasks.find().count()
    return render_template("portfolio.html",
                           count_tasks=count_tasks)


@app.route('/favourite_count')
def favourite_count():
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("portfolio.html",
                           favourite_count=favourite_count)

if __name__ == "__main__":
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', "5000")),
            debug=True)
