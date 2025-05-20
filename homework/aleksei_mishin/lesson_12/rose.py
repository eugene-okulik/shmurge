from flower_base_class import Flower


class Rose(Flower):
    __TITLE = "Роза"
    __PRICE = 190
    __ESTIMATE_LIFETIME = 96

    def __init__(self, color, delivery_date):
        super().__init__(color, delivery_date, self.__TITLE, self.__PRICE, self.__ESTIMATE_LIFETIME)
