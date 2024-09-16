first_num = float(input())
second_num = float(input())
third_num = float(input())

if first_num > second_num and first_num > third_num:
    print(int(first_num))
elif second_num > first_num and second_num > third_num:
    print(int(second_num))
elif third_num > first_num and third_num > second_num:
    print(int(third_num))