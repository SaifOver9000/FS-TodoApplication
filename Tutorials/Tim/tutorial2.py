# We are going to do templates now

from flask import Flask, redirect, url_for, render_template # So what render_template is going to do is grab an html file and render it as our webpage
#####THIS IS THE BASIC FLASK TUTORIAL -TEMPLATES
##We need to create an Html file and put it into a specific directory. --> Has to be named as templates - (1)
## It needs to be in the same directory as your python scripts as well.\
## If we need to display dynamic information() we can pass information from the backend of flask to the fontend, that being the htmltemplate
#So inside the html template, we can use some special expressions that work with flask-- go to the index.html
app = Flask(__name__) 

@app.route("/<name>") 
def home(name):
    # return render_template("index.html")
    # return render_template("index.html", content=name, rew=49) #this will replace the content in the template, with whatever we assign to it.
#to dynamically render information we use this special expression {{}} -- lets us type any variable, information we need to put in the template, example "content"
#So when we define content in this {{}}, what it allows us to do is pass a value that will replace "content" from the backend -- move back to the script
#{{}} this is interpreted as a variable

#how to pass in a list  
    return render_template("index.html", names=["james", "drake", "baby"])
if __name__ == "__main__":
    app.run()