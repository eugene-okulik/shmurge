# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt
# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл, находит в нём даты
# и делает с этими датами то, что после них написано. Опирайтесь на то, что структура каждой строки одинакова:
# сначала идет номер, потом дата, потом дефис и после него текст. У вас должен получиться код, который находит даты
# и для даты под номером один в коде должно быть реализовано то действие, которое написано в файле после этой даты.
# Ну и так далее для каждой даты.

from homework.aleksei_mishin.lesson_13.environments import (
    EUGENE_OK_FILEPATH,
    DATETIME_ISO_FORMAT
)
from homework.aleksei_mishin.lesson_13.files import File
from homework.aleksei_mishin.lesson_13.date_and_time import DateAndTime

file = File(EUGENE_OK_FILEPATH)
date_and_time = DateAndTime(DATETIME_ISO_FORMAT)

str_dates_list = file.read_date_from_file()
dates_list = date_and_time.do_datetime_from_string(str_dates_list)
date1, date2, date3 = dates_list

date_and_time.print_date_plus_seven_days(date1)
date_and_time.print_date_weekday(date2)
date_and_time.how_much_days_ago(date3)
