number = int(input())

def loading_bar(x):
    if number == 0:
        return f"{number}% [..........]\nStill loading..."
    elif number == 10:
        return f"{number}% [%.........]\nStill loading..."
    elif number == 20:
        return f"{number}% [%%........]\nStill loading..."
    elif number == 30:
        return f"{number}% [%%%.......]\nStill loading..."
    elif number == 40:
        return f"{number}% [%%%%......]\nStill loading..."
    elif number == 50:
        return f"{number}% [%%%%%.....]\nStill loading..."
    elif number == 60:
        return f"{number}% [%%%%%%....]\nStill loading..."
    elif number == 70:
        return f"{number}% [%%%%%%%...]\nStill loading..."
    elif number == 80:
        return f"{number}% [%%%%%%%%..]\nStill loading..."
    elif number == 90:
        return f"{number}% [%%%%%%%%%.]\nStill loading..."
    elif number == 100:
        return f"{number}% Complete!\n[%%%%%%%%%%]"

print(loading_bar(number))