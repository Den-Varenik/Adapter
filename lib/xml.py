import xml.etree.ElementTree as ET


class XmlParser(object):

    def __init__(self, file):
        self.__file = file
        self._data_xml = self.__open_xml()

    def __open_xml(self):
        return ET.parse(self.__file)

    def show(self):
        for i in self._data_xml.getroot():
            print(i.tag, i.attrib)
            for y in i:
                print(y.tag, y.attrib)

    def save(self, name: str):
        name += '.xml'
        self._data_xml.write(name)
