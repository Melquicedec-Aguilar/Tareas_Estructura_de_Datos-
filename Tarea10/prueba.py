from colas import Queue,BoundedPriorityQueue

print("------------PRUEBAS DE LAS COLAS CON PRIORIDAD ACOTADA-------------")
print()

maestres = {"prioridad":4, "descripcion":"Maestre", "personas":["Juan p", "Diego h"]}
ninos = {"prioridad":2, "descripcion":"Niños", "personas":["Santi h", "Angel h"]}
mecanicos = {"prioridad":4, "descripcion":"Mecanicos", "personas":["Diana t", "Maria z"]}
mujeres = {"prioridad":3, "descripcion":"Mujeres", "personas":["Fernanda", "Mariana"]}
Tercera_Edad = {"prioridad":2, "descripcion":"3er Edad", "personas":["Francisco", "Veronica"]}
ninas = {"prioridad":1, "descripcion":"Ninas", "personas":["Ana", "Daniela"]}
Hombres = {"prioridad":3, "descripcion":"Hombres", "personas":["Luis", "Mauricio"]}
vigia = {"prioridad":4, "descripcion":"Vigia", "personas":["Carlos", "Ricardo"]}
Capitan = {"prioridad":5, "descripcion":"Capitan", "personas":["Javier"]}
timonel = {"prioridad":4, "descripcion":"Timonel", "personas":["Antonio"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(ninos['prioridad'], ninos)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(Tercera_Edad['prioridad'], Tercera_Edad)
cpa.enqueue(ninas['prioridad'], ninas)
cpa.enqueue(Hombres['prioridad'], Hombres)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(Capitan['prioridad'], Capitan)
cpa.enqueue(timonel['prioridad'], timonel)
cpa.to_string()
print("-----------------------------------------------------------------------------------------------------------------")
print()
for cola in range(cpa.length()):
    print(f"Estan abandonando el barco: {cpa.dequeue()['descripcion']}")
print()
print("Ha sido evacuado el barco por completo")
print("-----------------------------------------------------------------------------------------------------------------")
print()
cpa.to_string()
