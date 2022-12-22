import csv


class Item:
    pay_rate = 0.8  # Уровень оплаты после скидки 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Название слишком длинное!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            f = open(file, 'r')

        except FileNotFoundError:
            print('file was not found')
        else:
            _ = f.readline()
            data = f.readlines()
            try:
                for d in data:
                    data_for_object = d.rstrip('\n').split(',')
                    data_for_object[0] = data_for_object[0].strip('"')
                    data_for_object[1] = float(data_for_object[1])
                    data_for_object[2] = int(data_for_object[2])

                    cls.all.append(Item(*data_for_object))
            except ValueError:
                print('can not initialize objects with file data')
            finally:
                f.close()


    def __str__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.price}, {self.quantity})'


Item.instantiate_from_csv('../data/items.csv')

for item in Item.all:
    print(item)