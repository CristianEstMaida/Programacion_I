import random

def crear_matriz_aleatoria(cantidad_filas:int, cantidad_columnas:int, desde:int, hasta:int)->list:
    '''
    Carga en un matriz números aleatorios.
    Recibe cantidad de filas, columnas, desde y hasta (int).
    Retorna None
    '''
    matriz = inicializar_matriz(cantidad_filas, cantidad_columnas, 0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(desde, hasta)
    return matriz

def mostrar_matriz(matriz:list)->None:
    '''
    Imprime en la pantalla la matriz.
    Recibe la matriz (list).
    Retorna None.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

def ocultar_impares(matriz:list)->None:
    '''
    Muestra la matriz y reemplaza cada numero impar con un asterisco.
    Recibe la matriz (list).
    Retorna None.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if int(matriz[i][j] % 2 != 0):
                print("*", end=" ")
            else:
                print(matriz[i][j], end= " ")
        print("")

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any)->list:
    '''
    Asigna a una matriz valores iniciales.
    Recibe una cantidad de filas y columnas (int).
    Retorna la matriz inicializada.
    '''
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def buscar_valor(matriz:list, valor:int)->bool:
    '''
    Comprueba si un valor coincide con algun elemento de una matriz.
    Recibe la matriz (list) y el valor (int).
    Retorna True si el valor coincide y sino False.
    '''
    resultado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                resultado = True
                break
        if resultado == True:
            break
    return resultado

def generar_matriz_sudoku(matriz:list, desde:int, hasta:int)->None:
    '''
    Crea una matriz con números diferentes en filas, columnas y recuadros.
    Recibe la matriz (list), y los valores desde y hasta (int).
    Retorna None.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = random.randint(desde, hasta)
            while buscar_valor(matriz, numero) == True:
                numero = random.randint(desde, hasta)
            matriz[i][j] = numero

def mostrar_matriz(matriz:list)->None:
    '''
    La funcion muestra los elementos de una matriz.
    Recibe la matriz (list).
    Retorna None
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

def sumar_matrices(matriz_a:list, matriz_b:list)->list:
    '''
    La funcion calcula la suma entre dos matrices.
    Recibe las matrices (list).
    Retorna la suma.
    '''
    matriz_resultante = inicializar_matriz(len(matriz_a), len(matriz_a[0]), 0)
    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[i])):
            matriz_resultante[i][j] = int(matriz_a[i][j]) + int(matriz_b[i][j])
    return matriz_resultante

def multiplicar_matriz_escalar(matriz:list, escalar:int)->list:
    '''
    La funcion calcula la multiplicacion entre una matriz y un numero escalar.
    Recibe la matriz (list) y el escalar (int).
    Retorna el resulta de la multiplicacion
    '''
    matriz_resultante = inicializar_matriz(len(matriz), len(matriz[0]), 0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultante[i][j] = int(matriz[i][j]) * escalar
    return matriz_resultante

def validar_matriz_multiplicable(matriz_a:list, matriz_b:list)->bool:
    '''
    Verifica que dos matrices se puedan multiplicar.
    Recibe las matrices (list).
    Retorna True en caso de que las matrices sean multiplicables o False en caso contrario.
    '''
    resultado = False
    if len(matriz_a[0]) == len(matriz_b):
        resultado = True
    return resultado

def multiplicar_matrices(matriz_a:list, matriz_b:list)->list:
    '''
    Calcula la multiplicacion entre dos matrices.
    Recibe las matrices (list).
    Retorna el resultado de la multiplicacion.
    '''
    matriz_resultante = None
    if validar_matriz_multiplicable(matriz_a, matriz_b):
        matriz_resultante = inicializar_matriz(len(matriz_a), len(matriz_b[0]), 0)
        for i in range(len(matriz_b[0])):
            for j in range(len(matriz_a)):
                for k in range(len(matriz_b)):
                    matriz_resultante[i][j] += int(matriz_a[i][k]) * int(matriz_b[j][i])                    
    return matriz_resultante
