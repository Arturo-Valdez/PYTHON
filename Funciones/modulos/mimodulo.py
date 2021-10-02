def holamundo(nombre):
    return f"Hola que tal estas, {nombre}"

def calculadora(numero1, numero2, basicas= False):
    suma = numero1 + numero2
    resta = numero1  - numero2
    mult = numero1*numero2
    divi = numero1/numero2

    cadena= ""

    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacion: " + str(mult)
    cadena += "\n"
    cadena += "Division: " + str(divi)
    return cadena