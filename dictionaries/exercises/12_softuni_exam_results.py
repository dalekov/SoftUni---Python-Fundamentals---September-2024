participants = {}
languages = {}

while True:
    command = input().split('-')

    if command[0] == "exam finished":
        # Print Results
        print("Results:")
        for username, user_data in participants.items():
            if not user_data.get("banned", False):
                total_score = sum(points for lang, points in user_data.items() if lang != "banned")
                print(f"{username} | {total_score}")

        # Print Submissions
        print("Submissions:")
        for language, count in languages.items():
            print(f"{language} - {count}")
        break

    elif command[1] == 'banned':
        username = command[0]
        if username in participants:
            participants[username]["banned"] = True  # Mark user as banned

    else:
        # Parse user, language, and points
        username = command[0]
        language = command[1]
        points = int(command[2])

        # Initialize participant and store max points per language
        if username not in participants:
            participants[username] = {}
        if language not in participants[username] or participants[username][language] < points:
            participants[username][language] = points

        # Track submissions per language
        if language not in languages:
            languages[language] = 0
        languages[language] += 1
