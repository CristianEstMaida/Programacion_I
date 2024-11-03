import random

def crear_menu()->str:
    """
    La funcion crea un mensaje para que se pueda pedir una opcion de un menu.
    No recibe valores por parametro.
    Retorna el mensaje
    """
    menu = """
    ===== Mi Programa =====
    1) Generar una lista alfanumerica aleatoria.
    2) Ordenar la lista alfanumerica.
    3) Buscar e informar cuantas veces se repite cada uno de los caracteres alfabeticos A-Z.
    4) El caracter que más veces se repite e informar la cantidad.
    El caracter que menos veces se repite e informar la cantidad.
    5) Generar una matriz aleatoria de números enteros.
    6) Buscar e informar si en la matriz existe una secuencia numerica ingresada.
    7) Salir
    ========================

    Ingrese la opcion del menu: """
    return menu

def cargar_lista_aleatoria(numero:int, valor_desde_a:int, valor_hasta_a:int, valor_desde_b:int, valor_hasta_b:int)->int:
    '''
    La funcion carga una lista de caracteres 0-9A-Z de forma aleatoria.
    Recibe un numero (int), dos valor desde (int) y dos valores hasta (int).
    Retorna la lista cargada. 
    '''
    lista_random = []
    for _ in range(numero):
        valor_a = chr(random.randint(valor_desde_a, valor_hasta_a))
        valor_b = chr(random.randint(valor_desde_b, valor_hasta_b))
        lista_random += [valor_a]
        lista_random += [valor_b]
    return lista_random

def determinar_letra(caracter:str)->bool:
    '''
    La función determina si un caracter está comprendido entre A-Z.
    Recibe un caracter de tipo str.
    Retorna True si estra comprendido entre  A-Z y en caso contrario retorna False.
    '''
    retorno = False
    if caracter >= 'A' and caracter <= 'Z':
        retorno = True
    return retorno

def filtar_lista_letras(lista:list)->list:
    '''
    
    '''
    lista_letras = []
    for elemento in lista:
        es_letra = determinar_letra(elemento)
        if es_letra == True:
            lista_letras += [elemento]
    return lista_letras

def encontrar_caracteres_repetidos(lista:list)->list:
    '''
    
    '''
    lista_cantidad_caracteres_repetidos = []
    for elemento in lista:
        lista_cantidad_caracteres_repetidos += [determinar_repetidos(lista, elemento)]
    return lista_cantidad_caracteres_repetidos

def determinar_repetidos(lista:list, valor:int)->int:
    '''
    La funcion cuenta la cantidad de elementos de una lista que repiten un 
    valor.
    Recibe la lista (list) y el valor (int).
    Retorna la cantidad.
    '''
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador

def mostrar_cabecera(cadena_a:str, cadena_b:str)->None:
    """
    La funcion muestra la cabecera de un listado con informacion de las 
    listas.
    Recibe dos cadenas (str).
    Retorna None
    """
    print(f"{cadena_a:10} {cadena_b:5}")

def mostrar_uno(pos:int, lista_posicion_a:list, lista_posicion_b:list)->None:
    """
    Muestra un elemento de cada listado.
    Recibe una posicion (int) a la que se va acceder en el listado y dos listas (list).
    Retorna None
    """
    print(f"{lista_posicion_a[pos]:10} {lista_posicion_b[pos]:8}")

def mostrar(lista_a:list, lista_b:list)->None:
    """
    Muestra los listados de los alumnos.
    Recibe dos listas (list).
    Retorna None.
    """
    for i in range(len(lista_a)):
        mostrar_uno(i, lista_a, lista_b)
    print("\n")

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

def encontrar_posicion_ocurrencias(lista:list, criterio:str)->int:
    '''
    La funcion encuentra la posicion del elemento que tiene mas ocurrencias.
    Recibe la lista (list).
    Retorna la posicion.
    '''
    contador = 0
    maximo = None
    minimo = None
    posicion = 0
    for elemento in lista:
        valor = determinar_repetidos(lista, elemento)
        if criterio == "max":
            if maximo == None or valor > maximo:
                maximo = valor
                posicion = contador
        elif criterio == "min":
            if minimo == None or valor < minimo:
                minimo = valor
                posicion = contador
        contador += 1
    return posicion

def encontrar_caracter_repetido(lista:list, criterio:str)->int:
    '''
    
    '''
    posicion = encontrar_posicion_ocurrencias(lista, criterio)
    return lista[posicion]

def identificar_valor_minimo(lista:list)->int:
    '''
    La funcion encuentra un minimo en una lista.
    Recibe la lista (list).
    Retorna None cuando se produjo un error o la lista está vacía, caso contrario retorna el minimo.
    '''
    menor = None
    for i in range(len(lista)):
        if menor == None or lista[i] < menor:
            menor = lista[i]
    return menor

def mostrar_dato(dato:str)->None:
    """
    Muestra el dato recibido por parametro.
    Recibe un dato (str).
    Devuelve un None.
    """
    print(dato)

def crear_matriz_aleatoria(cantidad_filas:int, cantidad_columnas:int, desde:int, hasta:int)->list:
    '''
    Carga en un matriz números aleatorios.
    Recibe cantidad de filas, columnas, desde y hasta (int).
    Retorna la matriz.
    '''
    matriz = inicializar_matriz(cantidad_filas, cantidad_columnas, 0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(desde, hasta)
    return matriz

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any)->list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def ordenar_cadena(lista:list)->list:
    lista_copia = lista[:]
    for i in range(len(lista_copia) - 1):
        for j in range(i + 1, len(lista_copia)):
            if len(lista_copia[i]) > len(lista_copia[j]):
                aux = lista_copia[i]
                lista_copia[i] = lista_copia[j]
                lista_copia[j] = aux
    return lista_copia

def ordenar_lista(lista:list, criterio:str = "asc")->list:
    '''
    La funcion ordena una lista según un criterio ascendente o descendente.
    Recibe la lista (list) y el criterio (str).
    Retorna la lista ordenada.
    '''
    for i in range(len(lista) -1):
        for j in range(i + 1, len(lista)):
            if criterio == "asc" and lista[i] > lista[j] or criterio == "desc" and lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def cargar_lista_enteros(mensaje:str, desde:int, hasta:int)->list:
    '''
    La funcion carga enteros en una lista.
    Recibe un mensaje con lo que se pide y la cantidad de elementos de la 
    lista.
    Retorna la lista conformada con los datos ingresados por el usuario.
    '''
    lista = []
    indice = 0
    seguir = "S"
    while seguir == "S":
        valor = validar_convertir_entero(mensaje, desde, hasta, 
                                          input(f"{mensaje} {indice + 1}: "))
        lista += [valor]
        indice += 1
        seguir = input("Desea seguir cargando? S/N: ")
        
    return lista

def validar_convertir_entero(mensaje:str, desde:int, hasta:int, 
                            valor:str)->int|float|str:
    """
    La funcion valida un valor y lo convierte a un entero.
    Rebice un mensaje (str), el tipo (type), un valor desde (int), un valor 
    hasta (int) y un valor (str).
    Retorna el valor validado y convertido.  
    """
    if validar_numero_entero(valor) == True:
        valor = int(valor)
        while validar_rango_entero(valor, desde, hasta) != True:
            valor = solicitar_entero(mensaje, desde, hasta)

def validar_rango_entero(numero_a_validar:int, minimo:int, maximo:int)->bool:
    '''
    La función determina si el entero ingresado está entre el rango mínimo y 
    máximo.
    Recibe el número a validar, el rango mínimo y el rango máximo.
    Retorna True en caso de estar en el rango, sino retorna False.
    '''

    retorno = False

    if numero_a_validar >= minimo and numero_a_validar <= maximo:
        retorno = True

    return retorno

def solicitar_entero(mensaje:str, minimo:int, maximo:int)->int:
    '''
    La función solicita y valida un número entero
    Recibe un mensaje y el rango mínimo y máximo
    Retorna el número solicitado validado como un entero
    '''

    numero = minimo - 1
    while validar_rango_entero(numero, minimo, maximo) == False:
        numero = input(mensaje)
        while validar_numero_entero(numero) != True:
            numero = input(mensaje)
        numero = int(numero)

    return numero

def validar_numero_entero(cadena:str)->bool:
    '''
    La función valida si la cadena es convertible a entero.
    Recibe la cadena a analizar.
    Retorna un booleano, si es True es convertible, si es False no es 
    convertible.
    '''
    bandera = True
    
    for num in cadena:
        if determinar_digito(num) != True:
            bandera = False
            break
    return bandera

def determinar_digito(caracter)->bool:
    '''
    La función determina si el caracter recibido está entre 0 y 9
    Recibe un caracter en formato string 
    Retorna un booleano
    '''
    retorno = False

    if caracter >= '0' and caracter <= '9':
        retorno = True

    return retorno

def determinar_matriz_secuencia(matriz:list, secuencia:list)->bool:
    '''
    Determina si una matriz contiene al menos una secuencia de numeros.
    Recibe la matriz y la secuencia (list).
    Retorna True si la matriz contiene la secuencia o en caso contrario False.
    '''
    resultado = False
    for fila in matriz:
        if fila == secuencia:
            resultado = True
            break
    return resultado

def mostrar_lista_formateada(lista:list):
    '''
    La funcion muestra los elementos de una lista separada por guiones.
    Recibe la lista (list).
    Retorna None.
    '''
    resultado = ""
    
    for i in range(len(lista)):
        resultado += str(lista[i])
        if i < len(lista) - 1:  
            resultado += " - "
            
    print(resultado, end="")