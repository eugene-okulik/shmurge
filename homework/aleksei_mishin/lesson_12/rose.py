from flower_base_class import Flower


class Rose(Flower):
    __TITLE = "Роза"
    __PRICE = 190

    @property
    def title(self):
        return self.__TITLE

    @property
    def price(self):
        return self.__PRICE
