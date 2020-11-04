class Array:
    def __init__(self , tam):
        self.__info = [0 for x in range(tam)]

    def get_item( self , posicion):
        try:
            dato = self.__info[posicion]
        except Exception as e:
            print("Error de posicion")
        return dato

    def set_item(self, dato, posicion):
        try:
            self.__info[posicion] = dato
        except Exception as e:
            print("Error de posicion")

    def get_length(self):
        return len(self.__info)


    def __iter__(self):
        return IteradorArreglo(self.__info)


class IteradorArreglo:
    def __init__(self, arr):
        self.__arr = arr
        self.__indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else:
            raise StopIteration
