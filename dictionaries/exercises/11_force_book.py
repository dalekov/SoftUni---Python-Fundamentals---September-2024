user_log = {}


while True:
    command = input()

    if command == "Lumpawaroo":
        for key, users_list in user_log.items():
            if len(users_list) > 0:
                print(f"Side: {key}, Members: {len(users_list)}")
                for user in users_list:
                    print(f"! {user}")
        break

    if '|' in command:
        force_side, force_user = command.split(' | ')

        if force_side not in user_log:
            user_log[force_side] = []

        user_exists = any(force_user in users for users in user_log.values())

        if not user_exists:
            user_log[force_side].append(force_user)


    elif ' -> ' in command:
        force_user, force_side = command.split(' -> ')

        for side, users in user_log.items():
            if force_user in users:
                users.remove(force_user)

        if force_side not in user_log:
            user_log[force_side] = []

        user_log[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
