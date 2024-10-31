contests = {}

while True:
    command = input().split(":")

    if command[0] == "end of contests":
        break


    contest = command[0]
    password = command[1]

    contests[contest] = password

submissions = {}
while True:
    new_command = input().split("=>")

    if new_command[0] == "end of submissions":

        # Find best candidate:
        max_total_points = 0
        for contestant, contests in submissions.items():
            total_points = sum(contests.values())
            if total_points > max_total_points:
                max_total_points = total_points
                best_candidate = contestant
        print(f"Best candidate is {best_candidate} with total {max_total_points} points.")

        print("Ranking:")
        # Print out each contestant and their points.
        # Sort keys alphabetically:
        sorted_names = sorted(submissions.keys(), key=lambda x:x.lower())
        for name in sorted_names:
            print(f"{name}")
            for score in sorted(submissions[name].values(), reverse=True):
                for key in submissions[name]:
                    if submissions[name][key] == score:
                        print(f"#  {key} -> {submissions[name][key]}")
        break

    contest = new_command[0]
    password = new_command[1]
    username = new_command[2]
    points = int(new_command[3])

    if contest in contests and password == contests[contest]:
        if username not in submissions:
            submissions[username] = {}

        if contest not in submissions[username] or submissions[username][contest] < points:
                submissions[username][contest] = points