from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Optional


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    health_labels = TextAreaField('Health Labels', validators=[Optional()])
    diet_labels = TextAreaField('Diet Labels', validators=[Optional()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    cooking_time = IntegerField('Cooking Time', validators=[DataRequired()])
    serving_size = IntegerField('Serving Size', validators=[DataRequired()])
    calories = IntegerField('Calories', validators=[DataRequired()])
    recipe_image = StringField(
        'Copy Image Address Link', validators=[DataRequired()])
    source = StringField('Source URL Link', validators=[Optional()])