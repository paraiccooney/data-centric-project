import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
# Mongo stores it's data in BSON format which is similar to JSON. We use this is the '/edit_task route/<task_id>' route below
# this allows us to convert our task id into bson format
from bson.objectid import ObjectId 



# instance of Flask created
app = Flask(__name__)

# configuration
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://paraiccooney:12345@myfirstcluster-4cfke.mongodb.net/task_manager?retryWrites=true&w=majority'

# instance of PyMongo created
mongo = PyMongo(app)

# / refers to the default route.
@app.route('/')
def my_recipes():
    return render_template("base.html")


# runs the app (instance created above)
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            