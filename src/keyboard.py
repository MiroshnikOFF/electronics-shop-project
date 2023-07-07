from src.item import Item


class MixinChangeLang:

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        return self


class Keyboard(Item, MixinChangeLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
