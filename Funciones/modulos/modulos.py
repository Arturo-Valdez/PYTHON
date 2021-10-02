"""
Modulos: Son funcionalidades ya hechas para reutilizar

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html#cap-m

Podemos conseguir modulos que ya vienen en el lenguaje. 
modulos en internet y tambien podemos crear modulos
"""
#Importar modulo propio
#import mimodulo

#print(mimodulo.holamundo("Santiago"))
#print(mimodulo.calculadora(3,5,True))


#Segunda forma de importar un modulo predeterminado de mimodulo importar holamundo
#from mimodulo import holamundo
#print(holamundo("Santiago"))

#Terser forma de importar modulos, el * significa todo modulo que contenga el fragmento de mimodulos
#from mimodulo import *
#print(holamundo("Santiago"))
#print(calculadora(3,5,True))

#Modulos de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)#Muestra dia,mes,año, y hora
print(fecha_completa.year)#Muestra el año que nos encontramos
print(fecha_completa.month)#Muestra el mes
print(fecha_completa.day)#Muestra el dia

fecha_personalizada = fecha_completa.strftime("%A/%d/%m/%Y, %H:%M:%S")#Formatear fecha
print("Mi fecha personalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp)

#modulo matematicas
import math
print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", float(math.pi))
print("Redondear: ", math.floor(6.54612))

#Modulo ramdom (aleatorio)
import random
print("Numero aleatorio entre 15 y 57: ", random.randint(15,67))
