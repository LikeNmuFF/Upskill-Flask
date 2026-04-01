# Class Variables - class variables is define or created outside the methods

class Students:

	total_students = 0
	graduation_year = 2028

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
		Students.total_students += 1


student1 = Students("Klein Ric", 21, "Male")
student2 = Students("Erica Joy", 20, "Female")


print(f"The Graduation year is on {Students.graduation_year} and a total of {Students.total_students} students")
print("-" * 60)
print("1." + student1.name, student1.age, student1.gender)
print("2." + student2.name, student2.age, student2.gender)
print("-" * 60)