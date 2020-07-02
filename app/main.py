from lib.interface import *
from lib.xml import *


if __name__ == '__main__':
    int1 = UserInterface1(XmlParser('contact_xml.xml'))
    int1.show()
    UserInterface1(JsonParser('contact_json.json')).show()
    UserInterface1(Adapter('contact_xml.xml', 'contact_json.json')).save('kuku')
