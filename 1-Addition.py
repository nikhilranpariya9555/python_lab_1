# Define a function to perform the calculations
def calculate_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Division by zero is not allowed"
    
    return addition, subtraction, multiplication, division

# Main block to take user input and display results
if __name__ == "__main__":
    try:
        # Take user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform calculations
        add, sub, mul, div = calculate_operations(num1, num2)

        # Display results
        print("Addition: {} + {} = {}".format(num1, num2, add))
        print("Subtraction: {} - {} = {}".format(num1, num2, sub))
        print("Multiplication: {} * {} = {}".format(num1, num2, mul))
        print("Division: {} / {} = {}".format(num1, num2, div))
    except ValueError:
        print("Please enter valid numbers.")
