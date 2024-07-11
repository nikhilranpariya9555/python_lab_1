# Function to display the current list of employee names
def display_employees(emp_list):
    print("\nCurrent Employee List:")
    for i, name in enumerate(emp_list, start=1):
        print(f"{i}. {name}")

# Main block to manage employee names
if __name__ == "__main__":
    EMPNAME = []

    while True:
        print("\nEmployee Management Menu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Append Employee")
        print("4. Display Employees")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Add Employee
            name = input("Enter the employee name to add: ")
            EMPNAME.append(name)
            print(f"Employee '{name}' added.")

        elif choice == '2':
            # Remove Employee
            name = input("Enter the employee name to remove: ")
            if name in EMPNAME:
                EMPNAME.remove(name)
                print(f"Employee '{name}' removed.")
            else:
                print(f"Employee '{name}' not found in the list.")

        elif choice == '3':
            # Append Employee (Similar to Add in this context)
            name = input("Enter the employee name to append: ")
            EMPNAME.append(name)
            print(f"Employee '{name}' appended.")

        elif choice == '4':
            # Display Employees
            display_employees(EMPNAME)

        elif choice == '5':
            # Exit the program
            print("Exiting Employee Management.")
            break

        else:
            print("Invalid choice, please select a valid option.")
