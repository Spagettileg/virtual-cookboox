# 3rd Milestone Project | Virtual Cookbook
Data-Centric Development - Code Institute 

This is my portfolio website to present to prospective employers. The portfolio highlights six projects that cover a range of technologies, as well as including a bit about myself, my coding skills, and a contact form. As I am bilingual, it has both an English and a French version.


## Demo
A live demo can be found [here](https://pbf-third-milestone-project.herokuapp.com/).

## Navigate to detail

## UX
My goal in the design was to make it as easy as possible to access information on the site while striving for a minimalist design. The greyscale color scheme was chosen to create a sleek and modern feel. 

For employers, I wanted to provide them with a brief overview of myself and my capabilities via a user friendly design. This way, they would be able to get a glimpse of who I am, my background, work I've done, and my skills, with the option to contact me if they choose. In the 'Work/Travail' section, I wanted them to be able to quickly access work that I've done, providing a short summary of the project and main technologies with a link to each GitHub Repository and live demo. A link to my LinkedIn profile, my GitHub, and a downloadable PDF version of my CV were also provided for their ease of access. 

## Wireframes

## User Stories

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
This site uses the scrollSpy feature in Bootstrap with an extra JavaScript function added to create a 'smooth scrolling' effect. The navbar also stays collapsed regardless of the screen size to promote a minimalist design.

### Features Left to Implement
In the future, I would like to add further projects that I've worked on to create a more comprehensive 'work/travail' section. I would like to also add animations to the progress circles in the "skills/compétences" section to animate on a hover. 

`Puddings & Deserts recipes....`

## Testing

### Introduction
The employer and recruiter user story achieved the intended outcome of providing them with a showcase of myself and my work. In the about me section, they can read a bit about my background, and if they're viewing on a desktop, the background of this section is a photo of me. They are able to see my showcased projects via the project cards in the "Work" section. They can view both the live version and the GitHub repository by clicking on the Font Awesome icons. They are also able to view my social media profiles via clicking on the icons in the footer. They are also able to download my CV by either clicking on CV in the navbar dropdown, or by clicking on the document icon in the footer. 

If you try to submit the contact form with an invalid email address, there will be an error noting the invalid email address. Furthermore, the 'required' attribute is added to the 'name,' 'email,' and 'message' fields, so if those fields are not filled in, the form will not submit. If all field are valid, the page will reload. If an employer or recruiter is interested in contacting me, they will have to fill out all fields in order for the form to go through.

All links will open in a new tab using 'target="_blank"' and the CV will download to your default folder for downloads on click using the 'download' attribute. All links have been manually tested to ensure that they are pointing to the correct destination.

By clicking on the links in the navbar, the scrollSpy effect will work regardless of whether or not you're viewing the sections in the same order they are listed in the dropdown navbar. 

This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox) and on multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness. During the testing phase, I realized that ```background-attachment: fixed``` was not compatible with iOS browsers. On Chrome and Safari in iOS, the background photos appeared zoomed-in and blurry. To fix this, the ```background-attachment: scroll``` property value was added in a media query.

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