# 15) Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir
# si dicho valor se encuentra en 2 o más posiciones en la lista)

from biblioteca import *

lista_cargada = cargar_lista("Ingrese un numero entero: ", 5, int)
valor_maximo = identificar_valor_maximo(lista_cargada)
cantidad_repetidos = determinar_repetidos(lista_cargada, valor_maximo)
print(f"El valor maximo es: {valor_maximo}")
if cantidad_repetidos >= 2:
    print(f"Se repetio el maximo {cantidad_repetidos} veces")