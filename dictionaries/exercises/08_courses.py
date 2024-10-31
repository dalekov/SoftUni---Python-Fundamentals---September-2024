courses = {}

while True:
    command  = input().split(" : ")

    if command[0] == "end":
        for key, value in courses.items():
            print(f"{key}: {len(value)}")
            for student in value:
                print(f"-- {student}")
        break

    course_name = command[0]
    student_name = command[1]

    if course_name not in courses:
        courses[course_name] = []


    courses[course_name].append(student_name)

