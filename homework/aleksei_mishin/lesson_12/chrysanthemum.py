from flower_base_class import Flower


class Chrysanthemum(Flower):
    __TITLE = "Хризантема"
    __PRICE = 250
    __ESTIMATE_LIFETIME = 148

    def __init__(self, color, delivery_date):
        super().__init__(color, delivery_date, self.__TITLE, self.__PRICE, self.__ESTIMATE_LIFETIME)
