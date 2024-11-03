import random
from os import system

def generar_lista_random_alfanumerica(cantidad:int)->list:
    '''
    La funcion carga una lista de caracteres 0-9A-Z de forma aleatoria.
    Recibe un numero (int).
    Retorna la lista cargada. 
    '''
    lista = []
    for i in range(cantidad):
        caracter = chr(random.randint(48, 90))
        while ord(caracter) < 65 and ord(caracter) > 57:
            caracter = chr(random.randint(48, 90))
        lista += [caracter]
    return lista

def ordenar_lista(lista:list, criterio:str = "asc")->bool:
    '''
    La funcion ordena una lista según un criterio ascendente o descendente.
    Recibe la lista (list) y el criterio (str).
    Retorna la lista ordenada.
    '''
    flag = False
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "asc" and lista[i] > lista[j]) or (criterio == "dsc" and lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                flag = True
    return flag

def contar_caracteres(lista:list):
    '''
    Crea una lista de conteo para las letras de "A" a "Z".
    Recibe una lista.
    Retorna la lista con la cantidad de letras.
    '''
    conteo = [0] * 26
    for caracter in lista:
        if 'A' <= caracter <= 'Z':
            indice = ord(caracter) - ord('A')
            conteo[indice] += 1
    return conteo

def mostrar_lista_paralela(lista_a:list, lista_b:list) -> None:
    ''' 
    Muestra lista paralelas.
    Recibe dos listas.
    Retorna None.
    '''
    for i in range(len(lista_a)):
        print(f"      {lista_a[i]} --> {lista_b[i]}")


def contador_de_caracteres(lista:list, caracteres:str):
    ''' 
    Cuenta los caracteres de una lista.
    Recibe caracteres. Conjuntos de elementos (str). Y recibe una lista (list).
    Retorna la lista con la cantidad de repetidos.
    '''

    cantidad_repetidos = []
    for caracter in caracteres:
        contador = 0
        for item in lista:
            if caracter == item:
                contador += 1
        cantidad_repetidos += [contador]
    mostrar_lista_paralela(caracteres, cantidad_repetidos)

    return cantidad_repetidos


def inicializar_matriz(cant_filas:int, cant_columnas:int)->list:
    '''
    Inicializa un matriz.
    Recibe dos numeros con la cantidad de filas y columnas.
    Retorna la matriz inicializada.
    '''
    matriz = []
    for _ in range(cant_filas):
        matriz += [[None] * cant_columnas]
    return matriz


def crear_matriz_aleatoria(cantidad_filas:int, cantidad_columnas:int, desde:int, hasta:int)->list:
    '''
    Carga en un matriz números aleatorios.
    Recibe cantidad de filas, columnas, desde y hasta (int).
    Retorna la matriz.
    '''
    matriz = inicializar_matriz(cantidad_filas,cantidad_columnas)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = str(random.randint(desde, hasta))
    return matriz


def mostrar_matriz(matriz)->None:
    '''
    Muestra por pantalla una matriz de enteros, con los elementos alineados en columnas.
    Recibe una matriz (list). La matriz a mostrar.
    Retorna None.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print(" ")


def validar_numero_entero(cadena:str)->bool:
    '''
    La función determina si el entero ingresado está entre el rango mínimo y 
    maximo.
    Recibe el numero a validar, el rango minimo y el rango maximo.
    Retorna True en caso de estar en el rango, sino retorna False.
    '''
    flag = True
    for num in cadena:
        if num < "0" or num > "9":
            flag = False
    return flag

def identificar_valor_maximo_y_minimo(lista:list)->None:
    '''
    La funcion busca cual es el caracter que se repite mas y menos veces.
    Recibe como parametro una lista.
    No retorna nada ya que se muestra el resultado por pantalla.
    '''
    numero_menor = None
    numero_mayor = None
    for i in range(len(lista)):
        caracter = lista[i]
        if ord(lista[i]) > 64 and ord(lista[i]) < 91:
            cantidad = contar_caracteres(lista, caracter)

def buscar_valor_minimo_y_maximo(lista:list, criterio:str)->list:
    '''
    Se busca caracter mayor.
    Recibe una lista por parametro.
    Retorna la lista.
    '''
    caracter = ""
    contador_menor_mayor = None
    caracter_menor_mayor = ""
    for i in range(26):
        contador = 0
        for j in range(len(lista)):
            if(lista[j] == chr(65 + i)): 
                caracter = lista[j] 
                contador += 1
        if criterio == "max" and (contador_menor_mayor == None or contador > contador_menor_mayor):
                contador_menor_mayor = contador
                caracter_menor_mayor = caracter
        if criterio == "min" and (contador_menor_mayor == None or contador < contador_menor_mayor):
                contador_menor_mayor = contador
                caracter_menor_mayor = caracter
    return [caracter_menor_mayor, contador_menor_mayor]


def buscar_secuencia(matriz:list, secuencia:str)-> bool:
    '''
    La funcion busca una secuencia en una matriz.
    Recibe la matriz y la secuencia.
    Retorna True en caso de encontrar la secuencia o False en caso contrario.
    '''
    resultado = False
    for i in range(len(matriz)):
        bandera_secuencia = False
        contador_secuencia = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == secuencia[contador_secuencia]:
                if contador_secuencia < len(secuencia):
                    contador_secuencia += 1
                    bandera_secuencia = True
                if contador_secuencia == len(secuencia) and bandera_secuencia == True:
                    resultado = True
            else:
                bandera_secuencia = False
                contador_secuencia = 0
            if resultado == True:
                break

    if resultado == False:
        print(f"La secuencia numérica {secuencia} no existe en la matriz.")
    else:
        print(f"La secuencia numérica {secuencia} existe en la matriz.")
    return resultado


def mostrar_resultado_punto_3(conteo:int)->None:
    '''
    La funcion muestra la cantidad de caracteres A-Z en una lista.
    Recibe la listas (list).
    Retorna None.
    '''
    print("CARACTER | CANTIDAD")
    print("---------+---------")
    for i in range(26):
        cantidad = conteo[i]  
        caracter = chr(i + ord('A'))  
        print(f"    {caracter}    |    {cantidad}")


def buscar_valor(matriz:list, valor:int)-> bool:
    '''
    Busca el valor dado en la fila de la matriz dada.
    Recibe una matriz (list). Matriz donde buscar un valor. Valor (int). Valor que se desea hallar.
    Retorna un booleano (bool). Devuelve True si el valor esta en la matriz, caso contrario False.
    '''
    resultado = False
    for fila in (matriz):
        if valor in fila:
            resultado = True
    return resultado
    
def mostrar_resultado_punto_4(lista_a:list, lista_b:list)->None:
    '''
    La funcion muestra los elementos de dos listas.
    Recibe la listas (list).
    Retorna None.
    '''
    print("CARACTER | CANTIDAD")
    print("---------+---------")
    mostrar_lista(lista_a)
    mostrar_lista(lista_b)
    
def mostrar_lista(lista:list):
    '''
    La funcion muestra los elementos de una lista.
    Recibe la lista (list).
    Retorna None.
    '''
    for elemento in lista:
        print(f"    {elemento}    |", end="")
    print("")
        
def menu_4_case(mensaje_a:str, mensaje_b:str, mensaje_c:str, mensaje_d:str="", mensaje_e:str="", mensaje_f:str="", mensaje_g:str="")->str:
    '''
    Menu basico pseudo generico.
    Recibe
        mensaje_a (str): Primera opcion del menu.
        mensaje_b (str): Segunda opcion.
        mensaje_c (str): Tercera opcion.
        mensaje_d (str, optional): Cuarta opcion / opcional.
        mensaje_e (str, optional): Quinta opcion / opcional.
        mensaje_f (str, optional): sexta opcion / opcional.
        mensaje_g (str, optional): septima opcion / opcional.
    Retorna una cadena (str) con la opcion del menu elegida.
    '''
    limpiar_pantalla()
    print("")
    print("   -------Menu de opciones-------   ")
    print(mensaje_a)
    print(mensaje_b)
    print(mensaje_c)
    print(mensaje_d)
    print(mensaje_e)
    print(mensaje_f)
    print(mensaje_g)
    return input("Ingrese opcion: ")


def limpiar_pantalla()->None:
    '''
    Limpia la pantalla de menu para mejor calidad visual.
    No recibe valores.
    Retorna None.
    '''
    system("cls")

def pausar()->None:
    '''
    Permite pausar el programa para poder ver los print de este.
    No recibe valores.
    Retorna None.
    '''
    system("pause")

def confirmar_salir(confirmacion:str)->bool:
    '''
    Espera la confirmacion de salida con "si" o "no".
    Recibe la confirmacion (str). Input con la confirmacion.
    Retorna True si la confimacion es "si", caso contrario retorna False.
    '''
    resultado = False
    while confirmacion != "si" and confirmacion != "no":
        confirmacion = input("Error, Elija solamente ['si' o 'no']: ")
    if confirmacion == "si":
        resultado = True
    return resultado
