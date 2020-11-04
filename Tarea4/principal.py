from trabajadores import Trabajador
from Arrays import Array

class Empleado:
    def __init__(self):
        self.__data = None

    def cargar_datos(self, ruta_archivo):
        lista = []
        archivo = open(ruta_archivo, 'rt')
        for i in archivo.readlines():
            linea = []
            for j in i.strip().split(','):
                i.replace(' ', '')
                linea.append(j)
            lista.append(linea)

        archivo.close()

        self.__data = Array(len(lista)-1)
        # se calculan los sueldos
        for i in range(1, len(lista)):
            trabajador = Trabajador(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5], lista[i][6])
            trabajador.sueldos(trabajador)
        print("")

        # se determina la antigüedad
        mayor = 0
        menor = 1000000
        for i in range(1, len(lista)):
            a = int(lista[i][6])
            if (a > mayor):
                mayor = a

            if (a < menor):
                menor = a

        for i in range(1, len(lista)):
            if (int(lista[i][6]) == mayor):
                print(f"El Trabajador {lista[i][1]} es el de mayor antiguedad {mayor}")
                print("")

            elif (int(lista[i][6]) == menor):
                print(f"El trabajador {lista[i][1]} es el de menor antiguedad {menor}")
                print("")


final = Empleado()
final.cargar_datos('junio.dat')