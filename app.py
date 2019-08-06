import os
from flask import Flask, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 



# instance of Flask created
app = Flask(__name__)

# configuration
app.config["MONGO_DBNAME"] = 'recipe_site'
app.config["MONGO_URI"] = os.getenv("MONGOURI")

# instance of PyMongo created
mongo = PyMongo(app)
app.secret_key = "randomstring123"

    
@app.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        print(request.form["username"])
        session["username"] = request.form["username"]
        
    # if username has been submitted then return the below page
    if "username" in session:
        return redirect(url_for("my_recipes"))
        
    # if username has not been submitted index.html will be rendered
    return render_template("index.html")

# MY RECIPES ROUTE
@app.route("/recipes", methods=["GET", "POST"])
def my_recipes():
    username = session["username"]
    return render_template("myrecipes.html", recipes=mongo.db.recipes.find(), username=username, recipes2=mongo.db.recipes.find())


# UPLOAD RECIPES PAGE ROUTE
@app.route('/upload_recipe')
def upload_recipe():
    username = session["username"]
    return render_template('upload.html',
                           categories=mongo.db.recipe_categories.find(), username=username)

# UPLOAD RECIPE ROUTE    
@app.route('/upload_recipe_button', methods=['POST'])
def upload_recipe_button():
    username = session["username"]
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    # redirect to my recipes page
    return redirect(url_for("my_recipes"))
    
# SEARCH RESULTS ROUTE    
@app.route('/search_recipes', methods=['POST'])
def search_recipes_button():
    username = session["username"]
    search_param = request.form.get('search_param')
    search_input = request.form.get('search_input')
    recipes=mongo.db.recipes.find({search_param : {'$regex' : ".*"+search_input+".*"}})
    return render_template("search_results.html", recipes=recipes)


# BROWSE RECIPES ROUTE
@app.route('/browse_recipes')
def browse_recipes():
    return render_template("browse.html", recipes=mongo.db.recipes.find(), recipes2=mongo.db.recipes.find(), recipes3=mongo.db.recipes.find(),
    recipes4=mongo.db.recipes.find(), recipes5=mongo.db.recipes.find(), recipes6=mongo.db.recipes.find(), recipes7=mongo.db.recipes.find(),
    recipes8=mongo.db.recipes.find(), recipes9=mongo.db.recipes.find(), recipes10=mongo.db.recipes.find(), recipes11=mongo.db.recipes.find(),
    recipes12=mongo.db.recipes.find(), recipes13=mongo.db.recipes.find(), recipes14=mongo.db.recipes.find(), recipes15=mongo.db.recipes.find(),
    recipes16=mongo.db.recipes.find(),recipes17=mongo.db.recipes.find())
 
   
# DISPLAY RECIPE FROM CAROUSEL ROUTE
@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    return render_template("display_recipe.html", recipes=mongo.db.recipes.find())


# SEARCH ROUTE
@app.route('/search_recipes')
def search_recipes():
    username = session["username"]
    return render_template("search.html", recipes=mongo.db.recipes.find(), username=username)
    

# BOOKMARK-BUTTON ROUTE
@app.route('/bookmarked')
def bookmark_recipe_button(recipe):
    # recipe_id = request.form.get('recipe_id')
    username = session["username"]
    recipes = mongo.db.recipes
    recipes.update({'_id' : ObjectId("5d40663d1c9d440000c0a680")},
    {'$push' : { 'bookmarkers': ('username')}})
    return render_template("display_recipe.html", recipes=mongo.db.recipes.find())


# runs the app (instance created above)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            