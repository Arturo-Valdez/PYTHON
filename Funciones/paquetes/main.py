#__init__.py sirve para decirle al sistema que es un paquete, una agrupacion de modulos
#No tienes que agregar nada, creara un archivo cache
print("PROBANDO PAQUETES:")

from mipaquete import pruebas
from mipaquete import herramientas

pruebas.probando()
herramientas.nombrecompleto("Santiago", "Valdez")