from biblioteca import *

lista_numeros_a = []
lista_numeros_b = []

cargar_listas_paralelas(4, "Ingrese un numero: ", "Ingrese otro numero: ", lista_numeros_a, lista_numeros_b, 0, 999, 0, 999, int, int)

resultado = sumar_listas(lista_numeros_a, lista_numeros_b)

print(f"La lista resultante es: ")

mostrar_lista(resultado)