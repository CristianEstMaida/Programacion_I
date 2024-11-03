from biblioteca import *

lista_numeros_enteros = cargar_lista("Ingrese un numero entero: ", 5, int)

valor_maximo = identificar_valor_maximo(lista_numeros_enteros)

print(f"El numero mas alto es {valor_maximo}")