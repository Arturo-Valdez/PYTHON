"""
Crear un script que tenga 4 variables, una lista, un string, un entero,
un booleano y que imprima un mensaje segun el tipo de cada variable.
usar funciones
"""
def traduciortipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == int:
        result = "Entero"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == bool:
        result = "Booleano"
    return result


def comprobartipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""
    if test:
        print(f"Este dato es del tipo {traduciortipo(tipo)}")
    else:
        result = None
    return result


    
mi_lista = ["Hola mundo", 77]
titulo = "Master"
numero = 100
verdadero = True
print(comprobartipado(mi_lista, list))
print(comprobartipado(numero, int))
print(comprobartipado(titulo, str))
print(comprobartipado(verdadero, bool))