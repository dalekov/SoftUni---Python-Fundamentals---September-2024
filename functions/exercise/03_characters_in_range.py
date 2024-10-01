string1 = input()
string2 = input()


def function(x, y):
    string1_ord = ord(x) #97
    string2_ord = ord(y) #100

    while string1_ord != string2_ord:
        string1_ord += 1
        if string1_ord == string2_ord:
            break
        else:
            print(chr(string1_ord), end=" ")

function(x=string1, y=string2)