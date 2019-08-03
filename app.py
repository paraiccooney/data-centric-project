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
    
"""    
# / refers to the default route.
@app.route('/')
def welcome_page():
    return render_template("index.html")


#route for my recipes
@app.route('/my_recipes', methods=["GET", "POST"])
def my_recipes(username):
    username=username;
    return render_template("myrecipes.html",recipes=mongo.db.recipes.find(), username=username)"""
    
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


@app.route("/recipes", methods=["GET", "POST"])
def my_recipes():
    username = session["username"]
    return render_template("myrecipes.html", recipes=mongo.db.recipes.find(), username=username)




# route for upload recipe
@app.route('/upload_recipe')
def upload_recipe():
    username = session["username"]
    return render_template('upload.html',
                           categories=mongo.db.recipe_categories.find(), username=username)

# route for bookmarked recipes
@app.route('/saved_recipes')
def saved_recipes():
    return render_template("saved_recipes.html")
    
@app.route('/upload_recipe_button', methods=['POST'])
def upload_recipe_button():
    username = session["username"]
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    # redirect to my recipes page
    return redirect(url_for("my_recipes"))


# route for search
@app.route('/search_recipes')
def search_recipes():
    username = session["username"]
    return render_template("search.html", recipes=mongo.db.recipes.find(), username=username)
    

# route for bookmarked
@app.route('/bookmarked', methods=['POST'])
def bookmark_recipe_button(recipe_id):
    username = session["username"]
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'bookmarkers': username
    })




# runs the app (instance created above)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            