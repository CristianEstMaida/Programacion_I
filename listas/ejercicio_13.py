from biblioteca import *

lista_enteros = cargar_lista(5,"Ingrese un entero: ", int)
numero_mas_chico = identificar_valor_minimo(lista_enteros)
indice_numero_minimo = posicion_numero_minimo(lista_enteros, numero_mas_chico)
print(f"El numero mas chico es {numero_mas_chico} y su indice es {indice_numero_minimo}")