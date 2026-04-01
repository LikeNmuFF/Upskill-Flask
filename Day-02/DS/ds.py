import random # Used to generate random selections

cars = ["Mustang", "Ferrari", "Civic", "Bugatti", "Lamborgini"] # List of available car names

car = random.choice(cars) # Randomly selects one car from the list

attempts = 5 # Total number of guesses allowed for the player

cache = [] # Stores revealed characters (currently storing the selected car)

cache.append(car) # Adds the selected car into cache (used for matching characters)

while attempts > 0: # Loop runs while the player still has remaining attempts

	masked = "" # Stores the masked version of the selected car (hidden letters)

	for x in car: # Iterate through each character in the selected car name

		if x in cache: # Check if the character exists in cache (revealed)

			masked += x # Show the character if it is in cache

		else:

			masked += "*" # Hide the character if it is not in cache
		
	print(masked) # Display the masked car name to the player

	client = input("Guess the Car: ") # Ask the player to guess the car name

	if client == car: # Check if the guess is correct

		print(f"You guess the Car {car}") # Display success message

		exit() # Exit the program when the player wins

	elif client != car: # If the guess is incorrect

		attempts -= 1 # Reduce remaining attempts by 1

		print(f"Remaining attemps {attempts}") # Show remaining attempts

		if attempts <= 0: # Check if no attempts are left

			print("You Loss!") # Display losing message