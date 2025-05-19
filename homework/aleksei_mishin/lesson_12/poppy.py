from flower_base_class import Flower


class Poppy(Flower):
    __TITLE = "Мак"
    __PRICE = 350
    __ESTIMATE_LIFETIME = 160

    def __init__(self, color, delivery_date):
        super().__init__(color, delivery_date, self.__TITLE, self.__PRICE, self.__ESTIMATE_LIFETIME)
