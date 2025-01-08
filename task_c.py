password = input("Enter a password: ")

try:
    if len(password) < 8 or password.isalpha() or password.isdigit():
        print("Your password must contain at least 8 characters, and a mix of letters and numbers")
    else:
        print("Your password is valid")
except:
    print("error, please try again.")
