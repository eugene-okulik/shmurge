class Bouquet:

    def __init__(self, *args):
        self.flowers_list = list(args)

    def get_bouquet_price(self):
        price_list = [obj.price for obj in self.flowers_list]
        print(f"Стоимость этого букета: {sum(price_list)} р.\n")

    def get_bouquet_time_of_fading(self):
        time_ls = [obj.time_remaining_in_hours for obj in self.flowers_list]
        avg_time = sum(time_ls) // len(time_ls)
        print(f"Время увядания этого букета ~ {avg_time} ч.\n")

    def sort_by(self, key):
        return sorted(self.flowers_list, key=lambda x: getattr(x, key))

    def search_by(self, key, value):
        return next(filter(lambda x: getattr(x, key).lower() == value.lower(), self.flowers_list), None)

    def do_search_by_freshness(self, exp_time_in_hours: (int, float)):  # поиск по времени увядания
        fresh_flowers_list = []

        for obj in self.flowers_list:
            if obj.time_remaining_in_hours >= exp_time_in_hours:
                fresh_flowers_list.append(obj)

        return fresh_flowers_list
