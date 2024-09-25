n = int(input())
word = input()

sample_list = []
container_list = []

for i in range(1, n + 1):
    string = input()
    sample_list.append(string)

    if word in string:
        container_list.append(string)

print(sample_list)
print(container_list)
