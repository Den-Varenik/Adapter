from json import dump, load


class JsonParser(object):

    def __init__(self, file):
        self.__file = file
        self._data_json = self.__open_json()

    def __open_json(self):
        with open(self.__file, 'r', encoding='utf-8') as file:
            return load(file)

    def show(self):
        print(self._data_json)

    def save(self, name):
        name += '.json'
        with open(name, 'w', encoding='utf-8') as f:
            dump(self._data_json, f, indent=4)
