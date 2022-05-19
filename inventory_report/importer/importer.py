from abc import abstractmethod


class Importer:
    def __init__(self):
        pass

    @abstractmethod
    def import_data(file):
        pass
