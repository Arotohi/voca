import csv
class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_csv()

    def read_csv(self):
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            data = [row for row in csv_reader]
        return data