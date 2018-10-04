class CashNote:
    "Classe responsável por modelar uma nota específica."
    def __init__(self, value, used=0):
        self.__value = value
        self.__used = used

    def value(self):
        return self.__value

    def used(self):
        return self.__used

    def discount(self, value):
        used = int(value/self.value())
        self.__used += used
        return (used * self.value())

    def __eq__(self, other):
        return(self.value() == other.value() and self.used() == other.used())
