companies = {}

while True:
    command = input().split(" -> ")

    if command[0] == "End":
        for key, value in companies.items():
            print(f"{key}")
            for employee_id in value:
                print(f"-- {employee_id}")
        break

    company_name = command[0]
    employee_id = command[1]

    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)




