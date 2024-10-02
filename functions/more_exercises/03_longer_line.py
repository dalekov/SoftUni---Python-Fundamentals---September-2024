import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    dist1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist2 = math.sqrt((x3 - x4)**2 + (y3 - y4)**2)

    dist_pair_1 = math.sqrt(x1 ** 2 + y1 ** 2)
    dist_pair_2 = math.sqrt(x2 ** 2 + y2 ** 2)
    dist_pair_3 = math.sqrt(x3 ** 2 + y3 ** 2)
    dist_pair_4 = math.sqrt(x4 ** 2 + y4 ** 2)

    if dist1 >= dist2:
        if dist_pair_1 > dist_pair_2:
            return f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})"
        else:
            return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})"

    else:
        if dist_pair_3 > dist_pair_4:
            return f"({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})"
        else:
            return f"({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})"


print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))