# enter day of week non case sensitive

day = input("Enter a day of the week: ")

# prints monday =1 sunday = 7

match day.lower():
    case "monday":
        print("Monday is day 1")
    case "tuesday":
        print("Tuesday is day 2")
    case "wednesday":
        print("Wednesday is day 3")
    case "thursday":
        print("Thursday is day 4")
    case "friday":
        print("Friday is day 5")
    case "saturday":
        print("Saturday is day 6")
    case "sunday":
        print("Sunday is day 7")
    case _:
        print("Please enter a valid day")
    
    
# else enter valid day

