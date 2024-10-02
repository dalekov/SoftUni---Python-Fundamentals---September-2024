num1 = int(input())
num2 = int(input())
num3 = int(input())

def multiplication_sign(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return "zero"

    negative_count = sum(1 for num in (x, y, z) if num < 0)
    if negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"


print(multiplication_sign(num1, num2, num3))
