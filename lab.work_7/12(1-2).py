class Hospital_staff:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print('Сотрудник больницы: Имя:"{0}", Возраст:"{1}",'.format(self.name, self.age), end=" ")


class Doctor(Hospital_staff):

    def __init__(self, name, age, salary=0):
        Hospital_staff.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        Hospital_staff.tell(self)
        print(', Зарплата: "{0:d}"'.format(self.salary))

    def __str__(self):
        return "Врач: \"{}\". Зарплата с премией составит: {} руб.".format(self.name, self.salary)

    def bonus(self, term_work, new_salary):
        if term_work == "5 лет":
            self.salary += new_salary * 1
        elif term_work == "1 год":
            self.salary += new_salary * 0


class Patient:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def data(self):
        print('Пациент: Имя:"{0}", Возраст:"{1}"'.format(self.name, self.age), end=" ")

    def name_patient(self):
        print('Пациент: Имя:"{0}"'.format(self.name), end=" ")


class Time_receipt(Patient):
    def __init__(self, name, age, time, medical_diagnosis):
        Patient.__init__(self, name, age)
        self.time = time
        self.medical_diagnosis = medical_diagnosis

    def data(self):
        Patient.data(self)
        print('Запись к врачу на: "{0}"'.format(self.time))

    def diagnosis_patient(self):
        Patient.name_patient(self)
        print('диагноз:"{0}" '.format(self.medical_diagnosis))


employee_1 = Doctor('Миронова Елена Викторовна', 41, 35000)
employee_2 = Doctor('Кузнецов Артем Михайлович', 36, 45000)
employee_3 = Doctor('Васильева Екатерина Олеговна', 32, 39000)
employee_4 = Doctor('Смирнов Олег Павлович', 32, 50000)
employee_5 = Doctor('Мельникова Ольга Викторовна', 28, 32000)

philip = Time_receipt("Филипп Кулаков", 22, "12:00", "Ангина")
alina = Time_receipt("Алина Колесник", 18, "16:25", "Зубная боль")
ilya = Time_receipt("Илья Тихомиров", 24, "18:45", "Миопия")

employee_1.bonus("5 лет", 35000)
employee_2.bonus("1 год", 45000)
employee_3.bonus("5 лет", 39000)
employee_4.bonus("1 год", 50000)
employee_5.bonus("5 лет", 32000)

staff_member = [employee_1, employee_2, employee_3, employee_4, employee_5]
for staff_member in staff_member:
    staff_member.tell()
print()
customer = [philip, alina, ilya]
for customer in customer:
    customer.data()

print()

print(employee_1)
print(employee_2)
print(employee_3)
print(employee_4)
print(employee_5)

print()

patient = [philip, alina, ilya]
for patient in patient:
    patient.diagnosis_patient()
