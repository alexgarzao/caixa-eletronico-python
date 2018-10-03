class CashNote:
    def __init__(self, value, used=0):
        self.__value = value
        self.__used = used

    def value(self):
        return self.__value

    def inc_used(self):
        self.__used += 1

    def used(self):
        return self.__used

    def __eq__(self, other):
        return(self.value() == other.value() and self.used() == other.used())
