from biblioteca import *

lista_nombres = cargar_lista(5, "Ingrese nombre: ", str)

nombre_mas_corto = identificar_string_mas_corto(lista_nombres)
print("El nombre mas corto es: ", nombre_mas_corto)