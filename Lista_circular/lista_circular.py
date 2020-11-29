class NodoCircular:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class CircularList:
    def __init__(self):
        self.__ref = None

    def is_empty(self):
        return self.__ref == None

    def insert(self, value):
        nuevo = NodoCircular(value)
        tmp = None
        if self.is_empty():                     #si la lista circular esta vacía
            self.__ref = nuevo
            self.__ref.next = self.__ref

        elif self.search(value):                #Comprueba que no exista un valor dentro de la lista
            print(f"El valor {value} ya existe dentro de la lista")

        else:
            curr_node = self.__ref
            if value > curr_node.data:          #si se agrega un valor mayor al que ya existía
                tmp = self.__ref
                curr_node = self.__ref.next
                tmp.next = nuevo
                self.__ref = tmp.next
                self.__ref.next = curr_node

            else:
                tmp = curr_node.next
                if value <= curr_node.next.data:    #se agrega un valor menor que los existentes
                    self.__ref.next = nuevo
                    curr_node.next.next = tmp

                else:                               #Se agrega en la parte media de la lista
                    curr_node = curr_node.next
                    while value > curr_node.data:      #se utiliza este while para ver la posicion en la que se agrega
                        tmp = curr_node
                        curr_node = curr_node.next
                    tmp.next = nuevo

                    while curr_node != self.__ref:      #en este while se agrega haciendo que los demas nodos se recorrán
                        tmp.next.next = curr_node
                        curr_node = curr_node.next
                        tmp = tmp.next
                    tmp.next.next = curr_node
                    self.__ref = curr_node

    def transversal(self):
        curr_node = self.__ref.next
        while curr_node != self.__ref:
            print(f"{curr_node.data} --> ", end="")
            curr_node = curr_node.next
        print(f"{self.__ref.data} --> {self.__ref.next.data} --> {self.__ref.next.next.data}")

    def search(self, value):
        curr_node = self.__ref.next
        bol = False
        while (curr_node != self.__ref) and (curr_node.data != value):
            curr_node = curr_node.next

        if curr_node.data == value:
            bol = True
        else:
            bol = False
        return bol

    def remove(self, value):
        curr_node = self.__ref.next
        tmp = None
        if self.search(value):
            if value == self.__ref.data:
                while curr_node != self.__ref:
                    tmp = curr_node
                    curr_node = curr_node.next
                curr_node = self.__ref.next
                self.__ref = tmp
                self.__ref.next = curr_node
            elif value == self.__ref.next.data:
                curr_node = curr_node.next
                self.__ref.next = curr_node
            else:
                while curr_node.data != value:
                    tmp = curr_node
                    curr_node = curr_node.next
                curr_node = curr_node.next
                tmp.next = curr_node

        else:
            print(f'No existe el valor {value} que desea eliminar')
