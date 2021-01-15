# 1) Сделать int такой что 2+2=5
class MyInt(int):
    def __add__(self, x):
        return super().__add__(x + 1)


y = MyInt(2)
n = y + 2
print(n)


#  2) Сделать так, чтобы len(list) < 10
class MyList(list):
    def __init__(self, x):
        if len(x) > 10:
            raise ValueError('> 10')
        else:
            super().__init__(x)

    def append(self, x):
        if len(self) == 10:
            raise ValueError('> 10')
        else:
            super().append(x)


y = MyList([5, 2, 4, 1, 6, 3, 10])
y.append(11)
print(y)
