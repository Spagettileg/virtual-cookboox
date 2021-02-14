import os
import math
from flask_pymongo import PyMongo, pymongo  # Flask connect to MongoDB Atlas
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import (Flask, render_template, redirect, request, url_for, flash,
                   session)
from forms import LoginForm, RegistrationForm, RecipeForm

"""
MongoDB represents JSON documents in binary-encoded format called
BSON behind the scenes. BSON extends the JSON model to provide
additional data types, ordered fields, and to be efficient
for encoding and decoding within different languages.
"""

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

"""
Environment variables SECRET and MONGO_URI set in Heroku
dashboard in production.
"""
app.config['SECRET_KEY'] = os.getenv("SECRET")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = "virtual_cookbook"
mongo = PyMongo(app)


@app.route('/')
def index():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    """
    Route allows users to view all the recipes within the database
    collection. Logged in users can view own profile, create, edit
    & delete recipes.
    """
    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('index.html', count_tasks=count_tasks,
                               favourite_count=favourite_count, tasks=task,
                               title='Home', current_user=current_user)
    else:
        return render_template('index.html', count_tasks=count_tasks,
                               favourite_count=favourite_count, tasks=task,
                               title='Home')


@app.route('/get_meat', methods=['GET'])
def meat():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('meat.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title='Meat Recipes',
                               current_user=current_user,
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Meat"}))
    else:
        return render_template('meat.html',
                               count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title="Meat Recipes",
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Meat"}))


@app.route('/get_poultry', methods=['GET'])
def poultry():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('poultry.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title='Poultry Recipes',
                               current_user=current_user,
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Poultry"}))
    else:
        return render_template("poultry.html", count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title="Poultry Recipes",
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Poultry"}))


@app.route('/get_fish', methods=['GET'])
def fish():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('fish.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title='Fish Recipes',
                               current_user=current_user,
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Fish"}))
    else:
        return render_template("fish.html", count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title="Fish Recipes",
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Fish"}))


@app.route('/get_veg', methods=['GET'])
def veg():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('veg.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title='Vegetable Recipes',
                               current_user=current_user,
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Vegetables"}))
    else:
        return render_template("veg.html", count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title="Vegetable Recipes",
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Vegetables"}))


@app.route('/get_grains', methods=['GET'])
def grains():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('grains.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title='Grains Recipes',
                               current_user=current_user,
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Grains"}))
    else:
        return render_template('grains.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title="Grains Recipes",
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Grains"}))


@app.route('/get_pasta', methods=['GET'])
def pasta():
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
        return render_template('pasta.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title='Pasta Recipes',
                               current_user=current_user,
                               tasks=mongo.db.tasks.find
                               ({"category_name": "Pasta"}))
    else:
        return render_template("pasta.html", count_tasks=count_tasks,
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
    a_recipe = mongo.db.tasks.find_one_or_404({"_id": ObjectId(tasks_id)})

    if 'logged_in' in session:
        current_user = mongo.db.user.find_one({
            'name': session['username'].title()})
        return render_template('recipe.html',
                               count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               task=a_recipe, current_user=current_user,
                               title=a_recipe['recipe_name'])
    else:
        return render_template('recipe.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               task=a_recipe, title=a_recipe['recipe_name'])


@app.route('/add_task', methods=['GET', 'POST'])
def add_tasks():
    """
    Add a new recipe to mongodb database collection
    """
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    # Allows task categories in MongoDB to connect with addtask.html file
    if 'logged_in' not in session:  # Check for user logged in
        flash('Apologies, only logged in users can add recipes.')
        return redirect(url_for('index'))

    form = RecipeForm(request.form)  # Initialise the form
    user = mongo.db.user.find_one({"name": session['username'].title()})
    if 'logged_in' in session:
        form = RecipeForm(request.form)
        current_user = mongo.db.user.find_one({'name': session[
            'username'].title()})
    else:
        return render_template('addrecipe.html', count_tasks=count_tasks,
                               favourite_count=favourite_count,
                               page_title='Add New Recipe', form=form,
                               current_user=current_user)
    if form.validate_on_submit():  # Insert new recipe if form is submitted
        tasks = mongo.db.tasks
        tasks.insert_one({
            'category_name': request.form['category_name'],
            'complexity': request.form['complexity'],
            'recipe_name': request.form['recipe_name'],
            'author_name': request.form['author_name'],
            'prep_time_mins': int(request.form['prep_time_mins']),
            'cook_time_mins': int(request.form['cook_time_mins']),
            'calories': int(request.form['calories']),
            'servings': int(request.form['servings']),
            'brief_description': request.form['brief_description'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'recipe_image': request.form['recipe_image'],
            'favourite': 'favourite' in request.form,
            'username': session['username'].title(),
            'created_by': {
                '_id': user['_id'],
                'name': user['name']}})
        return redirect(url_for('index'))
    return render_template('addrecipe.html', count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           current_user=current_user,
                           form=form, title="Add New Recipe")


@app.route('/edit_task/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' not in session:  # Check if its a logged in user
        flash('Apologies, only logged in users can edit recipes.')
        return redirect(url_for('index'))

    user = mongo.db.user.find_one({"name": session['username'].title()})
    task = mongo.db.tasks.find_one_or_404({"_id": ObjectId(task_id)})
    form = RecipeForm()
    """
    Find a particular task, parameter passed is 'id', looking
    for a match to 'id' in MongoDB, then wrapped for editing
    purposes.
    Reuse much of the layout in 'add_tasks' function,
    but with pre-populated fields.
    """
    if user['name'].title() == task['username'].title():
        if request.method == 'GET':
            form = RecipeForm(data=task)
            current_user = mongo.db.user.find_one({'name': session[
                'username'].title()})
            return render_template('editrecipe.html', task=task,
                                   current_user=current_user,
                                   count_tasks=count_tasks,
                                   favourite_count=favourite_count,
                                   form=form, title="Edit Recipe")
        if form.validate_on_submit():
            tasks = mongo.db.tasks  # Access to the tasks collection in mongo.db
            tasks.update_one({
                '_id': ObjectId(task_id),
            }, {
                '$set': {
                    'category_name': request.form['category_name'],
                    'complexity': request.form['complexity'],
                    'recipe_name': request.form['recipe_name'],
                    'author_name': request.form['author_name'],
                    'prep_time_mins': int(request.form['prep_time_mins']),
                    'cook_time_mins': int(request.form['cook_time_mins']),
                    'calories': int(request.form['calories']),
                    'servings': int(request.form['servings']),
                    'brief_description': request.form['brief_description'],
                    'ingredients': request.form['ingredients'],
                    'instructions': request.form['instructions'],
                    'recipe_image': request.form['recipe_image'],
                    'favourite': 'favourite' in request.form
                }})
            flash('Your recipe has been updated!')
            return redirect(url_for('task', tasks_id=task_id))
    flash("Apologies, this is not your recipe to edit!")
    return redirect(url_for('task', tasks_id=task_id))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    """
    We access the tasks collection & call to delete selected task.
    """
    if session:
        user = mongo.db.user.find_one({"name": session['username'].title()})
        task = mongo.db.tasks.find_one_or_404({'_id': ObjectId(task_id)})

        if user['name'].title() == task['username'].title():
            tasks = mongo.db.tasks
            tasks.delete_one({
                '_id': ObjectId(task_id)
            })
            return redirect(url_for('index'))

        flash("Apologies, this is not your recipe to edit!")
        return redirect(url_for('task', tasks_id=task_id))
    else:
        flash('Apologies, logged in users can only view this page')
        return redirect(url_for('index'))


@app.route('/count_tasks')  # Enables the total recipe counter
def count_tasks():
    count_tasks = mongo.db.tasks.find().count()
    return render_template("index.html",
                           count_tasks=count_tasks)


@app.route('/favourite_count')  # Enables the favourite recipe counter
def favourite_count():
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    return render_template("index.html",
                           favourite_count=favourite_count)


@app.errorhandler(404)
# 404 error message supports user when Virtual Cookbook incorrectly renders
def page_not_found(e):
    """Route for handling 404 errors"""
    return render_template('404.html',
                           title="Page Not Found!"), 404


@app.route('/profile/<user_id>')
def profile_page(user_id):  # User profile page
    count_tasks = mongo.db.tasks.find().count()
    favourite_count = mongo.db.tasks.find({'favourite': True}).count()
    if 'logged_in' not in session:  # Check if its a logged in user
        flash('Apologies, this profile page viewed by logged in users only.')
        return redirect(url_for('index'))

    current_user = mongo.db.user.find_one({"_id": ObjectId(user_id)})
    task = mongo.db.tasks.find({
        'username': current_user['name']}).sort('_id', pymongo.ASCENDING)
    count = mongo.db.tasks.find({'username': current_user['name']}).count()

    return render_template('profile.html',
                           current_user=current_user, count_tasks=count_tasks,
                           favourite_count=favourite_count,
                           tasks=task, count=count, title="Profile Page")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Function for handling the registration of users"""
    if 'logged_in' in session:  # Check is user already logged in
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():

        user = mongo.db.user
        dup_user = user.find_one({'name': request.form['username'].title()})

        if dup_user is None:
            hash_pass = generate_password_hash(request.form['password'])
            user.insert_one({'name': request.form['username'].title(),
                             'pass': hash_pass})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))

        flash('Attention: This username is already taken. Please try another.')
        return redirect(url_for('register'))
    return render_template('register.html', form=form, title="Register")


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    """Function for User login to Virtual Cookbook"""
    if 'logged_in' in session:  # Check is already logged in
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.user
        logged_in_user = user.find_one({
            'name': request.form['username'].title()})

        if logged_in_user:
            if check_password_hash(logged_in_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('index'))
            flash('Attention: Password is incorrect. Please try again.')
            return redirect(url_for('user_login'))
    return render_template('login.html', form=form, title='Login')

@ app.route('/search', methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    results = mongo.db.tasks.find({'$text': {'$search': str(query)}}).limit(10)
    result_num = mongo.db.tasks.find({'$text': {'$search': query}}).count()
    if result_num > 0:
        return render_template(
            "search.html", results=results, query=query,
            page_title="Search Results",
            message="Your search criteria produced the following results:")
    else:
        return render_template(
            "search.html", results=results,
            query=query, page_title="Search Results",
            message="Please, try a more general term, check the spelling or look up a specific ingredient")


@app.route('/logout')
def logout():
    """Logs the user out and redirects to home"""
    session.clear()  # End the session
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', "5000")),
            debug=True)
