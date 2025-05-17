class Bouquet:

    def __init__(self, *args):
        self.obj_ls = list(args)

    @staticmethod
    def print_dict(dct):

        for k, v in dct.items():
            print(f"{k} - {v}")

    def get_bouquet_price(self):
        price_list = [obj.price for obj in self.obj_ls]
        print(f"Стоимость этого букета: {sum(price_list)} р.\n")

    def get_bouquet_time_of_fading(self):
        time_ls = [obj.get_time_remaining_in_hours() for obj in self.obj_ls]
        avg_time = sum(time_ls) // len(time_ls)
        print(f"Время увядания этого букета ~ {avg_time} ч.\n")

    def do_sort_by_price(self):
        sorted_objs = sorted(self.obj_ls, key=lambda x: x.price)
        flowers = {f"{obj.title} {obj.color}": f"{obj.price} р." for obj in sorted_objs}
        print("Сортировка по стоимости цветов:")
        self.print_dict(flowers)
        print()

    def do_sort_by_freshness(self):
        sorted_objs = sorted(self.obj_ls, key=lambda x: x.get_time_remaining_in_hours())
        flowers = {
            f"{obj.title} {obj.color.lower()}": f"срок годности {obj.get_time_remaining_in_hours()} ч."
            for obj in sorted_objs
        }
        print("Сортировка по свежести цветов:")
        self.print_dict(flowers)
        print()

    def do_search_by_title(self, title: str):
        obj_titles = [obj.title.lower() for obj in self.obj_ls]
        if title.lower() in obj_titles:

            for obj in self.obj_ls:
                if obj.title.lower() == title.lower():
                    print(f"Результат поиска по запросу '{title}':\n"
                          f"цвет: {obj.color}\n"
                          f"стоимость: {obj.price}\n"
                          f"дата поставки: {obj.delivery_date}\n"
                          f"осталось часов до увядания: {obj.get_time_remaining_in_hours()}\n")
                    break
        else:
            print(f"По запросу '{title}' ничего не найдено!")

    def do_search_by_color(self, color: str):
        obj_colors = [obj.color.lower() for obj in self.obj_ls]
        if color.lower() in obj_colors:

            for obj in self.obj_ls:
                if obj.color.lower() == color.lower():
                    print(f"Результат поиска по запросу '{color}':\n"
                          f"название: {obj.title}\n"
                          f"стоимость: {obj.price}\n"
                          f"дата поставки: {obj.delivery_date}\n"
                          f"осталось часов до увядания: {obj.get_time_remaining_in_hours()}\n")
                    break
        else:
            print(f"По запросу '{color}' ничего не найдено!\n")

    def do_search_by_freshness(self, exp_time_in_hours: (int, float)):  # поиск по времени увядания
        flowers = {}

        for obj in self.obj_ls:
            if obj.get_time_remaining_in_hours() >= exp_time_in_hours:
                flowers[f"{obj.title} {obj.color}"] = f"{obj.get_time_remaining_in_hours()} ч."

        if flowers:
            print(f"Результат поиска по сроку годности:")
            self.print_dict(flowers)

        else:
            print(f"Не найдено цветов, превышающих срок годности {exp_time_in_hours} ч.")
