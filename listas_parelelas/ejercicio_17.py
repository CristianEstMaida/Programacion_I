from biblioteca import *

lista_nombres = []

lista_precios = []

cargar_listas_paralelas(5, "Ingrese el nombre del producto: ", "Ingrese el precio del producto: ", lista_nombres, lista_precios, 0, 0, 0, 999, str, float)

mayores_a_primer_valor = contar_mayor_que_primero(lista_precios)

print(f"La cantidad de productos que superan el precio del primer producto es de: {mayores_a_primer_valor}")