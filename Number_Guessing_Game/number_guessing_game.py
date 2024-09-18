import random
print("Welcome to the Number Guessing Game! ")
print("Try to guess the number between 1 and 100.")
random_number = random.randint(1,100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess:"))
        attempts +=1

        if guess < random_number:
            print("Too low!")
        elif guess> random_number:
            print("Too High!")
        else:
            print(f"Congratulations! you have guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")