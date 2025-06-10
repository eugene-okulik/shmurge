import csv


class Files:

    def __init__(self, filepath):
        self.filepath = filepath
        self.filetype = self.filepath[-4:]

    def read_csv_file(self):
        with open(self.filepath, newline='') as file:
            file_data = csv.DictReader(file)
            return list(map(lambda x: x, file_data))
