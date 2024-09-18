# Function Definitions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    # Handling division by zero
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

def modulus(a, b):
    # Handling modulus by zero
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    else:
        return a % b

# Main Program
print("This is a simple calculator using Python. Please select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")


operation = input("Enter choice (1/2/3/4/5): ")

# Taking input for numbers and handling potential errors
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

if operation == "1":
    print(f"Addition: {num1} + {num2} = {addition(num1, num2)}")

elif operation == "2":
    print(f"Subtraction: {num1} - {num2} = {subtraction(num1, num2)}")

elif operation == "3":
    print(f"Multiplication: {num1} * {num2} = {multiplication(num1, num2)}")

elif operation == "4":
    result = division(num1, num2)
    if isinstance(result, str):
        print(result)  # Display error message if division by zero
    else:
        print(f"Division: {num1} / {num2} = {result:.2f}")

elif operation == "5":
    result = modulus(num1, num2)
    if isinstance(result, str):
        print(result)  # Display error message if modulus by zero
    else:
        print(f"Modulus: {num1} % {num2} = {result}")

else:
    print("Error: Invalid operation choice.")
