class Patient:

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Пациент \"{}\". Остаток средств: {} руб.".format(self.name, self.balance)

    @property
    def balance(self):
        return self._balance

    def record_payment(self, amount_paid):
        assert amount_paid > 0
        self._balance += amount_paid

    def record_call(self, payment_type, number_visits):
        if payment_type == "Скидка":
            self._balance -= number_visits * 1000
        elif payment_type == "Стандарт":
            self._balance -= number_visits * 2500


if __name__ == "__main__":
    philip = Patient("Филипп Кулаков", 10000)
    alina = Patient("Алина Колесник", 4000)
    ilya = Patient("Илья Тихомиров")

    philip.record_call("Скидка", 3)
    philip.record_call("Стандарт", 2)
    alina.record_call("Стандарт", 1)
    ilya.record_call("Скидка", 4)

    philip.record_payment(2000)
    ilya.record_payment(4500)

    print(philip)
    print(alina)
    print(ilya)
