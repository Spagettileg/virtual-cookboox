# 3rd Milestone Project | Virtual Cookbook
###### Data-Centric Development - Code Institute 

Virtual Cookbook has been designed for people of all cooking capabilities to help produce delicious and wholesome meals. This application provides quick and intuitive access to recipes borne out of selected food genres.

If you are struggling for time to cook, notice on preparation and cooking time is made clear. Diet conscious consumers can view the calories per serving numbers to help plan for the right recipe.

Finally, you can add new recipes to this application by simply clicking on 'Add Recipe' at the top of the screen. Favourite recipes can be recorded, existing recipes can be edited and unwanted recipes can be deleted. All at the users fingertips.


## Demo
A live demo can be found [here](https://pbf-third-milestone-project.herokuapp.com/).

## Navigate to detail
***TBC***

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

## User Stories
> I need an app that provides quick and intuitive access to recipes across the globe

> I don’t have much time for cooking in the week, so I need to understand time taken to cook quality meals

> Some of my friends are worried about calory content in their food. I need to understand calory content per recipe serving

> I'd like to upload new recipes and contribute to existing recipes, to share my love and passion for good, wholesome eating

## Design, including Schema

## Database & Source Data

## Virtual Cookbook - Summary Functions

## Technologies Applied

### Languages
1. HTML
2. CSS
3. Bootstrap (3.3.7)

### Libraries

### Tools

### Hosting

## Features

### Features Left to Implement

`Puddings & Deserts recipes....`

## Testing

### Introduction

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
    - Key = IP, Value = 0.0.0.0
    - Key = PORT, Value = 5000
    - Key = SECRET, Value = ************
    - Key = MONGO_URI, Value = mongodb+srv:\\root:passwordatmyfirstcluster-52qvv.mongodb.net/virtual_cookbook?retryWrites=true&w=majority
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