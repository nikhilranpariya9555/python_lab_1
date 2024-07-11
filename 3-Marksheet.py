# Function to calculate grade based on average
def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

# Main block to take user input, calculate total, average, and grade
if __name__ == "__main__":
    try:
        # Take user input for marks in 5 subjects
        subjects = ['Math', 'Science', 'English', 'History', 'Geography']
        marks = []
        
        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))
            marks.append(mark)
        
        # Calculate total and average
        total = sum(marks)
        average = total / len(subjects)
        
        # Calculate grade
        grade = calculate_grade(average)
        
        # Display results
        print("\nMarksheet:")
        for i in range(len(subjects)):
            print(f"{subjects[i]}: {marks[i]}")
        
        print(f"\nTotal Marks: {total}")
        print(f"Average Marks: {average}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Please enter valid numbers.")
