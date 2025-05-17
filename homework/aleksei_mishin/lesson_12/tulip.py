from flower_base_class import Flower


class Tulip(Flower):
    __TITLE = "Тюльпан"
    __PRICE = 150

    @property
    def title(self):
        return self.__TITLE

    @property
    def price(self):
        return self.__PRICE
