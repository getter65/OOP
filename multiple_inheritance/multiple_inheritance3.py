class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, value):
        self.first, self.last = value.split(' ')

    @fullname.deleter
    def fullname(self):
        self.first, self.last = 'None', 'None'


    @property
    def email(self):
        return self.first + '.' + self.last + '@gmail.com'




emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
