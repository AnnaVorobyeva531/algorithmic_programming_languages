#  Оформить функцией поиск в словаре
employee_salary = {'Миронова Елена Викторовна': 35000, 'Кузнецов Артем Михайлович': 45000,
                   'Васильева Екатерина Олеговна': 39000, 'Смирнов Олег Павлович': 50000,
                   'Мельникова Ольга Викторовна': 32000}  # словарь зарплаты сотрудников


#  Определение самой низкой зарплаты
def has_low_salary(salary):
    return employee_salary[salary] < 35000


low_salary = list(filter(has_low_salary, employee_salary.keys()))
print("Самую низкую зарплату имеет", low_salary)


#  Повышение оклада сотрудников на 10%
def bonus(current_salary):
    return (current_salary[0], round(current_salary[1] * 1.10, 2))


new_employee_salary = dict(map(bonus, employee_salary.items()))
print(new_employee_salary)


# Определение зарплаты
def find_patch(name, salary):
    if salary in name:
        return name[salary]
    else:
        return "Not found"


employee_salary['_found'] = find_patch
print("Кузнецов Артем Михайлович имеет зарплату", find_patch(employee_salary, 'Кузнецов Артем Михайлович'))
print("Миронова Елена Викторовна имеет зарплату",
      employee_salary['_found'](employee_salary, 'Миронова Елена Викторовна'))



