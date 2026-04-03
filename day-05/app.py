# ============================================================
# Welcome to Day-05 of learning Python and Flask.			 |
#  Jinja Templates, Render_Templates, Loops, Extends, Filters|
# ============================================================
# render_template — instead of returning a string, you return an HTML file that lives in a special folder. 
# Ask yourself — what folder does Flask expect your HTML files to live in by default?
# {{ }} — this is how Jinja2 says "put a Python value here inside the HTML" 
# — think of it as a placeholder that gets replaced with real data.
# loops — Jinja2 lets you loop inside HTML, so if you have a list in Python, you can repeat HTML elements for each item 
# — ask yourself what keyword starts a loop in Jinja2 and how does it know where the loop ends?
# filters — these are modifiers you apply to a value inside {{ }} using a pipe | symbol 
# — like making text uppercase or limiting a string length.
# extends — this is template inheritance, meaning one HTML file can act as the base layout and other pages just fill in the gaps 
# — so you don't repeat your header and footer on every page

from flask import Flask, render_template, url_for, redirect 
# Newly import modules from flask
# render_template are used to render html files
# url_for used to know the specific url of the path
# redirect is used where if you visit something then you get redirect to another page

app = Flask(__name__) 


@app.route("/<name>") # if the users visite on the url/name it will redirect rendered on the html file
def home(name):		  # Defining as home and adding a parameter "name"
	items = ["Flask", "Jinja2", "Rendering Templates"]
	hello = "Welcome to flask!" # Welcome message that redered insind html file
	return render_template("index.html",hello = hello, name = name, items = items) # If the user go with url/name then,
	# they will go to the index.html and display on the index.html the hello varible who handles the Welcome to flask!, and,
	# it will display the name you put on the url/name and also it will display the list.


#this part is something we learn on the Day-04
@app.route("/about")
def about():
	return redirect(url_for("home", name = "klein"))




if __name__ == "__main__":
	app.run(debug=True)