from lib.adapter import *


class UserInterface1(object):

    def __init__(self, target):
        self.__target = target

    def show(self):
        self.__target.show()

    def save(self, name):
        self.__target.save(name)
