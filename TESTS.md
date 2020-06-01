# Virtual-Cookboox | Test Analysis & Report 

Access main [READEME](https://github.com/Spagettileg/virtual-cookboox/blob/master/README.md) file

View [Virtual-Cookboox](https://virtual-cookboox.herokuapp.com/) as a deployed project in Heroku

## Table of Contents
1. [Introduction](#introduction) 
2. [Systems Based Testing](#systems-based-testing)
3. [Manual Testing](#manual-testing)
    * [Registration Testing](#registration-testing)
    * [Recipe testing](#recipe-testing)
    * [Navigation Testing](#navigation-testing)
4. [Code Validation](#code-validation)
    * [Responsiveness and Rendering](#responsiveness-and-rendering)
    * [Browser Compatability](#browser-compatability)
    

## Testing
### Introduction
A combination of system based and manual testing processes was applied to this project to ensure the UXD was upheld. To make sure the data was correctly loaded, images would be successfully rendered and dynamic links would accurately support the user to navigate through this application.

The software has been thoroughly tested in many ways. JavaScript and its associated functions have all undergone extensive manual testing. JS hint was used to help validate the Javascript code.

Werkzeug library import has helped identity logic errors when trying to get Flask application, Python & MongoDB database to all correctly interact. 

Manual testing has been based upon a walkthrough of key process steps the User will experience. This is coupled with process alignment to CRUD (Create, Read, Update & Delete).   

All possible user actions were mimicked to put the tester in the shoes of the user. 

### Systems Based Testing 
- CRUD Operations tested = **READ**
- Mongo Shell was used to test the cloud database link to the Flask application. The virtual cookboox recipe database holds 41 recipes at present, with each recipe containing numerous key value pairings. 
- Current keys, per record, as follows: (the values doe vary by record due to the differing nature of the food recipe)
    - `category_name`, `recipe_name`, `author_name`, `prep_time_mins`, `cook_time_mins`, `complexity`, `favourite`, `servings`, `brief_description`, `calories`, `ingredients`, `instructions` and `recipe_image`.

- Outcome of tests run in Mongo Shell:

Mongo Shell Query                                           | Response (count) | Comments
------------------------------------------------------------|------------------|---------
`db.tasks.count();`                                         |        41        | Total number of records
`db.tasks.find({'favourite' : false}).count();`             |        31        | Number non-favourite recipes 
`db.tasks.find({'favourite' : true}).count();`              |        10        | Number of favourite recipes
`db.tasks.find({'author_name' : "BBC Good Food"}).count();` |        14        | Number of recipes authored by BBC Good Food
`db.tasks.find({'category_name' : "Fish"}).count();`        |         8        | Number of Fish based recipes

- Flask Application testing for connection to web-browser:
 
```
import os
from flask import Flask
app = Flask(__name__)
@app.route('/')  # Route decorator & default test
def hello():
    return 'Hello World'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

```
- Outcome in Bash Ubuntu (Flask testing):

```
ubuntu:~environment $ python3 app.py
    *Serving Flask app "app" (lazyloading)
    *Envioronment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
    *Debug mode: on
    *Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    *Restarting with stat
    *Debugger is active
    *Debugger PIN: xxx-xxx-xxx

```
- Outcome in web browser (Flask testing passed):

```
Hello World

```

### Manual Testing
##### Registration Testing
###### •	Username (register.html)
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Key url address in web browser
2.	Click in 'username' field (placeholder text helps the user with data entry)
3.	Key in first name (max character length = 20)
4.	If empty fields exist when clicking 'Submit', then user will get error message with request to complete missing data
5.	If username already taken by another user, then warning message appears to invite user for a different username
6.	If user has already registered then they can click on a link to move to login screen


###### •	Password (register,html)
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.  If user has already registered then they can click on a link to move to login screen
2.  Click in 'Password' field (placeholder text helps the user with data entry)
3.	Key in password (max character length = 20)
4.	If empty fields exist when clicking 'Submit', then user will get error message with request to complete missing data
5.  Click 'Submit' button to complete both the registration process


###### •	Username (login.html)
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Key url address in web browser
2.	If user has selected login by mistake, they can click on a link to move to register screen
3.	Click in 'username' field (placeholder text helps the user with data entry)
4.	Key in first name (max character length = 20)
5.	If empty fields exist when clicking 'Submit', then user will get error message with request to complete missing data
6.	If username does not match registered user details, then warning message appears to invite user for a different username


###### •	Password (login,html)
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	If user has selected login by mistake, they can click on a link to move to register screen 
2.  Click in 'Password' field (placeholder text helps the user with data entry)
3.	Key in password (max character length = 20)
4.	If empty fields exist when clicking 'Submit', then user will get error message with request to complete missing data
5.	If password does not match registered user details, then warning message appears to invite user for a different password
6.  Click 'Submit' button to complete both the authentication process

##### Recipe Testing
###### •	Home Page (portfolio.html)
- CRUD Operations tested = **READ**
1.	All Users should see 6 different food genre recipe cards on the home page
    - Meat
    - Poultry
    - Fish
    - Vegetables
    - Grains
    - Pasta
2. Click on a food genre recipe card

###### •	Summary Recipe Selection Page (meat.html, poultry.html, fish.html, veg.html, grains.html & pasta.html)
- CRUD Operations tested = **READ**
1.	All Users will be presented with individual recipe cards that fall under the selected food genre
2.	Each recipe card structure = Image, recipe name, brief description & 'Detail' button
3.	Hover over the 'Detail' button to see colout change from pea green #61892F to lime green #86C232
4.	User to click 'Detail' button to proceed to detailed view of the recipe

*Observation*: A tablet device landscape view appears to have compressed all padding & margin around each recipe card on show. This has the effect of merging the cards together. As a fix, a media query was written to set the screen orientation to portrait view and preserve padding and margin, per recipe card. 	

###### •	Detailed Recipe View (recipe.html)
- CRUD Operations tested = **READ**
1.  All Users will be presented with an individual recipe card containing the following information:
    - Recipe image
    - Recipe name
    - Brief description of the recipe
    - Icon graphic & authors name
    - Icon graphic & complexity (Easy or Challenge)
    - Icon graphic & preparation time
    - Icon graphic & cooking time
    - Icon graphic & calories
    - Icon graphic & servings
    - Full list of Ingredients
    - Detailed Instructions on how to cook

*Observation*: The recipe image was too large and disproportionate to remainder of recipe detail data, specific to desktop & larger devices. Media query created for desktop and larger devices to set height to auto and image max-width to 18.75rem.     
2.	Should the recipe content be fine with User, then User can follow next steps, as follows:
    - Click back page control to revisit summary recipe selection page
    - Click on the navbar brand logo 'Virtual Cookboox' to return to home page
    - Leave the application by using normal browser control
3.	Logged in users have options to [Edit](#edit-recipes) & [Delete](#delete-recipes) tested in their respective categories 

##### Navigation Testing
###### •	Navbar tests
- CRUD Operations tested = **READ**
1.	Hover on 'Virtual Cookboox' navbar brand for pea green (#61892F) text to flip from 'Virtual' to 'Cookboox'. There is a 2 second cycle time to complete this process  
2.	Click on ‘Virtual Cookboox’ navbar brand from anywhere within the website
3.	User will be routed back to home page
4.	Recipe Count & Favourite Count pulls through both all and favourite recipes held in mongodb atlas cloud server. Backend code (python3) then ensures this data is injected into the flask application

*Observation*: The presence of both recipe and favourite counters in the navbar occupies considerable screen space. Therefore, a decision was made to hide these counters in mobile device view via a media query   
5.	Hover on 'My Recipes' button for colour to change from pea green `#61892F` to lime green `#86C232` (Logged in users only)
6.	Click on 'My Recipes' button to take user to profile.html page (Logged in users only)
	
*Observation*: My recipe button were positioned to extreme right of the navbar, in mobile device view. Media query was written to add -1rem padding & margin, font-size 0.8rem and height 1.4rem to fix
7.	Hover on 'Add Recipe' button for colour to change from pea green `#61892F` to lime green #86C232 (Logged in users only)
8.	Click on 'Add Recipe' button to take user to [Add Recipe](#add-recipes) data entry template (Logged in users only)
	
*Observation*: Add recipe button were positioned to extreme right of the navbar, in mobile device view. Media query was written to add -1rem padding & margin, font-size 0.8rem and height 1.4rem to fix
	
###### •	Homepage portfolio
- CRUD Operations tested = **READ**
1.	Go to home page
2.	Click on food genre image
3.	All Users are passed through to list of recipes, with summary information, that belong to the selected food genre 
4.	Click navbar brand logo 'Virtual Cookbook' to return to homepage in readiness to select a different food genre
	
###### •	Footer links tests
- CRUD Operations tested = **READ**
1.	Go to footer section
2.	Click social media icons (LinkedIn & GitHub)
3.	All Users are passed through to website authors’ actual live pages
4.	Click on 'contact' link
5.	All Users are passed through to website authors' personal linkedin live page
	
###### •	Other Buttons / Icon functionality tests
*Social Media*
- CRUD Operations tested = **READ**
1.	Scroll to footer
2.	Hover on social media icons
3.	For LinkedIn, colour change from light grey to LinkedIn corporate colour (blue `#0077B5`). Inner icon colour changes from black to white
4.	For GitHub, colour change from light grey to GitHub corporate colour (purple `#6e5494`). Inner icon colour changes from black to white
5.	Both social media icons contain a fractional timing delay to help all users understand icon is active, prior to being clicked 

*Edit Button*
- CRUD Operations tested = **READ & UPDATE**
1.  Logged in users only 
2.	Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html))page, via 'My Recipes' or recipe.html through main portal 
3.	Hover on edit button and colour chamge fron yellow to green
4.	Click on edit button to take user to edit recipe page

*Delete Button*
- CRUD Operations tested = **READ, UPDATE & DELETE**
1.  Logged in users only 
2.  Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html)) page via 'My Recipes' or recipe.html through main portal
3.	Hover on delete button and colour chamge fron yellow to red
4.	Click on delete button to take user to home page, following deletion of recipe

*Favourites Tickbox*
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.  Logged in users only 
2.  Navigate to Edit Recipe page &/or Add Recipe page via 'My Recipes' or recipe.html through main portal
3.  Click on 'favourite' tickbox to uncheck = No favourite
4.  Click on 'favourite' tickbox to check = favourite
5.  Click 'Confirm' button to complete edit
6.  User will return back to recipe detail page to view their recipe updates 
7.  Navbar counter will increase by +1 for favourite and -1 for non-favourite
8.  Navbar counter will not be less than zero

*Submit Edit Button*
- CRUD Operations tested = **READ & UPDATE**
1. Logged in users only 
2. Navigate to Edit Recipe page via 'My Recipes' or recipe.html through main portal
3. Hover on 'Submit' button and colour chamge fron yellow to green
4. Click on 'Submit' button to complete edit
5. User will return back to recipe detail page to view their recipe updates 

*Submit Add Recipe*
- CRUD Operations tested = **READ & UPDATE**
1. Logged in users only 
2. Navigate to Add Recipe page via navbar
3. Hover on 'Submit' button and colour chamge from pea green `#61892F` to lime green `#86C232`
4. Click on 'Submit' button to complete add
5. User will return back to home page. New recipe can be viewed upon clicking an appropriate food genre image 

##### Add Recipes
- CRUD Operations tested = **CREATE, READ & UPDATE**
1. Logged in users only 
2. Hover on the 'Add Recipe' button in the navbar to show user the button is active
3. Click 'Add Recipe' button
4. User will be presented with a blank recipe template, with placeholder guidance text and required data, containing the following data requests:
    - Food genre - User is required to enter Meat, Poultry, Fish, Vegetables, Grains or Pasta as a genre
    - Complexity - User is required to enter 'Easy' or 'Challenge'
    - Recipe Name - Text data entry 
    - Authors name - Text data entry
    - Preparation time - Numbers only data entry
    - Cooking time - Numbers only data entry
    - Calories - Numbers only data entry
    - Servings - Numbers only data entry
    - Brief description of the recipe
    - Full list of Ingredients
    - Detailed Instructions on how to cook
    - Recipe image - url web address required from User 
    - Tickbox for favourite recipe. Tick for yes or no tick for no
5.  User must complete all data entry fields. Auto message appears to signal missing data entry 
6.	Click 'Submit' button for user to formally add their recipe to the application
7.	User is then routed back to homepage
8.	New recipe can be viewed by clicking on food genre image relative to the recipe that has been added 

##### Edit Recipes
- CRUD Operations tested = **READ & UPDATE**
1. Logged in users only 
2. Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html)) page via 'My Recipes' or recipe.html through main portal
3. Hover on 'Edit' button and colour change fron yellow to green to show the button is active
4. Click on 'Edit' button to complete edit
5. User will be presented with a blank recipe template, containing the following recipe data fields:
    - Food genre - User is required to enter Meat, Poultry, Fish, Vegetables, Grains or Pasta as a genre
    - Complexity - User is required to enter 'Easy' or 'Challenge'
    - Recipe Name - Text data entry  
    - Authors name - Text data entry
    - Preparation time - Numbers only data entry
    - Cooking time - Numbers only data entry
    - Calories - Numbers only data entry
    - Servings - Numbers only data entry
    - Brief description of the recipe
    - Full list of Ingredients
    - Detailed Instructions on how to cook
    - Recipe image - url web address required from User 
    - Tickbox for favourite recipe. Tick for yes or no tick for no
6.	Hover cursor over 'Confirm' button and colour change fron yellow to green to show the button is active
7.	Click 'Submit' button for user to formally edit their recipe in the application
8.	User is then routed back to recipe detail page to view their respective changes

##### Delete Recipes
- CRUD Operations tested = **READ, UPDATE & DELETE**
1. Logged in users only 
2. Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html)) page via 'My Recipes' or recipe.html through main portal
3. Hover on 'Delete' button and colour change fron red to green to show the button is active
4. Click on 'Delete' button to complete recipe delete
5. User is then routed back to homepage

##### Recipe Statistics
*Favourites*
- CRUD Operations tested = **CREATE, READ, UPODATE & DELETE**
1.  Logged in user navigates to [Edit Recipe](#edit-recipes) page &/or [Add Recipe](#add-recipes) page via 'My Recipes' or recipe.html through main portal
2.  Click on 'favourite' tickbox to uncheck = No favourite
3.  Click on 'favourite' tickbox to check = favourite
4.  Click 'Confirm' button to complete edit
5.  User will return back to recipe detail page to view their recipe updates 
6.  Navbar counter will increase by +1 for favourite and -1 for non-favourite (viewed by all users)
7.  Navbar counter will not be less than zero (viewed by all users)
  
*Recipes*
- CRUD Operations tested = **CREATE, READ, UPODATE & DELETE**
1. Logged in users complete [adding](#add-recipes) or [deleting](#delete-recipes) of a single recipe
2. Navbar counter will show +1 for adding recipe (viewed by all users)
3. Navbar counter will show -1 for recipe deletion (viewed by all users)
4. Navbar counter will not be less than zero (viewed by all users)

### Code Validation

Code       | Url Link                          | Filename      | Outcome | Comments
-----------|-----------------------------------|---------------|---------|---------
HTML5      |https://validator.w3.org           |base.html      |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |index.html     |Pass     |Jinja templating language used = ok        
HTML5      |https://validator.w3.org           |register.html  |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |login.html     |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |profile.html   |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |meat.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |poultry.html   |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |fish.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |veg.html       |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |grains.html    |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |pasta.html     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |recipe.html    |Pass     |HR stray end tag reported,but all ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |addrecipe.html |Pass     |Jinja templating language used = ok  
HTML5      |https://validator.w3.org           |editrecipe.html|Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |404.html       |Pass     |Jinja templating language used = ok
CSS3       |https://jigsaw.w3.org/css-validator|style.css      |Pass     |W3C CSS Validator results - CSS level 3 + SVG - negative padding -1rem triggered a warning message = ok
Javascript |https://jshint.com/                |index.html     |Pass     |Some instances of $ being undefined due to using jQuery. No errors found    
Javascript |https://jshint.com/                |helper.js      |Pass     |No errors found
Python3    |http://pep8online.com              |recipe.py      |Pass     |All convention errors corrected = ok
Python3    |http://pep8online.com              |forms.py       |Pass     |All convention errors corrected = ok

### Responsiveness & Rendering
Chrome DevTools together with a selection of mobile, table and desktop devices were relied upon through the entire software development cycle. A key objective was to test both the rendering and responsiveness of the software application against multiple screen resolutions and web browser platforms. Any bugs identified were debugged in real time with special observations noted in a [testing matrix control document](https://github.com/Spagettileg/virtual-cookboox/blob/master/tests/User%20Testing_3rd%20Milestone%20Project_vfinal%20draft.xlsx).

The Virtual Cookboox application has been tested by students from the Slack community, together with friends and family members. Feedback on what worked well and what did not was recorded and suitable corrections to the code were keyed.

In the final analysis, this application can be passed as fully responsive across all devices that participated in testing.

## Browser Compatability

The following browsers were used in testing the Virtual Cookbook application. Internet Explorer was out of scope for testing due to obsolete capability

platform | version
---------|--------
Chrome   |76.0.3809.132
Edge     |44.18362.267.0
Firefox  |67.0.3
Safari   |12.4.1
Opera    |63.0.3368.71
