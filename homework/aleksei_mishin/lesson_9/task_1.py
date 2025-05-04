# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
#
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

import datetime

example_date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(example_date, "%b %d, %Y - %H:%M:%S")
month_name = python_date.strftime("%B")
new_date_format = python_date.strftime("%d.%m.%Y, %H:%M")

print(month_name)
print(new_date_format)
