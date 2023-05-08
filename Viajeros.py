class Viajero:
    __num = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = ""

    def __init__(self, num, dni, nombre, apellido, millas_acum):
        self.__num = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def getnum(self):
        return int(self.__num)

    def getmillas(self):
        return int(self.__millas_acum)

    def __ge__(self, otro):
        maximo = 0
        if int(self.__millas_acum) >= int(otro):
            maximo = int(self.__millas_acum)
        else:
            maximo = int(otro)
        return maximo

    def __eq__(self, otro):
        return int(self.__millas_acum) == int(otro)

    def __radd__(self, otro):
        self.__millas_acum = int(otro) + int(self.__millas_acum)
        return str("{}, {}, {}, {}, {}").format(self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)

    def __rsub__(self, otro):
        self.__millas_acum = int(otro) - int(self.__millas_acum)
        return str("{}, {}, {}, {}, {}").format(self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)

    def __str__(self):
        return str("{},{},{},{},{}").format(self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)
