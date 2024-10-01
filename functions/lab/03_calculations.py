operation = input()
first_num = int(input())
second_num = int(input())

def calculate():
    if operation == "multiply":
        return first_num * second_num
    elif operation == "divide":
        return first_num // second_num
    elif operation == "add":
        return first_num + second_num
    elif operation == "subtract":
        return first_num - second_num

print(calculate())