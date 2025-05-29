from datetime import datetime, timedelta
from homework.aleksei_mishin.lesson_13.environments import DATETIME_ISO_FORMAT


class DateAndTime:

    def __init__(self, line, date_format=DATETIME_ISO_FORMAT):
        self.line = line
        self.date_format = date_format
        self.date_str = self.get_date_from_string()
        self.date = self.do_datetime_from_string()

    def get_date_from_string(self):
        text_list = self.line.split()
        str_date = f'{text_list[1]} {text_list[2]}'

        return str_date

    def do_datetime_from_string(self):
        return datetime.strptime(self.date_str, self.date_format)

    def print_date_plus_seven_days(self):
        print(f'Date + 7 days: {self.date + timedelta(days=7)}')

    def print_date_weekday(self):
        print(f'Date weekday: day number - {datetime.weekday(self.date)} ({datetime.strftime(self.date, "%A")})')

    def how_much_days_ago(self):
        different_date = datetime.now() - self.date
        print(f'It was {different_date.days} days ago')
