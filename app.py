from flask import Flask, render_template
from datetime import date


app = Flask(__name__)

@app.route("/")
def home():
    my_date = date.today()
    return render_template("index.html")


if __name__ =="__main__":
    app.run(debug=True, port=8080)