#structure type, architectural style, and descriptive attributes

class House:


	def __init__(self, type, architectural, descriptive):
		self.type = type
		self.architectural = architectural
		self.descriptive = descriptive



	def types_of_house(self):

		return f"Type of house is {self.type}"

	def architectural_of_house(self):

		return f"architectural style of house is {self.architectural}"

	def description_of_house(self):

		if self.descriptive == "Exterior" or self.descriptive == "Exteriors":

			return f"Stone walkway leading to a mahogany front door with a brass door knocker - {self.descriptive}"

		elif self.descriptive == "Interior":

			return f"Staircase with white balusters and a dark wood handrail - {self.descriptive}"

		elif self.descriptive == "setting" or self.descriptive == "settings":

			return f"Corner lot in a quiet suburban neighborhood - {self.descriptive}"

		else:

			return self.descriptive