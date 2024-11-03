"""Parte teorica -> 60% para aprobar (acceden al práctico)    multiple choise. 30 min.
Repasen las ppts!

Parte practica -> 3hs hasta las 22:15 se entrega por MOODLE (campus virtual)!
Se entregan 2 archivos .py! (Biblioteca con funciones y archivo principal (main))
Deben tener camara, microfono y poder compartir pantalla

APROBACION NO DIRECTA:
4 o 5 como minimo en cada uno de los 2 examenes parciales (Se debe rendir final)
Se puede levantar nota en los recuperatorios.

APROBACION DIRECTA (PROMOCION):
6 o mas en cada uno de los 2 examenes parciales (No se rinde final)

NO SE ADMITE: Plagio, ChatGPT, Google!
Permitido: utilizar y ver los ejemplos de ejercicios que se hicieron en clase y
cualquier funcion propia.

Apellido y Nombre: Maida Cristian Esteban
Asignatura: Programacion I
Division: 312
Fecha: 08/10/2024
Instancia: Primer Parcial

"""

import os
from biblioteca import *

bandera = False
bandera_5 = False
lista_aleatoria = []
lista_caracteres = []
lista_ordenada = []
lista_caracteres = []
lista_cantidad_repetidos = []

while True:
    opcion_seleccionada = input(crear_menu())
    # os.system("cls")
    match opcion_seleccionada:
        case "1":
            lista_aleatoria = cargar_lista_aleatoria(500, 48, 57, 65, 90)
            bandera = True
        case "2":
            if bandera == True:
                lista_ordenada = ordenar_lista(lista_aleatoria)
            else:
                print("Primero se debe generar una lista de manera aleatoria")
        case "3":
            if bandera == True:
                lista_caracteres = filtar_lista_letras(lista_ordenada)
                lista_cantidad_repetidos = encontrar_caracteres_repetidos(lista_caracteres)
                mostrar_cabecera("CARACTER", "CANTIDAD")
                print("--------------------------")
                mostrar(lista_caracteres, lista_cantidad_repetidos)
            else:
                print("Primero se debe generar una lista de manera aleatoria")
        case "4":
            if bandera == True:
                caracter_mas_repetido = encontrar_caracter_repetido(lista_cantidad_repetidos, "max")
                mayor = identificar_valor_maximo(lista_cantidad_repetidos)
                caracter_menos_repetido = encontrar_caracter_repetido(lista_cantidad_repetidos, "min")
                menor = identificar_valor_minimo(lista_cantidad_repetidos)
                mostrar_dato(f"El caracter mas repetido es {caracter_mas_repetido} y se repite {mayor} veces")
                mostrar_dato(f"El caracter menos repetido es {caracter_menos_repetido} y se repite {menor} veces")
            else:
                print("Primero se debe generar una lista de manera aleatoria")
        case "5":
            matriz = crear_matriz_aleatoria(10, 10, 10, 999)
            bandera_5 = True
        case "6":
            if bandera_5 == True:
                lista_enteros = cargar_lista_enteros("Ingrese un numero", 10, 999)
                
                flag = determinar_matriz_secuencia(matriz, lista_enteros)
                if flag == True:
                    print("La secuencia numerica ", end="")
                    mostrar_lista_formateada(lista_enteros)
                    print("existe en la matriz")
                else:
                    print("La secuencia numerica ", end="")
                    mostrar_lista_formateada(lista_enteros)
                    print("no existe en la matriz")
            else:
                print("Primero se debe generar la matriz")

        case "7":
            break
        case _:
            print("Error, opcion incorrecta")

print("Programa terminado")