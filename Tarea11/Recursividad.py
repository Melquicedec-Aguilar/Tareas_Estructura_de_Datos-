from pila import Stack

#Crear una lista de enteros en Python y realizar la suma con recursividad, el
#caso base es cuando la lista este vacia.

def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]

    else:
        return lista.pop() + suma_lista(lista)

def main():
    datos = [5,7,9,15,8]
    resultado = suma_lista(datos)
    print(resultado)
    print("-------------------------------------------------------------------")

main()

#Hacer un contador regresivo con recursión

def contador_regresivo(numero):
    if numero > 0:
        print(numero)
        contador_regresivo(numero - 1)

def main1():
    numero = 8
    contador_regresivo(numero)
    print("-------------------------------------------------------------------")

main1()

#Sacar de un ADT pila el valor de la posición media

def posicion_media(pila, media, pos):
    if pos < media:
        x = pila.pop()
        posicion_media(pila, media, pos+1)
        if pos != media-1:
            pila.push(x)

def main2():
    pila = Stack()
    #pila.push(4)
    pila.push(3)
    pila.push(2)
    pila.push(10)
    pila.push(5)
    pila.push(6)
    pila.push(2)
    print("--------------------Pila original----------------------------")
    pila.to_string()
    print()
    posicion_media(pila, round(pila.length() / 2), 0)
    print("-----------------Pila sin el elemento de la posición media------------------")
    pila.to_string()

main2()
