# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте “Etiam tincidunt neque erat,
# quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero” и после этого
# выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
# но уже преобразованного.

from string import punctuation

example = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
           "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")


def add_ing_in_words(text: str):
    data_list = text.split()
    result_str = []

    for word in data_list:
        if word[-1] in punctuation:
            p_mark = word[-1]
            result_str.append(word[:-1] + "ing" + p_mark)
        else:
            result_str.append(word + "ing")

    result_str = " ".join(result_str)
    return result_str


print(add_ing_in_words(example))
