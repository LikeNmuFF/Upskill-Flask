from house import House

home = House(input("Structure Type? "), input("architectural? "), input("Descriptive?(e.g Interior, Exterior, Setting) ").lower())

print(f"Structure Type: {home.type}")
print(f"architectural: {home.architectural}")
print(f"Descriptive: {home.description_of_house()}")