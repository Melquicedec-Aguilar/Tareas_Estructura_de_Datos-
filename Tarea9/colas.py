class Queue:
    def __init__(self):
        self.__data = list()  #también se puede así []

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def enqueue(self, elem):
        self.__data.append(elem)

    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "| " + str(elem)
        cadena = cadena + "|"
        return cadena

#Cola con prioridad no ACOTADA
class PriorityQueue:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def enqueue(self, prioridad, elem):
        pos = 0
        for lista in self.__data:
            if prioridad >= lista[0]:
                pos += 1

        if self.is_empty():
            self.__data.append((prioridad,elem))

        else:
            self.__data.insert(pos, (prioridad, elem))

    def dequeue(self):
        self.__data.pop(0)

    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "| " + str(elem)
        cadena = cadena + "|"
        return cadena
