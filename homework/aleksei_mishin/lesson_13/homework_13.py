# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt
# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл, находит в нём даты
# и делает с этими датами то, что после них написано. Опирайтесь на то, что структура каждой строки одинакова:
# сначала идет номер, потом дата, потом дефис и после него текст. У вас должен получиться код, который находит даты
# и для даты под номером один в коде должно быть реализовано то действие, которое написано в файле после этой даты.
# Ну и так далее для каждой даты.

from homework.aleksei_mishin.lesson_13.environments import EUGENE_OK_FILEPATH
from homework.aleksei_mishin.lesson_13.files import File

file_dates = File(EUGENE_OK_FILEPATH).data
date1, date2, date3 = file_dates

date1.print_date_plus_seven_days()
date2.print_date_weekday()
date3.how_much_days_ago()
