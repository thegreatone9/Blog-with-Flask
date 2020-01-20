from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #__name__ is a module...enables finding templates and static files. app is an instance of Flask.

app.config['SQLALCHEMY_DATABASE_URI'] = ''
posts = [
            {
                'author':'Musa Shakib',
                'title':'Post One',
                'content':'And so we shall go to war.',
                'date_posted':'18th Dec, 2019'
            },
            {
                'author':'Musa Shakib',
                'title':'Post Two',
                'content':'This is a war of attrition.',
                'date_posted':'19th Dec, 2019'
            }

        ]
@app.route("/") #routes are what we type in our browser to go to different pages. e.g. about pages in a website. these are navigated to using route decorators. here the forward slash is simply the root page which will return the output of the following function:

def hello():
    return "<h1>MY PAGE</h1>" # now we need to set our environment variable to this file, so go to command line in the same dir as this file and do that using >> export FLASK_APP=flaskblog.py
    

@app.route("/home")
def home():
    return render_template('home.html', posts = posts) 

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form")
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
