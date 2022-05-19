import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        if path.split('.')[1] != 'xml':
            raise ValueError("Arquivo inválido")
        else:
            with open(path, 'r') as file:
                tree = ET.parse(file)
                root = tree.getroot()
                return [
                    {elem.tag: elem.text for elem in item} for item in root
                    ]

# https://www.studytonight.com/python-howtos/
# how-to-read-xml-file-in-python#:~:
# text=a%20single%20tree.-,Example%20Read%20XML%20File
# %20in%20Python,XML%20file%20using%20getroot()%20
