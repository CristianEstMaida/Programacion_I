import random

def cargar_matriz_aleatoriamente(matriz:list):
    seguir = "S"
    while seguir == "S":
        fila = int(input("Indice de la fila: "))
        columna = int(input("Indice de columna: "))
        dato = int(input("Ingrese el numero a cargar: "))
        matriz[fila][columna] = dato
        seguir = input("Desea seguir cargando? S/N")

def buscar_valor_entero(matriz:list, valor:int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se encontro el numero en fila {i} columna {j}")

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

def crear_menu()->str:
    """
    La funcion crea un mensaje para que se pueda pedir una opcion de un menu.
    No recibe valores por parametro.
    Retorna el mensaje
    """
    menu = """
    ===== Mi Programa =====
    a) Generar una matriz con numeros aleatorios
    b) Mostrar la matriz generada
    c) Determinar si la matriz contiene series de numeros consecutivos
    d) Determinar la cantidad total de series
    e) Determinar el largo de la serie mas corta, y mostrar todas las series de ese largo
    f) Determinar el largo de la serie mas larga, y mostrar todas las series de ese largo
    g) Salir
    ========================

    Ingrese la opcion del menu: """
    return menu

def mostrar_series_longitud(matriz:list, longitud_buscada:int)->None:
    """
    Muestra las series de una longitud dada.
    Recibe una matriz (list) y la longitud.
    Retorna None.
    """

    for fila in matriz:
        if longitud_serie(fila) == longitud_buscada:
            print(fila)
    for i in range(len(matriz[0])):
        columna = []
        for fila in matriz:
            columna += [fila[i]]
            if longitud_serie(columna) == longitud_buscada:
                print(columna)

def encontrar_series_largas(matriz: list)->int:
    """
    Haya la longitud de las series mas largas.
    Recibe una matriz (list).
    Retorna la longitud.
    """

    longitudes_series = []
    for fila in matriz:
        longitudes_series += [longitud_serie(fila)]
    for i in range(len(matriz[0])):
        columna = []
        for fila in matriz:
            columna += [fila[i]]
            longitudes_series += [longitud_serie(columna)]

    longitud_maxima = longitudes_series[0]
    indice = 1
    while indice < len(longitudes_series):
        longitud = longitudes_series[indice]
        if longitud > longitud_maxima:
            longitud_maxima = longitud
            indice += 1
    return longitud_maxima

def longitud_serie(lista: list)->int:
    """
    Haya la longitud de una serie.
    Recibe una lista (list).
    Retorna la longitud
    """

    longitud_actual = 0
    longitud_maxima = 0
    for i in range(len(lista) - 1):
        if lista[i] + 1 == lista[i + 1]:
            longitud_actual += 1
        else:
            if longitud_actual > longitud_maxima:
                longitud_maxima = longitud_actual
            longitud_actual = 0
    if longitud_actual > longitud_maxima:
        longitud_maxima = longitud_actual
    if longitud_maxima < 2:
        longitud_maxima = 0
    return longitud_maxima

def encontrar_series_cortas(matriz: list)->int:
    """
    Haya la longitud de las series mas cortas.
    Recibe una matriz (list).
    Retorna la longitud.
    """

    longitudes_series = []
    for fila in matriz:
        longitudes_series += [longitud_serie(fila)]
    for i in range(len(matriz[0])):
        columna = []
        for fila in matriz:
            columna += [fila[i]]
            longitudes_series += [longitud_serie(columna)]

    longitud_minima = longitudes_series[0]
    indice = 1
    while indice < len(longitudes_series):
        longitud = longitudes_series[indice]
        if longitud < longitud_minima:
            longitud_minima = longitud
            indice += 1
    return longitud_minima

def contar_series(lista:list)->int:
    '''
    Cuenta la cantidad de series que contiene una lista.
    Recibe la matriz (list).
    Retorna la cantidad.
    '''
    contador = 0
    flag = False
    for i in range(len(lista) - 1):
        if lista[i] + 1 == lista[i + 1]:
            if flag == False:
                contador += 1
                flag = True
        else:
            flag = False
    return contador

def contar_matriz_series(matriz:list)->int:
    '''
    Cuenta la cantidad de series que contiene una matriz.
    Recibe la matriz (list).
    Retorna la cantidad.
    '''
    contador = 0
    for fila in matriz:
        contador += contar_series(fila)

    for i in range(len(matriz[0])):
        columna = []
        for fila in matriz:
            columna += [fila[i]]
            contador += contar_series(columna)
    return contador

def verificar_serie(lista:list)->bool:
    '''
    Determina si un lista contiene al menos una serie de numeros consecutivos.
    Recibe la (list).
    Retorna True si la lista contiene la serie o en caso contrario False.
    '''
    resultado = True
    for i in range(len(lista) - 1):
        if lista[i] + 1 != lista[i + 1]:
            resultado = False
            break
    return resultado

def determinar_matriz_series(matriz:list)->bool:
    '''
    Determina si una matriz contiene al menos una serie de numeros consecutivos.
    Recibe una matriz (list).
    Retorna True si la matriz contiene la serie o en caso contrario False.
    '''
    resultado = False
    for fila in matriz:
        if verificar_serie(fila):
            resultado = True
            break

    for i in range(len(matriz[0])):
        columna = []
        for fila in matriz:
            columna += [fila[i]]
            if verificar_serie(columna):
                resultado =  True
                break
    return resultado