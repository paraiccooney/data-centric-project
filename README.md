Startup modal credits - https://www.tutorialrepublic.com/faq/how-to-launch-bootstrap-modal-on-page-load.php

interesting bug - to apply two for loops with the recipes dataset on the myrecipes page I had to pass the same data into the render_template 
twice as Jinja only allows an argument to be used once;
return render_template("myrecipes.html", recipes=mongo.db.recipes.find(), username=username, recipes2=mongo.db.recipes.find())
This is also evident in the /browse_recipes route.