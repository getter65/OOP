class MyInt:
    def __init__(self, num):
        self.__num = int(num)

    def __repr__(self):
        return f'{self.__class__}: {self.__num}'

    def __str__(self):
        return str(self.__num)

    @classmethod
    def __validate(cls, other):
        if not isinstance(other, (str, int, float, MyInt)):
            raise TypeError('must be str, int, float or MyInt')
        if isinstance(other, (str, int, float)):
            return int(other)
        else:
            return other.__num

    def __add__(self, other):
        other = self.__validate(other)
        return MyInt(self.__num + other)

    def __radd__(self, other):
        other = self.__validate(other)
        return MyInt(self.__num + other)

    def __iadd__(self, other):
        other = self.__validate(other)
        self.__num = self.__num + other
        return self

    def __sub__(self, other):
        other = self.__validate(other)
        return MyInt(self.__num - other)

    def __isub__(self, other):
        other = self.__validate(other)
        self.__num = self.__num - other
        return self

    def __mul__(self, other):
        other = self.__validate(other)
        return MyInt(self.__num * other)

    def __imul__(self, other):
        other = self.__validate(other)
        self.__num = self.__num * other
        return self

    def __truediv__(self, other):
        other = self.__validate(other)
        return self.__num / other

    def __itruediv__(self, other):
        other = self.__validate(other)
        self.__num = self.__num / other
        return self

    def __floordiv__(self, other):
        other = self.__validate(other)
        return MyInt(self.__num // other)

    def __ifloordiv__(self, other):
        other = self.__validate(other)
        self.__num = self.__num // other
        return self

    def __mod__(self, other):
        other = self.__validate(other)
        return MyInt(self.__num % other)

    def __imod__(self, other):
        other = self.__validate(other)
        self.__num = self.__num % other
        return self

    def __eq__(self, other):
        other = self.__validate(other)
        return self.__num == other

    def __ne__(self, other):
        other = self.__validate(other)
        return self.__num != other

    def __lt__(self, other):
        other = self.__validate(other)
        return self.__num < other

    def __le__(self, other):
        other = self.__validate(other)
        return self.__num <= other

    def __gt__(self, other):
        other = self.__validate(other)
        return self.__num > other

    def __ge__(self, other):
        other = self.__validate(other)
        return self.__num >= other


a = MyInt(5)
a = a + 5
print(a)

a = a - 2 - 3
print(a)

a = a * '5'
print(a)

a = a / 10
print(a)