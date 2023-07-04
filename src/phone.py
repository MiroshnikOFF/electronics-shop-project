from src.item import Item


class Phone(Item):
    """Класс для телефонов, дочерний от Item"""

    def __init__(self, name, price, quantity, number_of_sim):
        """Расширяет функционал класса Item добавлением количества SIM-карт"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Возвращает расширенный repr класса Item с указанием количества SIM-карт"""
        return f"{super().__repr__().split(')')[0]}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Возвращает количество SIM-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """Устанавливает количество SIM-карт"""
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = number



