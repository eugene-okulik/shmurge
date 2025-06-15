import os


class Logs:

    def __init__(self):
        self.dirpath, self.keyword = self.check_user_input()
        self.files_list = os.listdir(self.dirpath)
        self.files_list.sort()
        self.search_logs_from_file()

    @staticmethod
    def check_user_input():
        while True:
            user_input = input('Enter your search request: ')
            if '--text' not in user_input:
                print('Invalid request!')
                continue
            dirpath, keyword = user_input.replace(' ', '').split('--text')
            if os.path.isdir(dirpath):
                return dirpath, keyword
            else:
                print('Directory not found!')

    def parse_error_string(self, file_name: str, line_num: int, data_list: list):
        ind = data_list.index(self.keyword.upper())
        return f"file({file_name}) - line({line_num}) msg: {data_list[ind - 1]} {data_list[ind]} {data_list[ind + 1]}"

    def search_logs_from_file(self):
        for file_name in self.files_list:
            filepath = self.dirpath + file_name
            line_cnt = 1

            with open(filepath) as file:
                for line in file:
                    line = line.split()
                    if self.keyword.upper() in line:
                        print(self.parse_error_string(file_name, line_cnt, line))
                    line_cnt += 1
