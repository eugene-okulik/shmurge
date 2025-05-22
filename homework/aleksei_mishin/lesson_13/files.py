from datetime import datetime, timedelta


class File:

    def __init__(self, filepath):
        self.filepath = filepath
        self.date_format = '%Y-%m-%d %H:%M:%S.%f'

    def read_date_from_file(self):
        result = []

        with open(self.filepath) as file:
            for line in file:
                result.append(self.__get_date_from_string(line))

        return result

    @staticmethod
    def __get_date_from_string(text: str):
        text_list = text.split()
        str_date = f'{text_list[1]} {text_list[2]}'

        return str_date

    def do_datetime_from_string(self, str_date_list):
        result = [datetime.strptime(s, self.date_format) for s in str_date_list]

        return result

    @staticmethod
    def print_date_plus_seven_days(date):
        print(f'Date + 7 days: {date + timedelta(days=7)}')

    @staticmethod
    def print_date_weekday(date):
        print(f'Date weekday: day number - {datetime.weekday(date)} ({datetime.strftime(date, "%A")})')

    @staticmethod
    def how_much_days_ago(date):
        different_date = datetime.now() - date
        print(f'It was {different_date.days} days ago')
