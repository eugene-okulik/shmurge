from flower_base_class import Flower


class Poppy(Flower):
    __TITLE = "Мак"
    __PRICE = 350

    @property
    def title(self):
        return self.__TITLE

    @property
    def price(self):
        return self.__PRICE
