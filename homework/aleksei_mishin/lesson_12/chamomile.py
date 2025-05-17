from flower_base_class import Flower


class Chamomile(Flower):
    __TITLE = "Ромашка"
    __PRICE = 100

    @property
    def title(self):
        return self.__TITLE

    @property
    def price(self):
        return self.__PRICE
