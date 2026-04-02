# =================================================
# Welcome to Day-03 of learning Python and Flask. |
# Today we are getting forward to know the basics |
# =================================================
# Flask Install & First App - Day03
# flask install -- for installing flask, in terminal we need to type "pip install flask"
# app.py 		-- this will be the name of our filename
# run server	-- running the server should we use the "python app.py or flask app.py"
# debug			-- this will need to see the error of are app we are currently making

from flask import Flask # we are importing the flask module so that we can work with flask

app = Flask(__name__) # variable is a special built-in variable that stores the name of 
					  # the current module or script being executed.
@app.route("/") 	  #  # this decorator tells Flask to call index() when the "/" URL is visited
def index():		  # defining a function of specific route to easily understand
	return("Welcome to Flask!") # returning a value that will shows in the web page





if __name__ == "__main__": # This indicates that if module name is equal to the main file then it can execute the file
	app.run(debug=True)    # and run it you can run it in specifi port like port="5000" or what you prefered, and the default port is 5000

