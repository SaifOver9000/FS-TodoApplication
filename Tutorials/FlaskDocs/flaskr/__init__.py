import os
from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__,instance_relative_config=True) # __name__ is the name of the current Python module. The instance_relative_config=True tells the app that configuration files are relative to the instance folder. The instance folder is located outside the flaskr package and can hold local data that shouldn't be committed to version control, such as configuration secrets and the database file.
    
    app.config.from_mapping(
        SECRET_KEY='dev', # SECRET_KEY
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'), # DATABASE 
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        