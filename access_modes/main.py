class Person:
    def __init__(self, fio, age, passport, weight):
        if self.verify_fio(fio) and self.verify_age(age) and self.verify_ps(passport) and self.verify_weight(weight):
            self.__fio = fio
            self.__age = age
            self.__passport = passport
            self.__weight = weight

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    def verify_fio(self, name):
        if type(name) is not str:
            raise ValueError('ФИО должно быть строкой')
        else:
            fio_list = name.split(' ')
            if len(fio_list) != 3:
                raise ValueError('Неверный формат записи ФИО')
            else:
                for n in fio_list:
                    if not n.isalpha():
                        raise ValueError('В ФИО можно использовать только буквенные символы')
                    else:
                        if len(n) < 1:
                            raise ValueError('В ФИО должен быть хотя бы один символ')
                return True

    def verify_age(self, num):
        if num < 14 or num > 150 or type(num) is not int:
            raise ValueError('Возраст должен быть целым числом от 14 до 150')
        return True

    def verify_weight(self, kg):
        if type(kg) is not float or kg < 25.0:
            raise ValueError('Вес должен быть вещественным числом от 25 и выше')

    def verify_ps(self, pas):
        if type(pas) is not str:
            raise ValueError('Паспорт должен быть строкой')
        else:
            pas_list = pas.split(' ')
            if len(pas_list) != 2:
                raise ValueError('Неверный формат паспорта')
            else:
                for num in pas_list:
                    if not num.isdigit():
                        raise ValueError('Серия и номер паспорта должны содержать только числа')
                return True


p = Person('Иванов Иван Иванович', 50, '0000 000000', 85.0)

p.fio = 'Иванов FFF Иванович'
print(p.fio)

p.age = 34
print(p.age)

p.passport = '123 3456'
print(p.passport)

p.weight = 76.3
print(p.weight)