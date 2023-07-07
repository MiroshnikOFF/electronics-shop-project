from src.item import Item


class MixinChangeLang:
    """Расширяет функционал класса Keyboard. Добавляет язык и возможность его изменения"""
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        """Возвращает язык клавиатуры"""
        return self.__language

    def change_lang(self):
        """Изменяет язык клавиатуры. По умолчанию 'EN'"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinChangeLang):
    """Класс для клавиатур, дочерний от Item"""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
