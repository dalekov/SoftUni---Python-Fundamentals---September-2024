import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def center_point(x1, y1, x2, y2):
    dist1 = math.sqrt(x1 ** 2 + y1 ** 2)
    dist2 = math.sqrt(x2 ** 2 + y2 ** 2)

    if dist1 <= dist2:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"

print(center_point(x1, y1, x2, y2))