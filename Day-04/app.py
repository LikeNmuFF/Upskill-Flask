# =================================================
# Welcome to Day-03 of learning Python and Flask. |
#  Routing and URL Rules and Methods              |
# =================================================

#=====================================================================================================
# Step 1 – Add a simple new route
# Add a second route to your existing app.py that responds to /about and
# returns a simple welcome message — just prove to yourself that one app can have multiple routes.
#=====================================================================================================
#=====================================================================================================
# Step 2 – Add a dynamic route with a string converter
# Create a route that accepts a name in the URL itself, like /user/john or /user/maria — 
# the name should come from the URL, not hardcoded inside the function.
#=====================================================================================================
#=====================================================================================================
# Step 3 – int converter
# You did /user/<name> for a string — for an integer, the syntax is almost the same but you add 
# the type before the variable name inside the angle brackets, like <type:variable>. 
# Ask yourself what type keyword Flask uses for whole numbers.
#=====================================================================================================
from flask import Flask, url_for, redirect # we are importing the flask module so that we can work with flask

app = Flask(__name__) # variable is a special built-in variable that stores the name of 
					  # the current module or script being executed.
@app.route("/") 	  #  # this decorator tells Flask to call index() when the "/" URL is visited
def index():		  # defining a function of specific route to easily understand
	return("Welcome to Flask!") # returning a value that will shows in the web page

@app.route("/about", methods=["GET", "POST"]) # This is the about route that if the user/client go the this url, with a methods of posting and getting data
def about():							   # Defining a function that is understandable so that even in code it get ez to undestand
	return "Welcome to About"			   # It will display to them the returned string value which is the "Welcome ..."

@app.route("/user/<name>")  			   # This part is the Step 2 where if you visit the user/<with your name> it show the page else you will got error 404
def user(name):							   # this function use the name parameter so that it can communicate to the route who is using the name placeholder
	return f"Hi {name}"					   # This will print out if you visit the /user/your_name and out put with Hi your_name

@app.route("/post/<int:number>")		   # This have the same idea on line 34, but instead of handling a string, this hadle an integers on the placeholder
def post(number):						   # the same explanation on the "def user(name):""		
	return f"The value you input is {number}" # This will print out if you visit the /post/ and add any number then it print out the "The value you input is "the number you input"

@app.route("/step4")
def step4():
	return redirect(url_for("about"))	   # This is using the url_for  from flask returning a url value that says the URL of the about on the line 30. output should be /about
										   # url_for is the ingredient — it produces the URL.
										   # redirect is the container — it uses that URL to send the user somewhere.

if __name__ == "__main__": # This indicates that if module name is equal to the main file then it can execute the file
	app.run(debug=True)    # and run it you can run it in specifi port like port="5000" or what you prefered, and the default port is 5000

