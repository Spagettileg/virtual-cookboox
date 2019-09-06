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

Code       | Url Link               | Filename      | Outcome | Comments
-----------|------------------------|---------------|---------|---------
HTML5      |https://validator.w3.org|base.html      |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org|index.html     |Pass     |Jinja templating language used = ok        
HTML5      |https://validator.w3.org|register.html  |Pass     |Style attribute for background-image used = ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org|meat.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|poultry.html   |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|fish.html      |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|veg.html       |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|grains.html    |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|pasta.html     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|tasks.html     |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|recipe.html    |Pass     |<HR> stray end tag reported,but all ok. Jinja templating language used = ok
HTML5      |https://validator.w3.org|portfolio.html |Pass     |Jinja templating language used = ok
HTML5      |https://validator.w3.org|addrecipe.html |Pass     |Option value empty on dropdown = ok. Jinja templating language used = ok  
HTML5      |https://validator.w3.org|editrecipe.html|
HTML5      |https://validator.w3.org|404.html       |
CSS3       |
Javascript |
Python3    |

### Responsiveness & Rendering

## Browser Compatability

## Deployment
This site is hosted using GitHub pages, deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch. In order for the site to deploy correctly on GitHub pages, the landing page must be named `index.html`.

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/hschafer2017/HSCHAFER-Portfolio.git` into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.


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