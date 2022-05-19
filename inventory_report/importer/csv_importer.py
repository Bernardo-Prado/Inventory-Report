import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if path.split('.')[1] != 'csv':
            raise ValueError("Arquivo inválido")
        else:
            with open(path, 'r') as file:
                reader = list(csv.DictReader(file))
                return reader
