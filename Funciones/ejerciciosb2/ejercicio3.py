"""
Programa que compruebe si una variable esta vacia y si esta vacia
, rellenarla con texto en munusculas y mostrarlo en mayusculas

"""

texto = ""

if len(texto.strip()) <= 0:#strip sirve para eliminar espacios
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")