# Дан такой кусок прайс листа:
#
# (Копируйте эту переменную (константу) в код прямо как есть)
#
# PRICE_LIST = '''тетрадь 50р
# книга 200р
# ручка 100р
# карандаш 70р
# альбом 120р
# пенал 300р
# рюкзак 500р'''
# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:
#
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# В выполнении не должно быть циклов.
#
# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# method 1
def dict_generator_1(text: str):
    price_ls = PRICE_LIST.split()
    new_price_ls = [(price_ls[i - 1], int(price_ls[i][:-1])) for i in range(1, len(price_ls), 2)]
    price_dict = {k: v for k, v in new_price_ls}

    return price_dict


# method 2
def dict_generator_2(text: str):
    names = [i for i in PRICE_LIST.split() if i.isalpha()]
    prices = [int(i[:-1]) for i in PRICE_LIST.split() if i[:-1].isnumeric()]

    return dict(zip(names, prices))


print(f"Method 1: {dict_generator_1(PRICE_LIST)}")
print(f"Method 2: {dict_generator_2(PRICE_LIST)}")