from Viajero import Viajero
from ManejadorViajero import ManejadorViajero


if __name__ == '__main__':
    mv = ManejadorViajero()
    mv.testViajeros()
    print(str(mv))
    numero = int(input("Ingrese el numero de un viajero: "))
    while numero != 0:
        unviajero = mv.buscarViajero(numero)
        if unviajero is None:
            print("----El viajero no existe----")
        else:
            while numero != 0:
                print("1. Consultar Cantidad de Millas")
                print("2. Acumular Millas")
                print("3. Canjear Millas")
                print("4. Elegir Otro Viajero")
                print("5: Viajeros con mayor millas")
                print("6: Comprar Millas con un valor")
                print("7. Salir")
                opcion = int(input())
                if opcion == 1:
                    print(Viajero.cantidadTotalMillas(unviajero))
                elif opcion == 2:
                    millas = int(input("Ingrese la cantidad de millas a sumar: "))
                    print(Viajero.__radd__(unviajero, millas))
                elif opcion == 3:
                    canjear = int(input("Ingrese la cantidaad de millas a canjear: "))
                    print(Viajero.__rsub__(unviajero, canjear))
                elif opcion == 4:
                    numero = 0
                elif opcion == 5:
                    maximo = mv.mayores()
                    print(f"Los viajeros con mayor millas son: ")
                    print(str(mv.mostarMayores(maximo)))
                elif opcion == 6:
                    entero = int(input("Ingrese un numero entero para comprar: "))
                    print(f"Los viajeros con millas iguales al numero ingresado son: ")
                    print(str(mv.mostarIguales(entero)))
                elif opcion == 7:
                    exit()
                else:
                    print("----Opcion Invalida----")
        numero = int(input("Ingrese el numero de un viajero: "))
