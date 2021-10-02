"""
Crear una lista con el contenido de tabla
"""

peliculas_lista = [
    {
        "Categoria": "ACCION",
        "Juegos": ["GTA","COD","PUGB"]
    },
    {
        "Categoria": "AVENTURA",
        "Juegos": ["ASSINS","CRASH","Prince of Percia"]
    },
    {
        "Categoria": "DEPORTES",
        "Juegos": ["FIFA21","PRO 21","MOTO GP 21"]
    }
]

for Categoria in peliculas_lista:
    print(f"---------------{Categoria['Categoria']}--------------")
    for Juegos in Categoria['Juegos']:
        print(Juegos)

