from flask import Flask,jsonify,request
from data import data

# CREATE THE API BODY
app = Flask(__name__)

# CREATE THE ROUTE
@app.route("/")

# GIVE THE DATA IN THE API
def index():
    return jsonify({
        "data":data,
        "message":"success"
    }),200

# ADD THE DATA OF A PARTICULAR STAR WHICH IS SEARCHED
@app.route("/star")

def star():
    name = request.args.get("star_names")
    star_data = next(item for item in data if item["star_names"]== name)
    return jsonify({
        "data":star_data,
        "message":"success"
    }),200

# CODE FOR RUNNING THE API
if __name__ == "__main__":
    app.run()
