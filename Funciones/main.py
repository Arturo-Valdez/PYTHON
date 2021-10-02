"""
#FUNCIONES
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando a la funcion tanta veces como sea nesesario.

Def nombreDeMiFuncion(parametros):
    #Bloque / conjunto de instrucciones

nombreDeMiFuncion(mi_parametro)
"""
#Ejemplo 1

print("###### EJEMPLO 1 ########")
##Definir funcion
def muestranombre():
    print("victor")
    print("Carlos")
    print("Manuel")
    print("Ulices")
    print("\n")

##Invocar funcion
muestranombre()

print("\n###### EJEMPLO 1 ########\n")

def mostrartuname(nombre, edad):
    print(f"Tu nombre es {nombre}")
    
    if edad >=18:
        print("y eres mayor de edad")
    else:
        print("Eres menor de edad")

nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
mostrartuname(nombre,edad)

print("\n###### EJEMPLO 3 ########\n")
def tabla(numero):
    print(f"Tabla de multiplicar del numero {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")
resultado = int(input("Dime cual tabla quieres: "))
tabla(resultado)

print("\n###### EJEMPLO 4 ########\n")

#Parametros obsionales
def getempleado(nombre, dni):
    print("empleado")
    print(f"nombre: {nombre}")
    print(f"DNI: {dni}")
getempleado("Arturo" , "7465285285")

print("\n###### EJEMPLO 5 ########\n")

#Parametros opcionales y return o devolver datos
def calculadora(numero1, numero2, basicas= False):
    suma = numero1 + numero2
    resta = numero1  - numero2
    mult = numero1*numero2
    divi = numero1/numero2

    cadena= ""
    cadena+= "Suma: " + str(suma)
    cadena += "\t"
    cadena+= "Resta: " + str(resta)
    cadena += "\t"
    cadena+= "Multiplicacion: " + str(mult)
    cadena += "\t"
    cadena+= "Division: " + str(divi)
    
    return cadena

print(calculadora(5,5))

print("\n###### EJEMPLO 6 ########\n")

def getNombre(nombre):
    texto= f"el nombre es: {nombre}"
    return texto

def getapellidos(apellidos):
    texto = f"los apellidos son: {apellidos}"
    return texto
def devuelve(nombre,apellidos):
    texto = getNombre(nombre) + "\t"+ getapellidos(apellidos)
    return texto
print(devuelve("jose", "Gonzalez"))

print("############# Ejercicio 8 ##########")

dime_el_year = lambda year: f"el año es {year}"

print(dime_el_year(3145))
