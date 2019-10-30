import os
import random
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
    recipes=mongo.db.recipes
    username = session["username"]
    bookmark_tag= username+'-bookmark'
    bookmarked=list(mongo.db.recipes.find({username+'-bookmark' : 'on' }))
    authored=list(mongo.db.recipes.find({'author' : username }))
    allRecipes= recipes.find()
    
    # if statement to display page based on present of authored & bookmarked recipes
    # if there's no authored or bookmarked recipes
    if authored and bookmarked: 
        return render_template("myrecipes.html", authored=recipes.find({'author': username}), username=username, recipes2=mongo.db.recipes.find({username+'-bookmark' : 'on' }), 
        bookmark_tag=bookmark_tag)
    
    # if there's authored but no bookmarked
    elif authored:
        return render_template("no_bookmarks.html", recipes=recipes.find({'author': username}), username=username)
    
    # if there's bookmarked but no authored
    elif bookmarked:
        return render_template("no_authored.html", recipes=recipes.find({username+'-bookmark' : 'on' }), username=username, bookmark_tag=bookmark_tag)
    
    else:
        return render_template("no_recipes.html", username=username)


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
    #number must be a string to be passed into database
    random_number=str(random.randrange(1,6))
    search_param = request.form.get('search_param')
    search_input = request.form.get('search_input')
    search_results=mongo.db.recipes.find({search_param : {'$regex' : ".*"+search_input+".*"}})
    search_list = list(mongo.db.recipes.find({search_param : {'$regex' : ".*"+search_input+".*"}}))
    promoted_recipes=mongo.db.recipes.find({'promoted_key' : random_number })
    if search_list:
        print("search successful")
        return render_template("search_results.html", recipes=search_results, promoted_recipes=promoted_recipes)
    else:
        print("no results")
        return render_template("no_results.html", promoted_recipes=promoted_recipes)

# BROWSE RECIPES ROUTE
@app.route('/browse_recipes')
def browse_recipes():
    return render_template("browse.html", recipes=mongo.db.recipes.find(), recipes2=mongo.db.recipes.find(), recipes3=mongo.db.recipes.find(),
    recipes4=mongo.db.recipes.find(), recipes5=mongo.db.recipes.find(), recipes6=mongo.db.recipes.find(), recipes7=mongo.db.recipes.find(),
    recipes8=mongo.db.recipes.find(), recipes9=mongo.db.recipes.find(), recipes10=mongo.db.recipes.find(), recipes11=mongo.db.recipes.find(),
    recipes12=mongo.db.recipes.find(), recipes13=mongo.db.recipes.find(), recipes14=mongo.db.recipes.find(), recipes15=mongo.db.recipes.find(),
    recipes16=mongo.db.recipes.find(),recipes17=mongo.db.recipes.find(),recipes18=mongo.db.recipes.find())
 
   
# DISPLAY RECIPE FROM CAROUSEL ROUTE
@app.route('/display_recipe/<recipe_id>')
def display_recipe(recipe_id):
    return render_template("display_recipe.html", recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


# SEARCH ROUTE
@app.route('/search_recipes')
def search_recipes():
    username = session["username"]
    return render_template("search.html", recipes=mongo.db.recipes.find(), username=username)
    

# BOOKMARK BUTTON ROUTE
@app.route('/bookmarked/<recipe_name>')
def bookmark_recipe_button(recipe_name):
    username=session["username"]
    bookmark_tag= username+"-bookmark"
    recipes = mongo.db.recipes
    recipe = recipes.update({"recipe_name": recipe_name}, {'$set': {bookmark_tag: "on"}})
    
    return redirect(url_for("my_recipes")) 
    
# REMOVE BOOKMARK ROUTE
@app.route('/bookmarkremoved/<recipe_name>')
def remove_bookmark_button(recipe_name):
    username=session["username"]
    bookmark_tag= username+"-bookmark"
    recipes = mongo.db.recipes
    recipe = recipes.update({"recipe_name": recipe_name}, {'$set': {bookmark_tag: "off"}})
    
    return redirect(url_for("my_recipes"))

# DELETE-BUTTON ROUTE
@app.route('/deleted/<recipe_name>')
def delete_recipe_button(recipe_name):
    username = session["username"]
    recipes = mongo.db.recipes
    recipes.remove({'recipe_name': recipe_name})
    return redirect(url_for("my_recipes"))


# runs the app (instance created above)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
            