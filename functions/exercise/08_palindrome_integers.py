numbers_list= input().split(", ")


def is_palindrome(x):
    output = []
    for number in x:
         output.append(number == number[::-1])

    for el in output:
        print(el)


is_palindrome(x=numbers_list)