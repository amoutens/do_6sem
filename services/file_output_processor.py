import csv

class FileOutputProcessor:
    def process(self, file_path="ExampleOfCSVData/OutputDataCSV/output.csv", data=None):
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([data.s])
            for row in data.x:
                if isinstance(row, (list, tuple)):
                    writer.writerow(row)
                else:
                    writer.writerow([row])