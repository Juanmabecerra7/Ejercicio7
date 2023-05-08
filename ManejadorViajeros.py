from Viajero import Viajero
import csv


class ManejadorViajero:
    def __init__(self):
        self.__listaviajero = []

    def agregarviajero(self, unviajero):
        self.__listaviajero.append(unviajero)

    def testViajeros(self):
        archivo = open("viajeros.csv")
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            num = (fila[0])
            dni = (fila[1])
            nombre = fila[2]
            apellido = fila[3]
            millas_acum = (fila[4])
            unviajero = Viajero(num, dni, nombre, apellido, millas_acum)
            self.agregarviajero(unviajero)
        archivo.close()

    def __str__(self):
        s = ""
        for viajero in self.__listaviajero:
            s = s + str(viajero) + "\n"
        return s

    def buscarViajero(self, numero):
        indice = 0
        valor = None
        bandera = False
        while not bandera and indice < len(self.__listaviajero):
            if self.__listaviajero[indice].getnum() == numero:
                bandera = True
                valor = indice
            else:
                indice = indice + 1
        return self.__listaviajero[valor]

    def mayores(self):
        maximo = self.__listaviajero[0].getmillas()
        for Viajero in self.__listaviajero:
            maximo = Viajero.__ge__(maximo)
        return maximo

    def mostarMayores(self, maximo):
        indice = 0
        p = ""
        while indice < len(self.__listaviajero):
            if int(self.__listaviajero[indice].getmillas()) == int(maximo):
                p = p + str(self.__listaviajero[indice]) + "\n"
            indice = indice + 1
        return str(p)

    def mostarIguales(self, entero):
        indice = 0
        p = ""
        bandera = ""
        while indice < len(self.__listaviajero):
            bandera = Viajero.__eq__(self.__listaviajero[indice], entero)
            if bandera:
                p = p + str(self.__listaviajero[indice]) + "\n"
            indice = indice + 1
        return str(p)
