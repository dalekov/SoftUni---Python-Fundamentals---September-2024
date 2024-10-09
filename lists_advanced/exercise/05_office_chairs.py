rooms = int(input())

total_chairs = 0
total_visitors = 0

for room in range(1, rooms + 1):
    info = input().split()
    chairs = len(info[0])
    visitors = int(info[1])

    total_chairs += int(chairs)
    total_visitors += visitors

    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        continue

else:
    if total_chairs >= total_visitors:
        print(f"Game On, {total_chairs - total_visitors} free chairs left")
