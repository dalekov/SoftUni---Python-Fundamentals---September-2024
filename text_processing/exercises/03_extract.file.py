path_file = input().split('\\')

for path in path_file:
    if '.' in path:
        file_name, file_extension = path.split('.')

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
