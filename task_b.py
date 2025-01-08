
try:
    grade = int(input("Enter a numerical grade between 0 - 100: "))

    if grade < 0 or grade > 100:
        print("Grades must be between 0 and 100")
    else:
        if grade >= 80:
            letter = "A"
        elif grade >= 60:
            letter = "B"
        elif grade >= 50:
            letter = "C"
        elif grade >= 40:
            letter = "D"
        else:
            letter = "F"

        print(f"Your grade is:{letter}")

except: 
    print("Error: Please enter a number")