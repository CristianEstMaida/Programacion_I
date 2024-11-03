import os

from biblioteca import *

lista_nombres_main = []
lista_notas_main = []
lista_condiciones_main = []
bandera = False

while True:
    opcion_seleccionada = input(crear_menu())
    os.system("cls")
    
    match opcion_seleccionada:
        case "a":
            numero = solicitar_entero("Ingrese la cantidad total de alumnos: ")
            print("Se ingreso la cantidad total de alumnos")
            bandera = True
        case "b":
            if bandera == True:
                cargar_listas_paralelas(numero, "Ingrese nombre: ", "Ingrese nota: ", lista_nombres_main, lista_notas_main, 0, 0, 1, 10, str, int)
                print("Se ingresaron nombre y nota de cada alumno.")
            else:
                print("Primero se debe ingresar la cantidad total de alumnos")
        case "c":
            if bandera == True:
                lista_condiciones_main = evaluar_condicion(lista_notas_main)
                mostrar_cabecera()
                print("--------------------------")
                mostrar(lista_nombres_main, lista_notas_main, lista_condiciones_main)
            else:
                print("Primero se debe ingresar la cantidad total de alumnos")
        case "d":
            if bandera == True:
                lista_cantidad_main = contar_condicion(lista_condiciones_main)
                mostar_dato(f"{'Cantidad aprobados':10} {'Cantidad promocionados':5} {'Cantidad Reprobados':5}")
                print("--------------------------")
                mostrar_lista_formateada(lista_cantidad_main)
            else:
                print("Primero se debe ingresar la cantidad total de alumnos")
        case "e":
            break
        case _:
            print("Error, opcion incorrecta")

print("Programa terminado")