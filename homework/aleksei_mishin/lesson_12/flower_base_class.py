from datetime import datetime


class Flower:

    def __init__(self, color, delivery_date, title, price, estimate_lifetime):
        self.__color = color
        self.__delivery_date = delivery_date
        self.__title = title
        self.__price = price
        self.__estimate_lifetime = estimate_lifetime

    @property
    def color(self):
        return self.__color

    @property
    def delivery_date(self):
        return self.__delivery_date

    @property
    def estimate_lifetime(self):
        return self.__estimate_lifetime

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    def get_current_lifetime_in_hours(self):
        delivery_date = datetime.strptime(self.__delivery_date, "%d.%m.%Y %H:%M")
        difference_in_hours = (datetime.now() - delivery_date).total_seconds() // 3600

        return difference_in_hours

    def get_time_remaining_in_hours(self):
        time_remaining = self.__estimate_lifetime - self.get_current_lifetime_in_hours()

        return time_remaining
