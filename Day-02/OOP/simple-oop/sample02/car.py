
# Simple OOP - Obejct Oriented Programming

class Car:
	# define first the initialization which is the __init__
	# functions inside on the class are called methods
	def __init__(self, name, model, color):
		# then we set an attributes that is connected to our methods

		self.name = name
		self.model = model
		self.color = color


	def car_name(self):
		# here, we can return a value of an attributes mentioned on the initialization

		return self.name

	def car_model(self):

		return self.model

	def car_color(self):

		return self.color


class Welcome:

	def welcome(self):

		print("-" * 50)
		print("|" + " " * 17 + "Welcome to cars" + " " * 17 + "|")
		print("-" * 50)



#	can you call the class Welcome with the welcome method using the ff.
#	Welcome().welcome() - one line code
#	wel = Welcome() 	- define a variable first then -
#	wel.welcome() 		- call the given variable name with .welcome()

