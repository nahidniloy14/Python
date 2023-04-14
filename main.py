employee_details = [("Araf", "200"), ("Jabir", 400), ("Faruk", 350), ("Jony", 250)]


def employee_check(employee_details):
    highest_paid_employee = ''
    max_salary = 0
    for name,salary in employee_details:

        if salary > max_salary:
            max_salary=salary
            highest_paid_employee=name
        else:
            pass
    return max_salary, highest_paid_employee


print(employee_check(employee_details))

