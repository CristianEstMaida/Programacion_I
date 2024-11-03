import random

def suma_elementos(lista: list)->int:
    '''
    La función suma los elementos de una lista
    Recibe una lista (list)
    Retorna la suma
    '''
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def mostrar_elemento(lista: list, indice: int, mensaje: str)->None:
    '''
    La función muestra un elemento de una lista
    Recibe la lista (list), un índice entero (int) y un mensaje (str).
    Retorna None.
    '''
    print(f"{mensaje}: {lista[indice]}")

def mostrar_promedio(lista:list)->None:
    '''
    La función muestra el promedio entre dos elementos de una lista
    Recibe la lista (list).
    Retorna None.
    '''
    print(f"Nombre del alumno: {lista[0]} y su promedio es {(lista[1] + lista[2]) / 2}")

def contar_mayores(lista:list, minimo:int)->int:
    '''
    La función cuenta la cantidad de elementos de una lista que son mayores a un número mínimo
    Recibe la lista (list) y el número entero (int).
    Retorna la cuenta.
    '''
    contador = 0
    for elemento in lista:
        if elemento > minimo:
            contador += 1
    return contador

def cargar_lista(mensaje:str, cantidad:int, tipo:type)->list:
    '''
    La funcion carga datos en una lista con un tipo especificado.
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista y el tipo de dato
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    lista = []

    for _ in range(cantidad):
        valor_ingresado = input(mensaje)
        valor_ingresado = tipo(valor_ingresado)
        
        lista += [valor_ingresado]

    return lista

def mostrar_lista_formateada(lista:list):
    '''
    La función muestra los elementos de una lista separada por guíones.
    Recibe la lista (list).
    Retorna None.
    '''
    resultado = ""
    
    for i in range(len(lista)):
        resultado += str(lista[i])
        if i < len(lista) - 1:  
            resultado += " - "
            
    print(resultado)

def cargar_lista(tamanio:int, mensaje:str)->list:
    '''
    La función carga elemento en una lista
    Recibe el tamaño de la lista (int) y un mensaje (str).
    Retorna la lista cargada.
    '''
    lista = []
    for i in range(tamanio):
        elemento = int(input(mensaje + f"{i + 1}: "))
        lista += [elemento]
    return lista

def filtrar_superior_o_igual(lista:list, valor_superior_igual:int)->list:
    '''
    La función cuenta la cantidad de elementos de una lista que son mayores a un número mínimo
    Recibe la lista (list) y el número entero (int).
    Retorna la cuenta.
    '''
    lista_numeros = []
    for i in range(len(lista)):
        if lista[i] >= valor_superior_igual:
            lista_numeros += [lista[i]]
    return lista_numeros 

def cargar_lista_aleatoria(numero:int, valor_desde:int, valor_hasta:int)->int:
    '''
    La funcion carga una lista de forma aleatoria.
    Recibe un numero (int), un valor desde (int) y un valor hasta (int).
    Retorna la lista cargada. 
    '''
    lista_random = []
    for _ in range(numero):
        lista_random += [random.randint(valor_desde, valor_hasta)]
    return lista_random

def contar_numeros_pares(lista:list)->int:
    '''
    La funcion cuenta la cantidad de numero pares que hay en una lista.
    Recibe la lista (list).
    Retorna la cantidad.
    '''
    contador = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            contador += 1
    return contador


def cargar_palabras_en_lista(mensaje:str, lista:list, cantidad:int)->list:
    '''
    La funcion carga string en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    lista = []

    for _ in range(cantidad):
        lista += [input(mensaje)]
    return lista

def contar_caracteres(lista:list, cantidad:int)->int:
    '''
    La funcion cuenta los elementos de una lista que superan una cantidad de caracteres.
    Recibe la lista (list) y la cantidad de caracteres (int).
    Retorna la cantidad de elementos.
    '''
    contador = 0
    for elemento in lista:
        if len(elemento) >= cantidad:
            contador += 1

    return contador


def cargar_lista_enteros(mensaje:str, valor_break)->list:
    '''
    La funcion carga enteros en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    lista = []

    while True:
        numero = int(input(mensaje))
        if numero == valor_break:
            break

        lista += [numero]

    return lista

def cargar_lista_enteros(mensaje:str, cantidad:int)->list:
    '''
    La funcion carga enteros en una lista
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    lista = []

    for _ in range(cantidad):
        lista += [int(input(mensaje))]
    return lista

def mostrar_lista(lista:list)->None:
    '''
    La funcion muestra los elementos de una lista.
    Recibe la lista (list).
    Retorna None.
    '''
    for elem in lista:
        print(elem)

def cargar_lista(mensaje:str, cantidad:int, tipo:type)->list:
    '''
    La funcion carga datos en una lista con un tipo especificado.
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la lista y el tipo de dato
    Retorna la lista conformada con los datos ingresados por el usuario
    '''
    lista = []

    for _ in range(cantidad):
        valor_ingresado = input(mensaje)
        valor_ingresado = tipo(valor_ingresado)
        
        lista += [valor_ingresado]

    return lista

def calcular_promedio(lista:list)->float|None:
    '''
    La funcion calcula promedio.
    Recibe una lista (list).
    Retorna un None cuando la lista se encuentra vacía
    '''
    if len(lista) == 0:
        promedio = None
    else:
        acumulador = 0
        for elemento in lista:
            acumulador += elemento
        promedio = acumulador / len(lista)
    return promedio

def contar_superen_promedio(lista:list, promedio:float)->int:
    '''
    La funcion cuenta la cantidad de elementos de una lista que superan el valor promedio.
    Recibe la lista (list) y el promedio (float).
    Retorna la cantidad.
    '''
    contador = 0
    for elementos in lista:
        if elementos > promedio:
            contador += 1
    return contador

def identificar_valor_maximo(lista:list)->int|None:
    '''
    La funcion encuentra un máximo en una lista.
    Recibe la lista (list).
    Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el máximo.
    '''
    mayor = None
    for i in range(len(lista)):
        if mayor == None or lista[i] > mayor:
            mayor = lista[i]
    return mayor

def identificar_valor_minimo(lista:list)->int:
    '''
    La funcion encuentra un minimo en una lista.
    Recibe la lista (list).
    Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el minimo.
    '''
    menor = None
    for i in range(len(lista)):
        if mayor == None or lista[i] < menor:
            mayor = lista[i]
    return mayor

def posicion_numero_minimo(lista:list, numero_menor:int)->int:
    '''
    La funcion posicion del elemento de valor minimo de un lista.
    Recibe la lista (list) y el valor minimo (int).
    Retorna la posicion.
    '''
    for i in range(len(lista)):
        if lista[i] == numero_menor:
            indice_menor = i
            break
    return indice_menor

def determinar_repetidos(lista:list, valor:int)->int:
    '''
    La funcion cuenta la cantidad de elementos de una lista que repiten un valor.
    Recibe la lista (list) y el valor (int).
    Retorna la cantidad.
    '''
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador

def identificar_string_mas_corto(lista:list)->str:
    '''
    La funcion encuentra la cadena mas corta de los elementos de una lista.
    Recibe la lista (list).
    Retorna la cadena.
    '''
    string_mas_corto = None
    for elem in lista:
        if string_mas_corto == None or len(elem) <len(string_mas_corto):
            string_mas_corto = elem
    return string_mas_corto

def convertir_string_en_entero(lista:list)->list:
    '''La funcion almacena en una lista el largo de cada elemento.
    Recibe una lista (list).
    Retorna la lista de largos. 
    '''
    lista_largos = []
    for i in range(len(lista)):
        lista_largos += [len(lista[i])]
    return lista_largos