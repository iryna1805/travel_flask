from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    url = "https://http.cat/images/"
    items = [f"{url}{x}.jpg" for x in [101, 404, 500, 412]]
    return render_template("index.html", items=items)