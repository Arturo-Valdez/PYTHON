"""
Listas(arrays)
son colecciones o conjunto de datos/valores, bajo un unico nombre

para acceder a esos valores podemos usar un indice numerico
"""

pelicula = "Batman"
peliculas = ["Batman", "spiderman", "El señor de los anillos"]
cantantes = list(("2pac", "drake", "jennifer"))
years = list(range(2020,2050))
variada = ["santiago", 30 , 4.5, True, "texto"]

print(peliculas)
print(cantantes)
print(years)
print(variada)

#indice
peliculas[1]= "gran torino"#cambiar de nombre en la lista o renombrar
peliculas[2] = "el hobitt"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:3])#muestra rango en el cual mostrara los cantantes
print(peliculas[1:])#mostrar desde la pelicula 1 a lo que alla creado

#añadir elemento a la lista
cantantes.append("Kase O")#append sirve para agregar un elemento en un listado
print(cantantes)

#Recorrer lista

nueva_peli = ""
while nueva_peli != "Parar":#si es diferente a  Parar sale del continua y si es asi sale
    nueva_peli = input("Introduce la nueva pelicula: ")
    peliculas.append(nueva_peli)#la funcion append sirve para añadir los nuevos datos
    
    if nueva_peli != "Parar":
        peliculas.append(nueva_peli)


print("\n################## Listado Peliculas #############")
for pelicula in peliculas:#mientras se queda en evento de pelicula ve interando en peliculas
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")#index enumera pelicula

#Listas multidimensionales
print("\n################## Listado de contactos #############")
contactos = [
    [
        'Antonio',
        'antonio@.com'
    ],
    [
        'Luis',
        'luis@.com'
    ],
    [
        'Salvador',
        'salvador@.com'
    ]
]
#print(contactos[1][1])#Mostar el contacto 1 y el dato 1 que es el correo

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

