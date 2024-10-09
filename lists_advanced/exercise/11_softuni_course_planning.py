# Read the initial course schedule
schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    action = command.split(":")

    if action[0] == "Add":
        lesson_title = action[1]
        if lesson_title not in schedule:
            schedule.append(lesson_title)

    elif action[0] == "Insert":
        lesson_title = action[1]
        index = int(action[2])
        if lesson_title not in schedule and 0 <= index <= len(schedule):
            schedule.insert(index, lesson_title)

    elif action[0] == "Remove":
        lesson_title = action[1]
        if lesson_title in schedule:
            # Remove the lesson
            schedule.remove(lesson_title)
            # Remove the exercise if it exists
            if f"{lesson_title}-Exercise" in schedule:
                schedule.remove(f"{lesson_title}-Exercise")

    elif action[0] == "Swap":
        lesson_title_1 = action[1]
        lesson_title_2 = action[2]

        if lesson_title_1 in schedule and lesson_title_2 in schedule:
            index_1 = schedule.index(lesson_title_1)
            index_2 = schedule.index(lesson_title_2)

            # Swap lessons
            schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]

            # Check for exercises and swap them as well
            exercise_1 = f"{lesson_title_1}-Exercise"
            exercise_2 = f"{lesson_title_2}-Exercise"

            # Check if exercises exist and swap them
            if exercise_1 in schedule and exercise_2 in schedule:
                # Swap the exercises
                exercise_index_1 = schedule.index(exercise_1)
                exercise_index_2 = schedule.index(exercise_2)

                schedule[exercise_index_1], schedule[exercise_index_2] = schedule[exercise_index_2], schedule[
                    exercise_index_1]

    elif action[0] == "Exercise":
        lesson_title = action[1]
        exercise_title = f"{lesson_title}-Exercise"
        if lesson_title in schedule:
            if exercise_title not in schedule:
                lesson_index = schedule.index(lesson_title)
                schedule.insert(lesson_index + 1, exercise_title)
        else:
            # If the lesson does not exist, add it and then the exercise
            schedule.append(lesson_title)
            schedule.append(exercise_title)

# Print the final schedule
for i in range(len(schedule)):
    print(f"{i + 1}. {schedule[i]}")
