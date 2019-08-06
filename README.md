Startup modal credits - https://www.tutorialrepublic.com/faq/how-to-launch-bootstrap-modal-on-page-load.php

interesting bug - to apply two for loops with the recipes dataset on the myrecipes page I had to pass the same data into the render_template 
twice as Jinja only allows an argument to be used once;
return render_template("myrecipes.html", recipes=mongo.db.recipes.find(), username=username, recipes2=mongo.db.recipes.find())
This is also evident in the /browse_recipes route.

# Data Driven Recipe Site
This is an interactive website with both front-end & back-end functionality.  It constitutes the third of my four projects which form the assessment 
basis of my Full-Stack Web Development course with The Code Institute.
The purpose of this project is to allow users to interact with a back-end database of recipes using an appealing & intuative front-end.  The site allows
users to upload & save their own recipes while also searching & browsing recipes submitted by others & bookmarking them for later recall.

## Demo
TO BE COMPLETED

## UX
The design goal of this project was to make the front-end as appealing & intuatively interactive as possible while also providing a warm colourful 
display which serves to stimulate the users senses.  An orange theme was choosen along with a visually rich backround image of fresh ingredients along
with a linen background image to add a rustic feel.

For the site administator I also wanted to be able to give them the ability to integrate promoted recipes (which serve as the revenue stream for the site)
without taking away from the user-generated feel & rendering the site overly-commercial.  To do so I incorporated a promoted recipe carousel in the 
browse section & also included a random promoted recipe underneath any search results.

## Technologies Used
1. HTML
2. CSS
3. Bootstrap
4. Materialize
5. Javascript
6. jQuery
7. Python
8. Flask
9. Jinja2
9. MongoDB

## Features
**Feature 1 - Recipe Page**
The My Recipes page (which can be accessed from the button in the nav of the same name or by clicking the site logo in the center of the nav) utilises
the jinja templating language to loop through & render each recipe written by the user.  It does so by passing in all recipes as an argument when
rendering the url & then, through use of a jinja if statement rendering only those recipes who's author matches that of the username entered at the 
start of the session.
The page then uses the same method to render all recipes which the user has bookmarker by checking if the bookmarkers field contains the substring
matching the username.

**Feature 2 - Browse Functionality**
**Feature 3 - Upload Recipe Functionality**
**Feature 3 - Search Functionality**
**Feature - Bookmark add/remove buttons**
**Feature - Delete buttons**


