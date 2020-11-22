class NodoDoble:
    def __init__(self, value, siguiente=None, anterior=None):
        self.data = value
        self.next = siguiente
        self.prev = anterior


class DoubleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def get_size(self):
        return self.__size-1

    def is_empty(self):
        return (self.__head == None) and (self.__tail == None)

    def append(self, value):
        nuevo = NodoDoble(value)

        if self.__head == None and self.__tail == None:
            self.__head = nuevo
            self.__tail = nuevo
            self.__size+=1
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            self.__tail = nuevo             #agrega el nuevo nodo al tail
            self.__tail.prev = curr_node    #se guarda curr_node en tail.prev
            curr_node.next = self.__tail

            self.__size+=1

    def transversal(self):#Recorrido desde head para impribir los nodos
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} --> ", end="")
            curr_node = curr_node.next
        print('')

    def reverse_transversal(self):#Recorrido desde tail hasta head
        curr_node = self.__tail
        while curr_node != None:
            print(f"{curr_node.data} <-- ", end="")
            curr_node = curr_node.prev
        print('')

    def find_from_tail(self, value):
        curr_node = self.__tail
        contador = self.get_size()

        while (curr_node.data != value) and (curr_node.prev != None):
            curr_node = curr_node.prev
            contador-=1

        if curr_node.data == value:
            contador = contador

        else:
            print("No existe el valor")
            contador = None

        return contador

    def find_from_head(self, value):
        curr_node = self.__head
        contador = 0

        while (curr_node.data != value) and (curr_node.next != None):
            curr_node = curr_node.next
            contador += 1

        if curr_node.data == value:
            contador = contador

        else:
            print("No existe el valor")
            contador = None

        return contador

    def remove_from_tail(self, value):
        curr_node = self.__tail

        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size -= 1

        else:
            tmp = None
            while (curr_node.data != value) and (curr_node.prev != None):
                tmp = curr_node
                curr_node = curr_node.prev

            if curr_node.data == value and curr_node != self.__head:
                tmp.prev = curr_node.prev
                curr_node.prev.next = tmp
                self.__size -= 1

            elif self.__head.data == value:
                self.__head = self.__head.next
                self.__head.prev = None
                self.__size -= 1

            else:
                print("El valor no existe en la lista doblemente ligada")

    def remove_from_head(self, value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size -= 1

        else:
            temp = None
            while (curr_node.data != value) and (curr_node.next != None):
                temp = curr_node
                curr_node = curr_node.next

            if (curr_node.data == value) and (curr_node != self.__tail):
                temp.next = curr_node.next
                curr_node.next.prev = temp
                self.__size -= 1

            elif self.__tail.data == value:
                self.__tail = self.__tail.prev
                self.__tail.next = None
                self.__size -= 1

            else:
                print("El valor no existe en la lista doblemente ligada")
