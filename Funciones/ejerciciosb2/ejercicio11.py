"""
#Multiples excepciones
try:
    numero = int(input("Numero elevado al cuadrado es: "))
    print("El cuadrado es " + str (numero*numero))
except TypeError:
    print("Debes convertir tu cadena a enteros en el codigo")
except ValueError:
    print("Introduce un numero correcto!!")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)
    """

#Excepciones personalizadas
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 110:
      raise ValueError("La edad introducida no es real")
    elif len(nombre)<=1:
      raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido a master python {nombre} con una edad de {edad}")
except ValueError:
    print("Ingrese los datos correctamente!!")
except Exception as e:
    print("Existe un error: ", e)