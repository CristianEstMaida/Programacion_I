from biblioteca import *

lista_alturas = cargar_lista("Ingrese una altura: ", 5, float)
promedio_alturas = calcular_promedio(lista_alturas)
contador_superen_promedio = contar_superen_promedio(lista_alturas, promedio_alturas)

print(f"El total de personas que superan el promedio {promedio_alturas} es: {contador_superen_promedio}")