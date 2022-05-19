from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        all_files = cls.file_type(path)

        if report_type == 'simples':
            return SimpleReport.generate(all_files)
        if report_type == 'completo':
            return CompleteReport.generate(all_files)
        else:
            return 'Error: Tipo de relatório inválido'

    def file_type(path):
        if '.csv' in path:
            return CsvImporter.import_data(path)
        if '.json' in path:
            return JsonImporter.import_data(path)
        if '.xml' in path:
            return XmlImporter.import_data(path)
