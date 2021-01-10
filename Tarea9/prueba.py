from colas import PriorityQueue


print()
print("------------PRUEBAS DE LAS COLAS CON PRIORIDAD NO ACOTADA-------------")
print()

cna = PriorityQueue()
cna.enqueue(4,"Maestre")
cna.enqueue(2,"Ninos")
cna.enqueue(4,"Mecanicos")
cna.enqueue(3,"Hombres")
cna.enqueue(4,"Vigia")
cna.enqueue(5,"Capitan")
cna.enqueue(4,"Timonel")
cna.enqueue(3,"Mujeres")
cna.enqueue(2,"3ra Edad")
cna.enqueue(1,"Ninas")
print(cna.to_string())
cna.dequeue()
print(cna.to_string())
cna.dequeue()
print(cna.to_string())

