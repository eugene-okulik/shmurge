# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
#
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).

from rose import Rose
from chamomile import Chamomile
from chrysanthemum import Chrysanthemum
from poppy import Poppy
from tulip import Tulip
from bouquet import Bouquet

roses = Rose("Розовый", "19.05.2025 12:00")
chrysanthemums = Chrysanthemum("Оранжевый", "19.05.2025 12:00")
chamomiles = Chamomile("Белый", "17.05.2025 12:00")
poppies = Poppy("Красный", "16.05.2025 12:00")
tulips = Tulip("Желтый", "16.05.2025 12:00")

new_bouquet = Bouquet(roses, chrysanthemums, roses, tulips, chamomiles, poppies, tulips, chamomiles)

new_bouquet.get_bouquet_time_of_fading()
new_bouquet.get_bouquet_price()

print(new_bouquet.do_sort_by_price())
print(new_bouquet.do_sort_by_freshness())
print(new_bouquet.do_search_by_title("Роза"))
print(new_bouquet.do_search_by_color("Желтый"))
print(new_bouquet.do_search_by_freshness(10))
