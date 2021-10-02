def mi_funcion(nombre):
    return "Hola que tal " + nombre

def mi_funcion2(apellidos):
    return "Hola que tal 2 " + apellidos

nombre = input("¿Cual es tu nombre?: ")
apellidos = input("¿Cual es tu apellido?: ")

print("Hola mundo")
print(f"Bienvenido {nombre}")
print(mi_funcion(nombre))
print(mi_funcion2(apellidos))