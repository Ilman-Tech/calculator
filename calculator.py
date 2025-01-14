# Function to add two numbers
def add_number(a, b):
    return a + b

# Function to subtract the second number from the first number
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide the first number by the second number
# Returns an error message if the second number is zero
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

# Main loop to keep the calculator running until the user exits
while True:
    # Display the available operations to the user
    print("\nChoose an operation:")
    print("1. + (Addition)")
    print("2. - (Subtraction)")
    print("3. * (Multiplication)")
    print("4. / (Division)")
    print("5. Exit")
    
    # Get the user's operation choice
    operation = input("Enter your operation (1/2/3/4/5): ")

    # Exit the program if the user chooses '5'
    if operation == '5':
        print("Goodbye!")
        break

    # Check if the user has selected a valid operation
    if operation not in ['1', '2', '3', '4']:
        print("Invalid selection! Please choose a valid operation.")
        continue

    # Get two numbers from the user, ensuring they are valid numeric inputs
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    # Perform the chosen operation
    if operation == '1':
        result = add_number(a, b)
    elif operation == '2':
        result = subtract(a, b)
    elif operation == '3':
        result = multiply(a, b)
    elif operation == '4':
        result = divide(a, b)
        
    # Display the result of the operation
    print("The result is:", result)

    # Ask the user if they want to calculate again
    repeat = input("Do you want to calculate again (yes/no)? ").lower()

    # If the user does not want to continue, exit the program
    if repeat != 'yes':
        print("Goodbye!")
        break
