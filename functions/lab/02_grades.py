grade_float = float(input())

def print_grade():
    if 2.00 <= grade_float <= 2.99:
        return "Fail"
    elif 3.00 <= grade_float <= 3.49:
        return "Poor"
    elif 3.50 <= grade_float <= 4.49:
        return "Good"
    elif 4.50 <= grade_float <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_float <= 6.00:
        return"Excellent"


print(print_grade())