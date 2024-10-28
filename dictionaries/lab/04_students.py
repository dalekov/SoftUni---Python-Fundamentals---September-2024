students = {}

num_entry = 0
while True:
    command = input().split(":")
    num_entry += 1

    if len(command) == 1:
        for entry in students:
            if command[0].replace("_", ' ') == students[entry]["course"]:
                print(f"{students[entry]['name']} - {students[entry]['student_id']}")
        break

    name = command[0]
    student_id = command[1]
    course = command[2]

    students.update({f"{num_entry}": {"name": name, "student_id": student_id, "course": course}})