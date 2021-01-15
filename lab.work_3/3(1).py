# Описание работников больницы (врачей), используя список
# Работники больницы = [Ф.И.О., возраст, оклад, специализация]
print("Task-1")
hospital_workers = [['Миронова Елена Викторовна', 41, 35000, 'Терапевт'],
                    ['Кузнецов Артем Михайлович', 36, 45000, 'Стоматолог'],
                    ['Васильева Екатерина Олеговна', 32, 39000, 'Окулист'],
                    ['Смирнов Олег Павлович', 32, 50000, 'Ортопед'],
                    ['Мельникова Ольга Викторовна', 28, 32000, 'Невролог']]

# Выбор сотрудника, который получает самую низкую зарплату
salary_min = 50000
for m in hospital_workers:
    if m[2] < salary_min:
        salary_min = m[2]
        employee_name = m[0]
print("Сотрудник", employee_name, "имеет наименьший оклад равный", salary_min, "т.р.")

# Нумирация списка работников
for c, value in enumerate(hospital_workers, 1):
    print(c, value)

#  Выбор сотрудника с самым длынным Ф.И.О
employee_name_max = len([])
for m in hospital_workers:
    if len(m[0]) > employee_name_max:
        employee_name_max = len(m[0])
        employee_name = m[0]
print("Сотрудник", employee_name, "имеет самое длинное Ф.И.О, которое состоит из ", employee_name_max, "символов")


