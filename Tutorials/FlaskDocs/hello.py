from flask import Flask # Import the Flask class from the flask module

app = Flask(__name__) # Create an instance of the Flask class called "app"

@app.route('/') # Use the route() decorator to tell Flask what URL should trigger our function
def hello_world(): # Define a function that returns the string "Hello, World!"
        return 'Hello, World!'
    
