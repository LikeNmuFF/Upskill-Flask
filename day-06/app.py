# ==========================================
# Welcome to Day 06 of learning Flask      #
# Today you'll learn about:                #
# /static, request.form, GET/POST, redirect#
# ==========================================#
# CHALLENGE & LEARNING
# Your mental roadmap before touching anything:
#
# static/ — Flask has a special folder for static files like CSS and images.
# Question: Why can't you just put a CSS file anywhere and link to it normally?
#
# request.form — When a user fills out a form and clicks submit, the data needs to go somewhere.
# Question: How does Flask receive what the user typed?
#
# GET vs POST — You already know routes can have methods, but today it becomes practical.
# Question: What is the actual difference between GET and POST in terms of where the data travels?
#
# redirect — You already know this from Day 04 and 05, but today you'll use it more practically.
# Question: Why would you redirect after a form submission instead of just returning a page directly?

from flask import (
	Flask,
	request,
	url_for,
	render_template,
	redirect
)
app = Flask(__name__)


#========================================#
# Home route that renders the index page
@app.route('/')
def home():
	return render_template('index.html')

#===========================#
# Custom 404 error handler
@app.errorhandler(404)
def error404(e):
	return f"""<h1>You are on the wrong path</h1>
			<h2>back to the root path <a href='/'>link</a></h2>"""

#=============================================================#
# Handle form submission - accepts both GET and POST requests
@app.route('/submit', methods=['GET', 'POST'])
def submit():
	if request.method == 'POST':
		#===============================================#
		# Get the user_name from the submitted form data
		name = request.form['user_name']

		#===============================================#
		# Redirect to the user_submit page with the name
		return redirect(url_for('user_submit', usr_name = name))
	else:

		#==================================================#
		# If it's a GET request, just render the index page
		return render_template('index.html')

#================================================#
# Display a greeting for the submitted user name
@app.route('/submit/<usr_name>')
def user_submit(usr_name):
	return f"<h1> Hi {usr_name}</h1>"




if __name__ == "__main__":
	app.run(debug=True)