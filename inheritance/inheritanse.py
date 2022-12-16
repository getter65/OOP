class Item:
    
    name: str
    price: int
    quantity: int
    
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        try:
            self.__check(name, price, quantity)
        except TypeError as e:
            print(e)
        
    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}"
    
    def __check(self, name, price, quantity):
        
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой")
        
        if not isinstance(price, int):
            raise TypeError("Цена товара должа быть числом")
        
        if not isinstance(quantity, int):
            raise TypeError("Количество товара должно быть целым числом")
            

class Phone(Item):
    
    broken_phone: int

    def __init__(self, name, price, quantity, broken_phone):
        super().__init__(name, price, quantity)
        self.broken_phone = broken_phone
        
    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}, {self.broken_phone}"
    

class MyList(list):
    def __init__(self, some_list):
        super().__init__(some_list)
        print('Работает магический метод init')

    def __getitem__(self, item):
        super().__getitem__(item)
        print('Работает магический метод getitem')

    def __str__(self):
        print('Работает магический метод str')
        return super(MyList, self).__str__()


    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        print('Работает магический метод setitem')

    def __len__(self):
        print('Работает магический метод len')
        return super(MyList, self).__len__()


lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))


class TeamIterator:
    def __init__(self, team):
        self.team = team
        self.counter_j = -1
        self.counter_s = -1

    def __next__(self):
        if self.counter_j == len(self.team._juniorMembers) - 1 and self.counter_s == len(self.team._seniorMembers) - 1:
            raise StopIteration
        elif self.counter_j < len(self.team._juniorMembers) - 1:
            self.counter_j += 1
            return self.team._juniorMembers[self.counter_j], 'junior'
        else:
            self.counter_s += 1
            return self.team._seniorMembers[self.counter_s], 'senior'


class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break



    