import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if path.split('.')[1] != 'json':
            raise ValueError("Arquivo inválido")
        else:
            with open(path, 'r') as file:
                reader = json.load(file)
                return reader
