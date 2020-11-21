class Nodo:
    def __init__( self , value , siguiente= None):
        self.data = value               #Falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__( self ):
        self.__head = None

    def is_empty( self ):
        return self.__head == None

    def append( self , value ):
        nuevo = Nodo( value )
        if self.__head == None:          #puede ser sustituido por self.is_empty()
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

    def tranversal ( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} --> ", end="")
            curr_node = curr_node.siguiente
        print('')

    def remove( self , value ):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
        else:
            temporal = None
            while curr_node.data != value and curr_node.siguiente != None:
                temporal = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                temporal.siguiente = curr_node.siguiente
            else:
                print("El dato no existe en la lista")

    def preppend( self, value ):
        nuevo = Nodo( value, self.__head )
        self.__head = nuevo

    def tail(self):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def get( self, posicion= None ):       #por defecto regresa el último
        curr_node = self.__head
        contador = 0
        dato = None
        if posicion == None:
            dato = self.tail()
        else:
            while contador <= posicion:
                if curr_node != None:
                    dato = curr_node
                    curr_node = curr_node.siguiente

                else:
                    print(f"Fuera de rango, la ultima posicion es {contador-1}")
                    print(f"Su ultimo valor es {dato.data}")
                    contador = posicion

                contador+=1
        return dato.data

    def Add_before ( self, reference_value, value):         #Agrega el valor antes de la primera coincidencia, si no encuentra la referencia no hace la insercción
        curr_node = self.__head
        nuevo = Nodo(value)
        tmp = None

        if self.__head.data == reference_value:
            self.__head = nuevo

            while curr_node.siguiente != None:
                tmp = curr_node.data
                self.append(tmp)
                curr_node = curr_node.siguiente
            self.append(curr_node.data)

        else:
            while (curr_node.data != reference_value) and (curr_node.siguiente != None):
                tmp = curr_node
                curr_node = curr_node.siguiente

            if curr_node.data == reference_value:
                tmp.siguiente = nuevo
                while curr_node.siguiente != None:
                    tmp = curr_node.data
                    self.append(tmp)
                    curr_node = curr_node.siguiente
                self.append(curr_node.data)
            else:
                print("No se encontro el valor de la referencia")

    def Add_after(self, reference_value, value):        #Agrega el valor despues de la referencia
        curr_node = self.__head
        nuevo = Nodo(value)
        tmp = self.tail().data

        while (curr_node.data != reference_value) and (curr_node.siguiente != None):
            curr_node = curr_node.siguiente

        if curr_node.siguiente != None:
            curr_node = curr_node.siguiente
            self.Add_before(curr_node.data, value)

        elif reference_value == tmp:
            self.append(nuevo.data)

        else:
            print("No se encontro el valor de la referencia")
