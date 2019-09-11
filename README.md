# 3rd Milestone Project | Virtual Cookbook
###### Data-Centric Development - Code Institute 

Virtual Cookbook has been designed for people of all cooking capabilities to help produce delicious and wholesome meals. This application provides quick and intuitive access to recipes borne out of selected food genres.

If you are struggling for time to cook, notice on preparation and cooking time is made clear. Diet conscious consumers can view the calories per serving numbers to help plan for the right recipe.

Finally, you can add new recipes to this application by simply clicking on 'Add Recipe' at the top of the screen. Favourite recipes can be recorded, existing recipes can be edited and unwanted recipes can be deleted. All at the users fingertips.


## Demo
A live demo can be found [here](https://pbf-third-milestone-project.herokuapp.com/).

## Navigate to detail
[UXD Considerations](#uxd-considerations) || [User](#user) | [Virtual Cookbook](#virtual-cookbook) 

[Wireframes](#wireframes) || [User Stories](#user-stories) 

[Design](#design) || [Schema](#schema) | [Application Framework](#application-framework) | [Database](#database) | [CSS Frameowrk](#css-framework) | [Colour Palette](#colour-palette) | [Typography](#typography) | [Icon Graphics](#icon-graphics)

[Database inc Source Data](#database-inc-source-data)

[Technologies Applied](#technologies-applied) || [Languages](#languages) | [Libraries](#libraries) | [Tools](#tools) | [Hosting](#hosting)

[Virtual Cookbook Summary Functions](#virtual-cookbook-summary-functions) ||

[Features](#features) || [Features Left to Implement](#features-left-to-implement)

[Testing](#testing) || [Introduction](#introduction) | [Systems Based Testing](#systems-based-testing) | [Manual Testing](#manual-testing) | [Code Validation](#code-validation) | [Responsiveness & Rendering](#responsiveness--rendering) 

[Browser Compatibility](#browser-compatibility) 

[Deployment](#deployment) || [Deployment To Heroku](#deployment-to-heroku) | [Local Deployment](#local-deployment)

[Credits](#credits) || [Content](#content) | [Media](#media) | [Acknowledgements](#acknowledgements)

## UXD Considerations
### Ambition

#### User
A thorough registration process lies in waitng for the user to secure their personal credentials, prior to access the website home page. All data entry requests are mandatory, with controls to support integrity of data entry. This process will provide the user with an acceptable level of assurance that unauthorised access to their recipe data will not be tolerated.     

The website design encourages the user to access both modern and traditional recipes via clear signposting of 6 food genres (Meat, Poultry, Fish, Vegetables, Grains & Pasta). The intention is for these sub-portals to take over from 'type & search' to reduce user thinking time on what to find and replaced by a seduction of great images and narrative.

Furthermore, the user can extend their amazing personal experience to edit existing recipes, should they seize the opportunity to improve the recipe. New recipes can be added by the user via a button click from the host page navbar. Data entry has been made easy with placeholder text visible in all data input boxes, with careful attention placed upon the quality of data entry and subsequent compatability with backend storage in the cloud. Both new and existing recipes can be flagged as a favourite or deselected through the click of a simple tickbox. 

Unwanted recipes can be deleted through a 'one and done' button click. This button has been painted red for the user to view as a danger sign post. For this application release, deleted recipes are non-recoverable. 

Time waits for no one. Therefore, all recipes include mandatory preparation and cooking times to help the user plan for meals that fit in with their current lifestyle. Diet conscious users have access to calory count data, with the numbers based upon per food serving.    

Imagery and recipe narrative selected throughout the site design has been mostly sourced from BBC Good Food Guide to establish an excellent provenance, enjoyable viewing experience using quality ingredients and generate confidence to produce delicious meals. Integrity of recipe design is maintained by including the originating recipe authors' name.

A summary of total recipes and total favourite recipes is on view in the navbar, irrespective of where the user finds themself in the website.

Finally, the 'Virtual Cookbook' navbar brand is configured to move the user back to the home page and should be used upon completion of a recipe edit or when the user wants to view all 6 food genre categories. 

#### Virtual Cookbook
- Provide a simple and intuitive site for the user to click, search, add & delete both modern & traditional cooking recipes, where age is no barrier to entry.
- On a personal note, creating a multi-layered learning and practice experience in frontend and backend programming. Substantial effort and desire to integrate the use of HTML5, CSS3, Bootstrap4, JavaScript, Python3, MongoDB Atlas, Flask and Jinja.
- Nest stage generation is to move on from a personal recipe application to enterprise scale where professional kitchens and learning institutions leverage the power of code in the cloud to access quality recipes to create industry best practice and blue print models for recipe innovation.  

## Wireframes
My [wireframe mock up design](https://github.com/Spagettileg/pbf-third-milestone-project/tree/master/plans/wireframes) has been developed as a fully responsive application capable of running on mobile, tablet & desktop devices. All mock up material was created in Balsamiq and has been appended as .bmpr file on GitHub. The mock up design has stayed consistent with the original planning. 

## User Stories
> I need an app that provides quick and intuitive access to recipes across the globe [READ]

> I don’t have much time for cooking in the week, so I need to understand time taken to cook quality meals [READ]

> Some of my friends are worried about calory content in their food. I need to understand calory content per recipe serving {READ]

> I'd like to upload new recipes and contribute to existing recipes, to share my love and passion for good, wholesome eating [CREATE & UPDATE]

> I want to remove unwanted recipes from my collection [DELETE]

## Design
### Schema
My [schema](https://github.com/Spagettileg/pbf-third-milestone-project/blob/master/plans/schema/Schema%20Plan%20v1.pdf) was developed through de-engineering of the User Stories to then produce a conceptual design model. This model then formed the foundation to the project data requirements and ultimately the build of a database and the rules governing the use of the data. The schema design has evolved during the course of the project as better information and knowledge of database technology improved.

### Application Framework
Flask application framework was a prerequisite in the design of this project, according to the project brief.

### Database
MongoDB Atlas NoSQL database was used for this project. Key reason supporting my selection was the database was highly scalable and stores data is non-relational format. The data collections format is very well conditioned to support JSON files via the 'Key':'Value' structure and was a good fit to house my recipe raw data. The same data can be easily stored across multiple servers in the cloud.

The database consists of the following collections:
1. Categories - Meat, Poultry, Fish, Vegetables, Grains & Pasta
2. Tasks - List of key value pairs that are consistent per recipe record

### CSS Framework
Bootstrap 4 was the chosen framework for styling my project. I used the bootstrap grid extensively to support responsiveness on mobile, tablet and desktop devices. Materializecss had featured as part of my earlier work in this project, but I lost valuable developer time with code conflicting with Bootstrap 4. The latter was dropped with Bootstrap 4 given sole exclusivity rights to the formatting of my project. 

### Colour Palette
Colours used in this project were sourced from [Gorgeous Contrast](https://visme.co/blog/website-color-schemes/) palette in visme.com. Essentially, various shades of green and black worked well with the multiple array of colours that were present in the food recipe imagery.

### Typography
Monserrat & Lato fonts were used throughout this project. H1 header was used in the home page to announce Virtual Cookbook brand to the user. Thereafter, H2 & H3 was used for sub-heading narrative, with H6 being used user information guide purposes to understand the function of both edit recipe & delete recipe buttons.

Font-weight of 500 & 700 was used to help draw attention to the user for both branding and instruction too.

### Icon Graphics
Font Awesome 5 icon graphics were used in conjunction with Bootstrap 4, primarily in the design of the recipe detail page, including edit and add recipe pages too.

- authors name = `fas fa-user`
- complexity = `fas fa-graduation-cap`
- preparation time - `far fa-clock`
- cooking time - `far fa-clock`
- calories - `fas fa-weight`
- servings - `fas fa-users`

## Database inc Source Data
[BBC Good Food Guide](https://www.bbcgoodfood.com/recipes) was the source of the raw project data. I manually keyed the raw data into MongoDB database via Virtual Cookbook Tasks collection, adopting the key valuie pair approach. Both `MONGO_URI` and `MONGO_DBNAME` database were configured in the flask application and the import of PyMongo library enabled the injection of cloud server data into the Flask application. 

## Technologies Applied
### Languages
•	[HTML5](https://html.spec.whatwg.org/multipage/) used as the markup language

•	[CSS3](https://www.w3.org/Style/CSS/) used to style the HTML

•	[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) used mostly for DOM manipulation

•	[Python3](https://www.python.org/) used to run the backend application

### Libraries
•	[Font Awesome](https://fontawesome.com/) v5.8.2 to provide the icon set

•	[Google Fonts](https://fonts.google.com/) provided the fonts used throughout the project

•	[jQuery](https://jquery.com/) is used to manipulate the DOM, for example buttons, and showing / hiding elements

•	[Flask](https://flask.palletsprojects.com/en/1.1.x/) v1.0.2 is the micro web framework that runs the application

•	[PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) 2.3.0 was used to enable the python application to access the Mongo database

•	[Jinja](https://jinja.palletsprojects.com/en/2.10.x/) v2.10.1 is the default templating language for flask and is used to display data from the python application in the frontend html pages


### Tools
•	[AWS Cloud9](https://aws.amazon.com/cloud9/) a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser.

•	[MongoDB Atlas](https://www.mongodb.com/cloud/atlas) global cloud database service for modern applications providing availability, scalability, and compliance with the most demanding data security and privacy standards.

•	[Git](https://git-scm.com/) is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

•	[GitHub](https://github.com/) is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

•	[Balsamiq](https://balsamiq.com/) is a small graphical tool to sketch out user interfaces, for websites and web / desktop / mobile applications and used to visualise my project through mock-up design.

### Hosting
•	[Heroku](https://heroku.com) is used to host the deployed application - 'virtual cookbook'

## Virtual Cookbook Summary Functions

## Features
### Feature 1 - Registration & Authentication 

•	User has a mandatory requirement to complete the registration & authentication form when clicking on the sites url address 

•	Data entry requirements include firstname, lastname, email, phone number, birthday, username and password. Where appropriate, data entry governance exists in the form of required attributes meaning all requests for data must be completed prior to access the full Virtual Cookbook website   

•	The process to register is controlled by previous, next & submit buttons  

### Feature 2 - Navbar brand logo 

•	Normal html convention rules followed by placing the navbar brand logo 'Virtual Cookbook' in the navbar, at the top left corner. The User has unhindered access to this logo and when clicked, will always return the user to the homepage.  

### Feature 3 - Recipe counter

•	A read only view created to show a count of all recipes that have been added to the Virtual Cookbook . The cursor has been set to none when the User hovers over the counter

•	The counter will be activated by the User should they add a recipe (+1) or delete a recipe (-1). The counter will not fall below zero 

### Feature 4 - Favourite recipe counter

•	A read only view created to show a count of all favourite recipes that have been added to the Virtual Cookbook The cursor has been set to none when the User hovers over the counter    

•	The counter will be activated by the User should they elect to tick the 'favourites box' contained in either the 'add recipe' or 'edit recipe' pages. The counter will increment (+1) if the box is ticked or reduce (-1) if the box is unticked. The counter will not fall below zero 

### Feature 5 - Add recipe 

•	User can click on 'Add Recipe' button located at top right of the navbar. The navbar is present on all pages in the website, following completion of the registration process  

•	Once button has been clicked, the User is presented with a clear and intuitive data entry form with guidance provided by placeholder text &/or dropdown boxes. All input and dropdown are required to be completed, otherwise the User will receive a mandatory warning message to complete. Incomplete recipes cannot be added to Virtual Cookbook 

•	Information required from the User includes food genre dropdown box, recipe complexity dropdown box, recipe name, author name, recipe preparation time, recipe cooking time, calories per serving, brief description of the recipe, full list of ingredients, detailed instructions on how to cook, url web address for a recipe image & a tickbox for favourite recipes       

•	Once all required recipe information added, the User should click 'Confirm' button. User is then routed back to homepage  

•	New recipe can be viewed by clicking on food genre image relative to the recipe that has been added

### Feature 6 - Overview of Virtual Cookbook 

•	An elevation statement has been created to promote Virtual Cookbook to the User to set out its purpose, value generators, responsive to user stories and reference to key features  

### Feature 7 - Food genre image portal gateway

•	Six fully responsive images of different food genres on display for the User. Images of meat, poultry, fish, vegetables, grains & pasta are clickable and will migrate the User to the respective recipe collection  

•	To save on any confusion, all images have been name tagged  

### Feature 8 - Food genre recipe collection 

•	A Recipe image, recipe name, brief description and a recipe detail button are displayed in a card style. This structure is then repeated for all recipes 

•	If the User likes a certain recipe after reading the summary information, then they can simply click the 'Detail' button to find out much more information

•	There is every chance the User does not find the recipe they're looking for. In this instance, the User can elect to add a recipe of their own or exit the Virtual Cookbook  

### Feature 9 - Detailed recipe card 

•	User will be presented with an individual recipe card containing a recipe image, recipe name, brief description of the recipe, icon graphic & authors name, icon graphic & complexity (Easy or Challenge), icon graphic & preparation time, icon graphic & cooking time, icon graphic & calories, icon graphic & servings, full list of Ingredients & detailed Instructions on how to cook

•	Should the recipe content be fine with User, then User can follow next steps, as follows:

1.	Click back page control to revisit summary recipe selection page
2.  Click on the navbar brand logo 'Virtual Cookbook' to return to home page
3.  Leave the application by using normal browser control

•	User will have access to both [Edit](#edit-recipes) and [Delete](#delete-recipes) recipe material 

### Feature 10 - Edit recipe 

•	User can click on 'Edit Recipe' button located at the bottom of the recipe detail page   

•	Once button has been clicked, the User is presented with all the recipe information in a series of dropdown and input boxes  

•	Information to be updated by the User includes food genre dropdown box, recipe complexity dropdown box, recipe name, author name, recipe preparation time, recipe cooking time, calories per serving, brief description of the recipe, full list of ingredients, detailed instructions on how to cook, url web address for a recipe image & a tickbox for favourite recipes       

•	Once all updated recipe information added, the User should click 'Confirm' button. User is then routed back to the recipe detail page showing an updated view of the recipe  

### Feature 11 - Delete recipe 

•	For unwanted recipes, the User can click on 'Delete Recipe' button located at the bottom of the recipe detail page  

•	Once button has been clicked, the User has committed to complete removal of the recipe record, with no reversal. Thereafter, the User is routed to the homepage  

### Feature 12 - Favourite recipe tickbox 

•	User to navigate to either 'Edit Recipe' or 'Add Recipe' page to mark their given recipe as a favourite. A simple tickbox has been created to record the User actions in both the application and cloud database too. Tick for favourite and untick for non-favourite   

•	Summary favourite count statistics can be viewed in the navbar. The cursor has been set to none as the data is only intended for read only purposes   

### Feature 13 - Footer 

•	Provides a social media link to LinkedIn and a link to my GitHub page. Fonts (icons) secured from bootstrap 4 / font awesome 5. The links are wired to the website designers’ respective social media sites. A .hover pseudo class has been used to provide a background colour change (light grey to corporate colour code) and font colour change too.   

•	Contact link embedded into the conatact section that enables the user to send requests for software development support direct to website authors LinkedIn account 

### Feature 14 - 404 alert page

•	Provides a friendly sign post for the user in the event an incorrect link has been clicked and the user has the option to click back into a correct link

### Features Left to Implement

- The registration process can be further improved by leveraging the current Javascript code to improve data entry governance. For exmaple;
    - Firstname & last name to beging with a capital letter
    - Email structure to recognise HTTPS/, @gmail, @yahoo, etc
    - Telephone numbers to be recognised with international prefixes for both landline and mobile telephony devices
    - Passwords to be unique. auto-generated and include special characters. Also include a password reset capability  
     
- Breakfasts, Hors D'oeuvre's, Starters and Desert recipes to be included for a future release
- Deleted recipes to be reversed by the user, in the event human error was responsible for the original recipe deletion 
- A dedicated favourite recipes page that allows the user to view collectively and in detail
- Additional food genres that relate to cuisine by location. The list is will be quite extensive and could be developed by creating a new 'key value' field, per record held in cloud database. For example;
    - `country_name': "Chinese"`
    - `country_name': "Italian"`
    - `country_name': "Indian"`
    - `country_name': "Mexican"`

## Testing

### Introduction
A combination of system based and manual testing processes was applied to this project to ensure the UXD was upheld. To make sure the data was correctly loaded, images would be successfully rendered and dynamic links would accurately support the user to navigate through this application.

The software has been thoroughly tested in many ways. JavaScript and its associated functions have all undergone extensive manual testing. JS hint was used to help validate the Javascript code.

Werkzeug library import has helped identity logic errors when trying to get Flask application, Python & MongoDB database to all correctly interact. 

Manual testing has been based upon a walkthrough of key process steps the User will experience. This is coupled with process alignment to CRUD (Create, Read, Update & Delete).   

All possible user actions were mimicked to put the tester in the shoes of the user. 

### Systems Based Testing 
- CRUD Operations tested = **READ**
- Mongo Shell was used to test the cloud database link to the Flask application. The virtual cookbook recipe database holds 41 recipes at present, with each recipe containing numerous key value pairings. 
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
###### •	Name (index.html)
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Key url address in web browser
2.	Click in 'first name' field (placeholder text helps the user with data entry)
3.	Key in first name (max character length = 40)
4.	Click in 'last name' field (placeholder text helps the user with data entry)
5.	Key in last name (max character length = 40)
6.	Click 'Next' button to proceed to next screen
7.	If empty fields exist when clicking 'Next', then user will get error message with request to complete missing data

###### •	Contact Info
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Circle dot at bottom of screen changes to green. Ok to proceed
2.	Click 'Previous' button if user wants to update either first or last name
3.	Click in 'email' field (placeholder text helps the user with data entry)
4.	Key in email address
5.	Click in 'Phone' field (placeholder text helps the user with data entry)
6.	Key in phone number in the suggetsed xxxxx xxxxxx format
7.	Click 'Next' button to proceed to next screen
8.	If empty fields exist when clicking 'Next', then user will get error message with request to complete missing data
	
###### •	Birthday
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Circle dot at bottom of screen changes to green. Ok to proceed
2.	Click 'Previous' button if user wants to update either Contact Info or back again to first or last name
3.  Click in 'dd' field (placeholder text helps the user with data entry)
4.	Key in dd or day (Min value = 1, Max value = 31)
5.	Click in 'mm' field (placeholder text helps the user with data entry)
6.	Key in mm or month (Min value = 1, Max value = 12)
7.	Click in 'yyyy' field (placeholder text helps the user with data entry)
8.	Key in yyyy or year (Min value = 1900, Max value = 2020) 
9.	Click 'Next' button to proceed to next screen
10.	If empty fields exist when clicking 'Next', then user will get error message with request to complete missing data

###### •	Login Info
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.	Circle dot at bottom of screen changes to green. Ok to proceed
2.	Click 'Previous' button if user wants to update either Birthday or back again contact info or to first & last name
3.  Click in 'Username' field (placeholder text helps the user with data entry)
4.	Key in username
5.	Click in 'Password' field (placeholder text helps the user with data entry)
6.	Key in password (Characters show as an asterix with max 8 characters permitted) 
7.  Click 'Submit' button to complete bothe the registration & authentication process
8.	If empty fields exist when clicking 'Submit', then user will get error message with request to complete missing data

##### Recipe Testing
###### •	Home Page (portfolio.html)
- CRUD Operations tested = **READ**
1.	User should see 6 different food genre recipe cards on the home page
    - Meat
    - Poultry
    - Fish
    - Vegetables
    - Grains
    - Pasta
2. Click on a food genre recipe card

###### •	Summary Recipe Selection Page (meat.html, poultry.html, fish.html, veg.html, grains.html & pasta.html)
- CRUD Operations tested = **READ**
1.	User will be presented with individual recipe cards that fall under the selected food genre
2.	Each recipe card structure = Image, recipe name, brief description & 'Detail' button
3.	Hover over the 'Detail' button to see colout change from pea green #61892F to lime green #86C232
3.	User to click 'Detail' button to proceed to detailed view of the recipe


###### •	Detailed Recipe View (recipe.html)
- CRUD Operations tested = **READ**
1.  User will be presented with an individual recipe card containing the following information:
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
2.	Should the recipe content be fine with User, then User can follow next steps, as follows:
    - Click back page control to revisit summary recipe selection page
    - Click on the navbar brand logo 'Virtual Cookbook' to return to home page
    - Leave the application by using normal browser control
3.	Options to [Edit](#edit-recipes) & [Delete](#delete-recipes) tested in their respective categories 

##### Navigation Testing
###### •	Navbar tests
- CRUD Operations tested = **READ**
1.	Hover on 'Virtual Cookbook' navbar brand for text to change from pea green #61892F to lime green #86C232  
2.	Click on ‘Virtual Cookbook’ navbar brand from anywhere within the website
3.	User will be routed back to home page
4.	Hover on 'Add Recipe' button for colour to change from pea green #61892F to lime green #86C232
5.	Click on 'Add Recipe' button to take user to [Add Recipe](#add-recipes) data entry template
	
###### •	Homepage portfolio
- CRUD Operations tested = **READ**
1.	Go to home page
2.	Click on food genre image
3.	User is passed through to list of recipes, with summary information, that belong to the selected food genre 
4.	Click navbar brand logo 'Virtual Cookbook' to return to homepage in readiness to select a different food genre
	
###### •	Footer links tests
- CRUD Operations tested = **READ**
1.	Go to footer section
2.	Click social media icons (LinkedIn & GitHub)
3.	User is passed through to website authors’ actual live pages
4.	Click on 'contact' link
5.	User is passed through to website authors' personal linkedin live page
	
###### •	Other Buttons / Icon functionality tests
*Social Media*
- CRUD Operations tested = **READ**
1.	Scroll to footer
2.	Hover on social media icons
3.	For LinkedIn, colour change from light grey to LinkedIn corporate colour (blue # 0077B5). Inner icon colour changes from black to white
4.	For GitHub, colour change from light grey to GitHub corporate colour (purple # 6e5494). Inner icon colour changes from black to white
5.	Both social media icons contain a fractional timing delay to help user understand icon is active, prior to being clicked 

*Edit Button*
- CRUD Operations tested = **READ & UPDATE**
1.	Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html))page
2.	Hover on edit button and colour chamge fron yellow to green
3.	Click on edit button to take user to edit recipe page

*Delete Button*
- CRUD Operations tested = **READ, UPDATE & DELETE**
1.  Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html)) page
2.	Hover on delete button and colour chamge fron yellow to red
3.	Click on delete button to take user to home page, following deletion of recipe

*Favourites Tickbox*
- CRUD Operations tested = **CREATE, READ & UPDATE**
1.  Navigate to Edit Recipe page &/or Add Recipe page
2.  Click on 'favourite' tickbox to uncheck = No favourite
3.  Click on 'favourite' tickbox to check = favourite
4.  Click 'Confirm' button to complete edit
5.  User will return back to recipe detail page to view their recipe updates 
6.  Navbar counter will increase by +1 for favourite and -1 for non-favourite
7.  Navbar counter will not be less than zero

*Confirm Edit Button*
- CRUD Operations tested = **READ & UPDATE**
1. Navigate to Edit Recipe page
2. Hover on 'Confirm' button and colour chamge fron yellow to green
3. Click on 'Confirm' button to complete edit
4. User will return back to recipe detail page to view their recipe updates 

*Confirm Add Recipe*
- CRUD Operations tested = **READ & UPDATE**
1. Navigate to Add Recipe page
2. Hover on 'Confirm' button and colour chamge from pea green #61892F to lime green #86C232
3. Click on 'Confirm' button to complete add
4. User will return back to home page. New recipe can be viewed upon clicking an appropriate food genre image 

##### Add Recipes
- CRUD Operations tested = **CREATE, READ & UPDATE**
1. Hover on the 'Add Recipe' button in the navbar to show user the button is active
2. Click 'Add Recipe' button
3. User will be presented with a blank recipe template, with placeholder guidance text and required data, containing the following data requests:
    - Food genre - Dropdown box containing Meat, Poultry, Fish, Vegetables, Grains & Pasta options
    - Complexity - Dropdown box containing 'Easy' or 'Challenge'
    - Recipe Name  
    - Authors name
    - Preparation time - Numbers only data entry
    - Cooking time - Numbers only data entry
    - Calories - Numbers only data entry
    - Servings - Numbers only data entry
    - Brief description of the recipe
    - Full list of Ingredients
    - Detailed Instructions on how to cook
    - Recipe image - url web address required from User 
    - Tickbox for favourite recipe. Tick for yes or no tick for no
4.  User must complete all data entry fields. Auto message appears to signal missing data entry 
5.	Click 'Confirm' button for user to formally add their recipe to the application
6.	User is then routed back to homepage
7.	New recipe can be viewed by clicking on food genre image relative to the recipe that has been added 

##### Edit Recipes
- CRUD Operations tested = **READ & UPDATE**
1. Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html)) page
2. Hover on 'Edit' button and colour change fron yellow to green to show the button is active
3. Click on 'Edit' button to complete edit
4. User will be presented with a blank recipe template, containing the following recipe data fields:
    - Food genre - Dropdown box containing Meat, Poultry, Fish, Vegetables, Grains & Pasta options
    - Complexity - Dropdown box containing 'Easy' or 'Challenge'
    - Recipe Name  
    - Authors name
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
7.	Click 'Confirm' button for user to formally edit their recipe in the application
8.	User is then routed back to recipe detail page to view their respective changes

##### Delete Recipes
- CRUD Operations tested = **READ, UPDATE & DELETE**
1. Navigate to [Recipe detail](#detailed-recipe-view-(recipe.html)) page 
2. Hover on 'Delete' button and colour change fron red to green to show the button is active
3. Click on 'Delete' button to complete recipe delete
4. User is then routed back to homepage

##### Recipe Statistics
*Favourites*
- CRUD Operations tested = **READ**
1.  Navigate to [Edit Recipe](#edit-recipes) page &/or [Add Recipe](#add-recipes) page
2.  Click on 'favourite' tickbox to uncheck = No favourite
3.  Click on 'favourite' tickbox to check = favourite
4.  Click 'Confirm' button to complete edit
5.  User will return back to recipe detail page to view their recipe updates 
6.  Navbar counter will increase by +1 for favourite and -1 for non-favourite
7.  Navbar counter will not be less than zero
  
*Recipes*
- CRUD Operations tested = **READ**
1. Complete [adding](#add-recipes) or [deleting](#delete-recipes) of a single recipe
2. Navbar counter will show +1 for adding recipe
3. Navbar counter will show -1 for recipe deletion
4. Navbar counter will not be less than zero

### Code Validation

Code       | Url Link                          | Filename      | Outcome | Comments
-----------|-----------------------------------|---------------|---------|---------
HTML5      |https://validator.w3.org           |base.html      |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |index.html     |Pass     |Jinja templating language used = ok        
HTML5      |https://validator.w3.org           |register.html  |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |meat.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |poultry.html   |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |fish.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |veg.html       |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |grains.html    |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |pasta.html     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |tasks.html     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |recipe.html    |Pass     |HR stray end tag reported,but all ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org           |portfolio.html |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |addrecipe.html |Pass     |Option value empty on dropdown = ok. Jinja templating language used = ok  
HTML5      |https://validator.w3.org           |editrecipe.html|Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org           |404.html       |Pass     |Jinja templating language used = ok
CSS3       |https://jigsaw.w3.org/css-validator|style.css      |Pass     |W3C CSS Validator results - CSS level 3 + SVG - No errors found
Javascript |https://jshint.com/                |index.html     |Pass     |Some instances of $ being undefined due to using jQuery. No errors found    
Javascript |https://jshint.com/                |helper.js      |Pass     |No errors found
Python3    |http://pep8online.com              |recipe.py      |Pass     |All convention errors corrected = ok

### Responsiveness & Rendering
Chrome DevTools together with a selection of mobile, table and desktop devices were relied upon through the entire software development cycle. A key objective was to test both the rendering and responsiveness of the software application against multiple screen resolutions and web browser platforms. Any bugs identified were debugged in real time with special observations noted in a [testing matrix control document](https://github.com/Spagettileg/pbf-third-milestone-project/blob/master/tests/User%20Testing_3rd%20Milestone%20Project_vfinal%20draft.xlsx).

The Virtual Cookbook application has been tested by students from the Slack community, together with friends and family members. Feedback on what worked well and what did not was recorded and suitable corrections to the code were keyed.

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

## Deployment

### Deployment to Heroku
The site has been formally deployed to [Heroku](https://pbf-third-milestone-project.herokuapp.com/) and the latest version of my application can be found here. The following steps were taken in order to deploy:

#### AWS Cloud 9 IDE
- I created a secret_key within .bashrc and heroku so I could still run the project from my own IDE and the security of the password be preserved
- MongoDB Atlas, upon creation of a cluster & database, created a connection string to be copied into both .bashrc and heroku
- Flask debugging turned off by setting debug=False
- Requirements.txt file created with the command `sudo pip3 freeze --local > requirements.txt`. This is essential
- Procfile created withthe command `echo web: python app.py > Procfile`
- Push all my latest production ready code to GitHub ready for deployment via Heroku's GitHub function where you can deploy from GitHub the production ready app

#### Heroku
- From the Heroku dashboard I created a new app, using the name cheers-drinksdb and set the region to Europe
- In the settings tab I clicked reveal config vars and entered the required environment variables, which in this case were:
    - Key = `IP`: Value = `0.0.0.0`
    - Key = `PORT`: Value = `5000`
    - Key = `SECRET`: Value = `************`
    - Key = `MONGO_URI`: Value = `mongodb+srv:\\root:passwordatmyfirstcluster-52qvv.mongodb.net/virtual_cookbook?retryWrites=true&w=majority`
    - On the deploy tab, in the Deployment method section I chose deploy from AWS Cloud 9 IDE via command `git push heroku master`

#### Local Deployment
##### Via GitHub
- Manually download the application locally to your machine and then upload to your preferred IDE
- Install the projects requirements.txt using `pip3 install -r requirements.txt`
- A few environment variables need to be updated before you can run the app:
    - `app.secret_key = os.getenv("SECRET")` 
    - `app.config["MONGO_URI"] = os.getenv("MONGO_URI")`
    - `app.config["MONGO_DBNAME"] = "virtual_cookbook"`
- Once the above steps are complete you can try run the application using `python3 recipe.py`

##### Via the CLI
- Clone my repo via Git using the following command `https://github.com/Spagettileg/pbf-third-milestone-project.git`
- Install the projects requirements.txt using `pip3 install -r requirements.txt`
- A few environment variables need to be updated before you can run the app:
    - `app.secret_key = os.getenv("SECRET")` 
    - `app.config["MONGO_URI"] = os.getenv("MONGO_URI")`
    - `app.config["MONGO_DBNAME"] = "virtual_cookbook"`
- Once the above steps are complete you can try run the application using `python3 recipe.py` 

## Credits

### Content
All code content in this software was written by me, with the expection of the following:
- Reformatting of [Textarea](https://alistapart.com/article/expanding-text-areas-made-elegant/) was supported by code sourced from Neil Jenkins. Under normal circumatances, HTML & CSS are not geared up for responsive formatting of textarea, hence a specialist Javascript code snippet was found and implemented.   
- [User registration](https://www.w3schools.com/howto/howto_js_form_steps.asp) code snippet sourced from W3Schools.com. Additional formatting and creation of required attributes was written by myself.

### Media
- Food genre immages were taken from [pixabay](https://www/pixabay.com), a royalty free stock image library.

- Food recipe image url links were taken from [BBC Good Food Guide](https://www.bbcgoodfood.com/recipes).

- Favicon image was sourced from [pixabay](https://www/pixabay.com).


### Acknowledgements
Theo Despoudis (Mentor) - For his guidance with the process of delivering my project and reminders for keeping the code simple, yet effective. 

Slack Community and the following experts to keep me honest and focused.

Haley Schafer - Tutor,
Niel Mcewen - Tutor &
Michael Park - Tutor

**This is for educational use.** 