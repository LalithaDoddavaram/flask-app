from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__, template_folder="templates")

client = MongoClient('mongodb+srv://doddavaramsn27:fbaj1zCmrRBQCtxM@cluster0.howrb.mongodb.net/')
db = client['sample']
collection = db['movies']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        movie = request.form.get("movie")
        actor = request.form.get("actor")
        director = request.form.get("director")
        year = request.form.get("year")

        collection.insert_one({
            "movie": movie,
            "actor": actor,
            "director": director,
            "year": year
        })

        return render_template("result.html", details=list(collection.find({}, {"_id": 0})))
if __name__ == "__main__":
    app.run(debug=True)
    
