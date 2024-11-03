from biblioteca import *

lista_nombres_main = []
lista_edades_main = []

print(lista_nombres_main)
print(lista_edades_main)

cargar_listas_paralelas(5, "Ingrese nombre: ", "Ingrese edad: ", lista_nombres_main, lista_edades_main, 0, 0, 0, 120, str, int)
mostrar_mayores_que(lista_nombres_main, lista_edades_main, 18)

print(lista_nombres_main)
print(lista_edades_main)