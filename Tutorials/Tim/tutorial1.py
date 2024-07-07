from flask import Flask, redirect, url_for #how to redirect, 
#####THIS IS THE BASIC FLASK TUTORIAL
app = Flask(__name__) #Create an instance of flask

#Define how we are going to access this specific page, right now flask doesnt know where we should be gpoing to get to the page 
# So we need to define the route

@app.route("/") # inside the parenthesis the path we need to follow to reach the route

#define the pages of the website
# the function returns what will be displayed on the page
def home():
    return '<h1>Hello World</h1>'

@app.route("/<name>") # If I write anything inbetween tags like these, It will grab the stuff and pass it into the parameter below
def user(name):
    return f"Hello {name}!"

#using / after and before allows us to acces the page regardless of whether there is a / in the end or not
@app.route("/admin/") # so if the user types in the url for a page that they donot have access to, for example that being the admin page.
def admin(): #using the redirect and url_for function we can redirect them bback to where theya are authorised
    return redirect(url_for("user", name = "Admin!"))
#how can we redirect to a specific url, you type the name of the parameter and  = what ever you want to pass through

# so what is going to happen, when we go to the admin page, it is going to return the url for user and pass through the arguement Admin!
if __name__ == "__main__":
    app.run()