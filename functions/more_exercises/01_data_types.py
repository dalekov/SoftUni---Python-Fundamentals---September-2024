a = input()
num = input()

def my_func(x):
    if a == "int":
        return int(num) * 2
    elif a == "real":
        return f"{int(num) * 1.5:.2f}"
    elif a == "string":
        return f"${num}$"


print(my_func(a))