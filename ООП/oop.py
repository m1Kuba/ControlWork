class Person:
    def __init__(self):
        self._age = 0


    def set_age(self, age):
        if age < 0:
            return print('Ошибка: Возраст не должен быть отрицательным')
        self._age = age


    def get_age(self):
        return self._age

p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25
p.set_age(-5)  # Должна быть ошибка или предупреждение