from homework.aleksei_mishin.lesson_13.date_and_time import DateAndTime


class File:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read_date_from_file()

    def read_date_from_file(self):
        result = []

        with open(self.filepath) as file:
            for line in file:
                result.append(DateAndTime(line))

        return result
