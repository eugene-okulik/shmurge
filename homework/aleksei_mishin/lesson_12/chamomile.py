from flower_base_class import Flower


class Chamomile(Flower):
    __TITLE = "Ромашка"
    __PRICE = 100
    __ESTIMATE_LIFETIME = 200

    def __init__(self, color, delivery_date):
        super().__init__(color, delivery_date, self.__TITLE, self.__PRICE, self.__ESTIMATE_LIFETIME)
