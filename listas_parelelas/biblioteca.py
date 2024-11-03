def cargar_listas_paralelas(cantidad:int, mensaje_a:str, mensaje_b:str, lista_a:list, lista_b:list, desde_a:int = 0, hasta_a:int = 999, desde_b:int = 0, hasta_b:int = 999, tipo_a:type = str, tipo_b:type = str)->None:
    """
    Pide y carga en listas dos valores.
    Recibe una cantidad (int), dos mensajes (str) y dos listas (list).
    Retorna None
    """    
    for _ in range(cantidad):
        valor_a = validar_convertir_valor(mensaje_a, tipo_a, desde_a, hasta_a, input(mensaje_a))
        valor_b = validar_convertir_valor(mensaje_b, tipo_b, desde_b, hasta_b, input(mensaje_b))
        lista_a += [valor_a]
        lista_b += [valor_b]

def validar_convertir_valor(mensaje:str, tipo:type, desde:int, hasta:int, valor:str)->int|float:
    """
    La funcion valida un valor y lo convierte a un tipo.
    Rebice un mensaje (str), el tipo (type), un valor desde (int), un valor hasta (int) y un valor (str).
    Retorna el valor validado y convertido.  
    """
    if tipo == int:
        if validar_numero_entero(valor) == True:
            valor = tipo(valor)
            while validar_rango_entero(valor, desde, hasta) != True:
                valor = solicitar_entero(mensaje, desde, hasta)
    elif tipo == float:
        valor = tipo(valor)
        while validar_rango_entero(valor, desde, hasta) != True:
            valor = input(mensaje)
            valor = tipo(valor)
    return valor

def mostrar_mayores_que(lista_a: list, lista_b: list, valor_b:int)->None:
    '''
    Muestra los elementos de una lista que superan un valor.
    Recibe dos listas (list) y un valor (int)
    Retorna None
    '''
    for i in range(len(lista_b)):
        if int(lista_b[i]) >= valor_b:
            print(lista_a[i])

def contar_mayor_que_primero(lista:list)->int:
    '''La funcion cuenta los elementos de una lista que superan al primer elemento.
    Recibe la lista (list).
    Retorna la cantidad de elementos.'''
    contador = 0
    for i in range(len(lista)):
        if i == 0:
            primer_valor = lista[i]
        elif lista[i] > primer_valor:
            contador += 1
    return contador

def sumar_listas(lista_a:list, lista_b:list)->list:
    '''
    La funcion calcula la suma entera de dos elementos de listas paralelas.
    Recibe dos listas (list).
    Retorna la suma.
    '''
    lista_c = []
    for i in range(len(lista_a)):
        lista_c += [int(lista_a[i]) + int(lista_b[i])]
    return lista_c

def mostrar_lista(lista:list)->None:
    '''
    La funcion muestra los elementos de una lista.
    Recibe la lista (list).
    Retorna None.
    '''
    for elem in lista:
        print(elem)

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

def validar_rango_entero(numero_a_validar:int, minimo:int, maximo:int)->bool:
    '''
    La función determina si el entero ingresado está entre el rango mínimo y máximo.
    Recibe el número a validar, el rango mínimo y el rango máximo.
    Retorna True en caso de estar en el rango, sino retorna False.
    '''

    retorno = False

    if numero_a_validar >= minimo and numero_a_validar <= maximo:
        retorno = True

    return retorno

def validar_numero_entero(cadena:str)->bool:
    '''
    La función valida si la cadena es convertible a entero
    Recibe la cadena a analizar
    Retorna un booleano, si es True es convertible, si es False no es convertible
    '''
    bandera = True
    
    for num in cadena:
        if determinar_digito(num) != True:
            bandera = False
            break
    return bandera

def solicitar_entero(mensaje:str, minimo:int = 1, maximo:int = 999)->int:
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

def mostrar_lista(lista:list)->None:
    '''
    La funcion muestra los elementos de una lista.
    Recibe la lista (list).
    Retorna None.
    '''
    for elem in lista:
        print(elem)

def evaluar_condicion(lista:list)->list:
    """
    La funcion evalua la condicion academica de una lista de alumnos.
    Recibe una lista de notas (list).
    Retorna una lista con la condicion ademica de cada alumno  
    """
    lista_condiciones = []
    for elemento in lista:
        elemento = int(elemento)
        if elemento >= 6:
            lista_condiciones += ["Promocionado"]
        elif elemento >= 4:
            lista_condiciones += ["Aprobado"]
        else:
            lista_condiciones += ["Reprobado"]
    return lista_condiciones

def mostrar_cabecera()->None:
    """
    La funcion muestra la cabecera de un listado con informacion de los alumnos.
    No recibe valores por parametro.
    Retorna None
    """
    print(f"{'Nombre':10} {'Nota':5} {'Condicion':5}")

def mostrar_uno(pos:int, lista_posicion_a:list, lista_posicion_b:list, lista_posicion_c:list)->None:
    """
    Muestra un elemento de cada listado.
    Recibe una posicion (int) a la que se va acceder en el listado.
    Retorna None
    """
    print(f"{lista_posicion_a[pos]:10} {lista_posicion_b[pos]:8} {lista_posicion_c[pos]:5}")

def mostrar(lista_a:list, lista_b:list, lista_c:list)->None:
    """
    Muestra los listados de los alumnos.
    No recibe valores por parametro.
    Retorna None.
    """
    for i in range(len(lista_a)):
        mostrar_uno(i, lista_a, lista_b, lista_c)
    print("\n")

def mostrar_lista_formateada(lista:list):
    '''
    La funcion muestra los elementos de una lista separada por guíones.
    Recibe la lista (list).
    Retorna None.
    '''
    resultado = ""
    
    for i in range(len(lista)):
        resultado += str(lista[i])
        if i < len(lista) - 1:  
            resultado += " - "
            
    print(resultado)

def contar_condicion(lista:list)->list:
    """
    La funcion cuenta la cantidad de alumnos de una lista que estan aprobados, 
    promociondos o reprobados.
    Recibe la lista (list).
    Retorna la cantidad en una lista.
    """
    cantidad_aprobados = 0
    cantidad_promocionados = 0
    cantidad_reprobados = 0
    lista_cantidad_condiciones = []
    for elemento in lista:
        if elemento == "Aprobado":
            cantidad_aprobados += 1
        elif elemento == "Promocionado":
            cantidad_promocionados += 1
        else:
            cantidad_reprobados += 1
    lista_cantidad_condiciones += [cantidad_aprobados]
    lista_cantidad_condiciones += [cantidad_promocionados]
    lista_cantidad_condiciones += [cantidad_reprobados]
    return lista_cantidad_condiciones

def crear_menu()->str:
    """
    La funcion crea un mensaje para que se pueda pedir una opcion de un menu.
    No recibe valores por parametro.
    Retorna el mensaje
    """
    menu = """
    ===== Mi Programa =====
    a) Ingresar la cantidad total de alumnos
    b) Ingresar nombre y nota de cada alumno
    c) Realizar un listado que muestre los nombres, notas y condicion de cada alumno
    d) Contar e imprimir la cantidad de "Aprobados", "Promocionados" y "Reprobados"
    e) Salir
    ========================

    Ingrese la opcion del menu: """
    return menu

def mostar_dato(dato:str)->None:
    """
    Muestra el dato recibido por parametro.
    Recibe un dato (str).
    Devuelve un None.
    """
    print(dato)
