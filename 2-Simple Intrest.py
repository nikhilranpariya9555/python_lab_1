# Function to calculate simple interest
def calculate_simple_interest(principal, time, rate):
    simple_interest = (principal * time * rate) / 100
    return simple_interest

# Main block to take user input and display the result
if __name__ == "__main__":
    try:
        # Take user input
        principal = float(input("Enter the principal amount: "))
        time = float(input("Enter the time period in years: "))
        rate = float(input("Enter the rate of interest: "))

        # Calculate simple interest
        simple_interest = calculate_simple_interest(principal, time, rate)

        # Display the result
        print("The simple interest is: {}".format(simple_interest))
    except ValueError:
        print("Please enter valid numbers.")
