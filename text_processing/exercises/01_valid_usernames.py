usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        if username.isalnum() or (username.isalnum() or '-' in username or '_' in username ):
            print(username)