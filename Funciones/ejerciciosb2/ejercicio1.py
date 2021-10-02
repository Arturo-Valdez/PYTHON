"""
Hacer un programa que tenga una lista de 8 numeros enteros y
haga lo siguiente:
-Recorrer la lista y mostrarla
-ordenarla y mostrarla
-mostrar su longitud
-buscar algun elemento(que el usuario pida por teclado)

"""
#Crear lista
listas = [1,5,78,41,56,45,241,23]

#Crear duncion que recorra lista y devuelva string
def mostrarlista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado
    
#Recorrer y mostrar
print("####### recorrer y mostrar #######")

"""
for lista in listas:
    print(lista)
"""
print(mostrarlista(listas))

#Ordenar y mostrar
listas.sort()
print("#### Ordenado ####\n")
print(mostrarlista(listas))

#Mostrar longitud
print("#### Mostrar longitud ####\n")
print("La longitud es:", len(listas))

#def otrointento():


#Busqueda en la lista
print("#### Busqueda ####\n")
busqueda = int(input("Introdusca un numero para mostrar: "))
comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introdusca un numero para mostrar: "))
    
else:
    print(f"Has introducido el {busqueda}")

print(f"####### Buscar en la lista el numero {busqueda} ########\n")
try:
    search = listas.index(busqueda)#index buscara en listas si se encuentra en la lista
    print(f"El numero buscado existe en la lista, es el indice: {search}")
except:
    print("No se encuentra en la lista")
    

