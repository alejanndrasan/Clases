from hashlib import new


class Car():
    def __init__(self, mark, driver):
        self.__mark = mark
        self.__driver = driver
    def getDriver(self):
        return self.__driver
    def getMark(self):
        return self.__mark
    def setDriver(self, newDriver):
        newDriver = self.__driver
        return newDriver
    def setMark(self, newMark):
        newMark = self.__mark
        return newMark

class CarHijo(Car):
    def __init__(self, mark, driver, carnet, materias):
        super().__init__(mark, driver)
        self.__carnet = carnet
        self.__materias = materias
    