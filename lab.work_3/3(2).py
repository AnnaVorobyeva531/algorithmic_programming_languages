# Описание работников больницы (врачей), используя словарь
employee_salary = {'Миронова Елена Викторовна': 35000, 'Кузнецов Артем Михайлович': 45000,
                   'Васильева Екатерина Олеговна': 39000, 'Смирнов Олег Павлович': 50000,
                   'Мельникова Ольга Викторовна': 32000}  # словарь зарплаты сотрудников
payment_specialization = dict(Терапевт='35000', Стоматолог='45000', Окулист='39000', Ортопед='50000', Невролог='32000')

#  Расчет расходов
expenses = 0
for value in employee_salary.values():
    expenses += value
print("Для обеспечения сотрудников зарплатой потребуется", expenses, "т.р.")

# Определение высокооплачиваемой специализации
max = 0
for key in payment_specialization:
    if int(payment_specialization[key]) > max:
        max = int(payment_specialization[key])
        n = key
print("Сама востребованная специализая", n + " ее стоимость оплаты составляет " + str(max), "т.р")

# Определение наименьшего уникального значения в словаре
flipped_dict = dict(zip(employee_salary.values(), employee_salary.keys()))

counter = {}
for k in employee_salary:
    val = employee_salary[k]
    counter[val] = counter.get(val, 0) + 1

lowest_unique = (sorted([k for k in counter if counter[k] == 1]) or [None])[0]
if lowest_unique is None:
    print("Not found!")
else:
    print("Found [%s]->[%s]" % (flipped_dict[lowest_unique], lowest_unique))
