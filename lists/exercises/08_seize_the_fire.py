fires = input().split("#")
water = int(input())

effort = 0
total_fire = 0

put_out_cells = []

for fire in fires:
    level_of_fire, required_water = fire.split(" = ")

    required_water = int(required_water)

    if (level_of_fire == "High" and 81 <= required_water <= 125) or (level_of_fire == "Medium" and 51 <= required_water <= 80) or (level_of_fire == "Low" and 1 <= required_water <= 50):
        if water >= required_water:
            water -= required_water
            effort += 0.25 * required_water
            put_out_cells.append(fire)
        else:
            continue

print("Cells:")

for cell in put_out_cells:
    required_water = int(cell.split(" = ")[1])
    total_fire += required_water
    print(f" - {required_water}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
