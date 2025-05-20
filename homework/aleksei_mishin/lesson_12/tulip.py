from flower_base_class import Flower


class Tulip(Flower):
    __TITLE = "Тюльпан"
    __PRICE = 150
    __ESTIMATE_LIFETIME = 180

    def __init__(self, color, delivery_date):
        super().__init__(color, delivery_date, self.__TITLE, self.__PRICE, self.__ESTIMATE_LIFETIME)
