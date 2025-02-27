from csv import DictReader


class InstantiateCSVError(Exception):
    """Класс исключения при проверке csv файла на повреждения"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

        Item.all.append(self)

    def __repr__(self):
        """
        Возвращает информацию об экземпляре класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает информацию об экземпляре класса для пользователя
        """
        return self.name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Позволяет изменить название товара
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса `Item` данными из файла _src/items.csv
        """
        try:
            with open('../src/items.csv', encoding='cp1251') as csv_file:
                file = DictReader(csv_file)
                Item.all.clear()
                for row in file:
                    if len(row) != 3:
                        raise InstantiateCSVError
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    cls(name, price, quantity)
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')
        except InstantiateCSVError:
            print("InstantiateCSVError: Файл item.csv поврежден")


    @staticmethod
    def string_to_number(num):
        """
        Возвращает число из числа-строки
        """
        return int(num.split('.')[0])

    def __add__(self, other):
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)








