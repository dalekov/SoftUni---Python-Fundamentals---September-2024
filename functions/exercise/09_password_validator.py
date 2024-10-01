password = input()

def pass_validator(x):
    errors = []

    if not 6 <= len(x) <= 10:
        errors.append("Password must be between 6 and 10 characters")

    if not x.isalnum():
        errors.append("Password must consist only of letters and digits")

    if not sum(2 for ch in x if ch.isdigit()):
        errors.append("Password must have at least 2 digits")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


pass_validator(password)
