import os
from config import FILEPATH, KEYWORD


class Logs:

    def __init__(self):
        self.dirpath, self.keyword = self.check_user_input()
        self.files_list = os.listdir(self.dirpath)
        self.files_list.sort()
        self.search_logs_from_file()

    @staticmethod
    def check_user_input():
        if not os.path.isdir(FILEPATH):
            print('Incorrect filepath!')
            print(FILEPATH)
            exit()
        return FILEPATH, KEYWORD

    def parse_error_string(self, file_name: str, line_num: int, data_list: list):
        ind = data_list.index(self.keyword.upper())
        return f"file({file_name}) - line({line_num}) msg: {data_list[ind - 1]} {data_list[ind]} {data_list[ind + 1]}"

    def search_logs_from_file(self):
        for file_name in self.files_list:
            filepath = os.path.join(self.dirpath, file_name)
            line_cnt = 1

            with open(filepath) as file:
                for line in file:
                    line = line.split()
                    if self.keyword.upper() in line:
                        print(self.parse_error_string(file_name, line_cnt, line))
                    line_cnt += 1
