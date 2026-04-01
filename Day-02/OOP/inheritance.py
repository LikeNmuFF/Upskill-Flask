# Inheritance - Allows a class to inherit attributes and methods from another class
#				helps with the code reusability and flexibility class Child(Parent)
# For the example we use the Animal


class Animal:

	def __init__(self, name):

		self.name = name
		self.alive = True

	def eat(self):

		print(f"{self.name} is eating")

	def sleep(self):

		print(f"{self.name} is sleeping")

class Dog(Animal):

	def sound():
		print("Arf Arf")

class Cat(Animal):

	def sound():
		print("meow meow")

class Bird(Animal):
	def sound():
		print("tweet tweet")

print("-" * 50)
print("|" + " " * 14 +"WELCOME TO INHERITANCE" + " " * 14 + "|")
print("-" * 50)
# DOG 
print("-" * 50)
print("DOG - Area")
print()
dog = Dog("Scooby")
print(f"Name of dog is: {dog.name}")
dog.sleep()
dog.eat()
Dog.sound()
# CAT
print("-" * 50)
print("CAT - Area")
print()
cat = Cat("Garfield")
print(f"Name of cat is: {cat.name}")
cat.eat()
cat.sleep()
Cat.sound()

#BIRD
print("-" * 50)
print("BIRD - Area")
print()
bird = Bird("Parrot")
print(f"Name of the bird is: {bird.name}")
bird.eat()
bird.sleep()
Bird.sound()