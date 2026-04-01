from car import Car, Welcome


Welcome().welcome()

car = Car(input("What Name: "), int(input("What model: ")), input("What color: "))

print(car.car_name())
print(car.car_model())
print(car.car_color())