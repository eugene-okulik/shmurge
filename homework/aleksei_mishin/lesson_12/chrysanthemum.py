from flower_base_class import Flower


class Chrysanthemum(Flower):
    __TITLE = "Хризантема"
    __PRICE = 250

    @property
    def title(self):
        return self.__TITLE

    @property
    def price(self):
        return self.__PRICE
