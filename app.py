import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
# Mongo stores it's data in BSON format which is similar to JSON. We use this is the '/edit_task route/<task_id>' route below
# this allows us to convert our task id into bson format
from bson.objectid import ObjectId 



# instance of Flask created
app = Flask(__name__)

# configuration
app.config["MONGO_DBNAME"] = 'recipe_site'
app.config["MONGO_URI"] = os.getenv("MONGOURI")

# instance of PyMongo created
mongo = PyMongo(app)

# / refers to the default route.
@app.route('/')
def my_recipes():
    return render_template("index.html",recipies=mongo.db.recipes.find())

# route for upload recipe
@app.route('/upload_recipe')
def upload_recipe():
    return render_template('upload.html',
                           categories=mongo.db.recipe_categories.find())

# route for random recipe
@app.route('/saved_recipies')
def saved_recipies():
    return render_template("saved_recipies.html")
    
# route for search
@app.route('/search_recipes')
def search_recipes():
    return render_template("search.html")
    
@app.route('/upload_recipe_button', methods=['POST'])
def upload_recipe_button():
    recipies = mongo.db.recipes
    recipies.insert_one(request.form.to_dict())
    # redirect to my recipies page
    return render_template("index.html",recipies=mongo.db.recipes.find())

# runs the app (instance created above)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            