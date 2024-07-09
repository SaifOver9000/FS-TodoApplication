#### SO in this tutorial we will learn about utilizing template inheritance, to avoid duplicating html and other codes
#Essentially we wil be creating a base template that all other of the templates will work off of.
#Also how to add bootstrap to this website

from flask import Flask, render_template, redirect, url_for 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) #Debug = true allows us to not need to rerun the server every time we make a change