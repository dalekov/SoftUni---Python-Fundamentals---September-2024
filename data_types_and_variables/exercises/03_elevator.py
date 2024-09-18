import math

num_of_people = int(input())
capacity = int(input())

courses = math.ceil(num_of_people / capacity)
print(courses)