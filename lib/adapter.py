from lib.xml import *
from lib.json import *


class Adapter(JsonParser, XmlParser):

    def __init__(self, xml_file, json_file):
        XmlParser.__init__(self, xml_file)
        JsonParser.__init__(self, json_file)
        self.__big_json_data = self.__big_json()
        self.__big_xml_data = self.__to_xml()

    def show(self):
        print('Адаптер только сохраняет данные их разных форматов в один!')

    def save(self, name):
        answer = input('Выберите формат для сохранения данных:\n'
                       '1 ".json"\n'
                       '2 ".xml"\n'
                       '- ')
        if answer == '1':
            name += '.json'
            with open(name, 'w', encoding='utf-8') as f:
                dump(self._data_json, f, indent=4)
        elif answer == '2':
            name += '.xml'
            self.__big_xml_data.write(name)
        else:
            print('Неверный выбор')

    def __to_json(self) -> list:
        target = []
        for contact in self._data_xml.getroot():
            contact_dict = contact.attrib
            contact_dict.update({'phone': dict([self.__dict_to_list(phone.attrib) for phone in contact])})
            target.append(contact_dict)
        return target

    def __big_json(self):
        big_data = self._data_json
        big_data['phoneBook'] = big_data['phoneBook'] + self.__to_json()
        return big_data

    def __to_xml(self):
        big_data = self._data_xml
        element = big_data.getroot()
        for contact in self._data_json['phoneBook']:
            contact_with_atr = []
            for obj in self.__dict_to_list(contact):
                contact_with_atr.append(obj if type(obj) != dict else list(zip(list(obj), self.__dict_to_list(obj))))
            new_contact = ET.SubElement(element, 'contact')
            new_contact.set('name', contact_with_atr[0])
            for cont in contact_with_atr:
                if type(cont) is list:
                    for attrib in cont:
                        phone = ET.SubElement(new_contact, 'phone')
                        phone.set('type', attrib[0])
                        phone.set('phone', attrib[1])
        return big_data

    @staticmethod
    def __dict_to_list(target: dict) -> list:
        return [item for key, item in target.items()]
