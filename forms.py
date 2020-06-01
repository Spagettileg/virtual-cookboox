import os
from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Optional
from flask_pymongo import PyMongo, pymongo

CSRF = CSRFProtect()

def create_app():
    CSRF.init_app(app)

app = Flask(__name__)
"""
Environment variables SECRET and MONGO_URI set in Heroku
dashboard in production.
"""
app.config['secret_key'] = os.getenv("SECRET")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = "virtual_cookbook"
mongo = PyMongo(app)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RecipeForm(FlaskForm):
    category_name = StringField('category_name', validators=[DataRequired()])
    complexity = StringField('complexity', validators=[DataRequired()])
    recipe_name = StringField('recipe_name', validators=[DataRequired()])
    author_name = StringField('author_name', validators=[DataRequired()])
    prep_time_mins = IntegerField('prep_time_mins', validators=[DataRequired()])
    cook_time_mins = IntegerField('cook_time_mins', validators=[DataRequired()])
    calories = IntegerField('calories', validators=[DataRequired()])
    servings = IntegerField('servings', validators=[DataRequired()])
    brief_description = TextAreaField('brief_description', validators=[DataRequired()])
    ingredients = TextAreaField('ingredients', validators=[DataRequired()])
    instructions = TextAreaField('instructions', validators=[DataRequired()])
    recipe_image = StringField('recipe_image', validators=[DataRequired()])
    favourite = StringField('favourite', validators=[Optional()])
