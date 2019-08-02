import os
from flask import Flask, redirect, render_template, request, session, url_for
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
    """Main page with instructions"""
    if request.method == "POST":
        print(request.form["username"])
        session["username"] = request.form["username"]
        
    # if username has been submitted then return the below page (url_for redirects to the function name as opposed to the @app.route)
    if "username" in session:
        print(session)
        return redirect(url_for("my_recipes"))
        
    # if username has not been submitted index.html will be rendered
    return render_template("index.html")


@app.route("/recipes", methods=["GET", "POST"])
def my_recipes():
    username = session["username"]
    return render_template("myrecipes.html", username=username)




# route for upload recipe
@app.route('/upload_recipe')
def upload_recipe():
    return render_template('upload.html',
                           categories=mongo.db.recipe_categories.find())

# route for random recipe
@app.route('/saved_recipes')
def saved_recipes():
    return render_template("saved_recipes.html")
    
# route for search
@app.route('/search_recipes')
def search_recipes():
    return render_template("search.html")
    
@app.route('/upload_recipe_button', methods=['POST'])
def upload_recipe_button():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    # redirect to my recipes page
    return render_template("index.html",recipes=mongo.db.recipes.find())



# runs the app (instance created above)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            