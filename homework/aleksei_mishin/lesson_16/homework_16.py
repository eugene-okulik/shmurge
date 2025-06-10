# В папке /homework/eugene_okulik/Lesson_16/hw_data лежит csv файл. Файл никуда не копируйте и не переносите.
# Прочитайте этот файл с помощью модуля csv и проверьте есть ли те данные, которые там перечислены,
# в нашей базе данных.
#
# При подключении к базе данных не прописывайте данные подключения в коде,
# а воспользуйтесь подходом .env c такими переменными: DB_USER, DB_PASSW, DB_HOST, DB_PORT, DB_NAME.
# Я на своем компе уже создал файл .env с этими переменными, так что, если все сделаем одинаковые названия,
# будет работать всё универсально
#
# В результате сравнения, если обнаружится, что каких-то данных, которые есть в файле, нет в базе данных,
# распечатайте каких данных не хватает в базе.
#
# Подсказка для самопроверки: в базе нет данных, которые полностью соответствуют первой строке файла,
# но в базе есть данные, которые соответствуют второй строке файла.

import os
import dotenv
from homework.aleksei_mishin.lesson_16.files import Files
from homework.aleksei_mishin.lesson_16.request_methods import SqlRequests
from homework.aleksei_mishin.lesson_16.sql_requests import SEARCH_STUDENT
from homework.aleksei_mishin.lesson_16.environments import EUGENE_OK_FILEPATH

dotenv.load_dotenv(override=True)

with SqlRequests(
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
) as sql_requests:
    new_file = Files(EUGENE_OK_FILEPATH)
    data_list = new_file.read_csv_file()
    sql_requests.print_if_data_not_in_db(query=SEARCH_STUDENT,
                                         data=data_list)
