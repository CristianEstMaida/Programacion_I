from biblioteca import *

lista_nombres = cargar_palabras_en_lista("Ingrese un nombre: ", 4)

cantidad_nombres = contar_caracteres(lista_nombres, 5)

print(f"La cantidad de nombres con 5 o más caracteres son: {cantidad_nombres}")