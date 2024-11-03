from biblioteca import *

lista_sueldos = cargar_lista("Ingrese numeros: ", 7, float)
lista_promedio = calcular_promedio(lista_sueldos)
mostrar_lista(lista_sueldos)
print(f"El promedio de los sueldos es de: {lista_promedio}")