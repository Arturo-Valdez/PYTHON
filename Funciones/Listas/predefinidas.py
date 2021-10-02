cantantes = ["2Pac", "Drake", "Vicente Fernandes", "Julion Alvarez"]
numeros = [1,8,4,5,7,6]

#Ordenar
print(numeros)
numeros.sort()#La funcion sort sirve para ordenar 
print(numeros)

#Agregar elementos a una lista
cantantes.append("Natos y Waor")

cantantes.insert(1,"David")#La funcion insert sirve para agregar y colocar el orden donde quiere ese elemento
print(cantantes)

#Eliminar cantantes
cantantes.pop(1)#La funcion pop sirve para eliminar un elemento
cantantes.remove("Drake")
print(cantantes)

#Dar la vuelta a la lista
print(numeros)
numeros.reverse()#La funcion reverse sirve para cambiar el orden o voltear
print(numeros)

#Buscar dentro de una lista
print("Julion Alvarez" in cantantes)#esta Julion Alvarez en cantantes, muestra falso o verdadero

#Contar elementos
print(len(cantantes))

#Cuantas veces aparece un elemento en lista
numeros.append(8)
print(numeros.count(8))

#Conseguir indice
print(cantantes.index("Julion Alvarez"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)
