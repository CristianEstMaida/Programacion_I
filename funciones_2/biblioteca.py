def determinar_par_impar(numero:int)->bool:
    '''
    La función determina si un número es par o impar
    Recibe un número entero (int).
    Retorna True cuando es par y False cuando es impar.
    '''
    retorno = False
    if numero % 2 == 0:
        retorno = True
    return retorno

def determinar_letra(caracter:str)->bool:
    '''
    La función determina si un caracter está comprendido entre a-z o A-Z.
    Recibe un caracter de tipo str.
    Retorna True si estra comprendido entre a-z o A-Z y en caso contrario retorna False.
    '''
    retorno = False
    if caracter >= 'a' and caracter <= 'z' or caracter <= 'A' and caracter >= 'Z':
        retorno = True
    return retorno

def convertir_a_mayuscula(caracter:str)->str:
    '''
    La función convierte un caracter a mayúscula
    Recibe un caracter
    Retorna el caracter ingresado en mayúscula
    '''
    retorno = caracter
    if caracter >= 'a' and caracter <= 'z':
        valor_numero_de_caracter = ord(caracter) - 32
        retorno = chr(valor_numero_de_caracter)
    
    return retorno

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

def solicitar_entero_borrador(mensaje:str, minimo:int, maximo:int)->int:
    '''
    La función solicita y valida un número entero
    Recibe un mensaje y el rango mínimo y máximo
    Retorna el número solicitado validado como un entero
    '''

    numero = input(mensaje)
        
    while validar_numero_entero(numero) != True:

        numero = input(mensaje)
    
    numero = int(numero)

    booleano = validar_rango_entero(numero, minimo, maximo)

    while booleano != True:
        if booleano == False:
            numero = input(mensaje)
        
        while validar_numero_entero(numero) != True:

            numero = input(mensaje)
        
        numero = int(numero)
    return numero

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

def validar_cadena(mensaje:str, cadena_1:str, cadena_2:str=None, cadena_3:str = None)->str:
    '''
    La función valida que una cadena ingresada sea como las 1, 2 o 3 cadenas que lo representan.
    Recibe un mensaje y 1, 2 o 3 cadenas
    Retorna la cadena ingresada validada
    '''
    cadena_ingresada = input(mensaje)

    while cadena_ingresada != cadena_1 and cadena_ingresada != cadena_2 and cadena_ingresada != cadena_3:
        cadena_ingresada = input(mensaje)
    
    return cadena_ingresada

def largo_cadena(cadena:str)->int:
    '''
    Mide el largo de la cadena de caracteres.
    Recibe una cadena de caracteres que se va a medir.
    Retorna un entero represantando el largo de la cadena.
    '''
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

def determinar_primo(numero:int)->bool:
    '''
    La función determina si un número ingresado es primo o no.
    Recibe un número entero.
    Retorna True en caso de que el número sea primo, sino retorna False.
    '''
    
    retorno = True

    if numero % 2 == 1:
        if numero > 2:
            for i in range(3, numero):
                if numero % i == 0:
                    retorno = False
                    break
        else:
            retorno = False
    elif numero != 2:
        retorno = False
    return retorno

def determinar_factorial(numero:int)->int:
    '''
    La función calcula el factorial de un número.
    Recibe un número entero.
    Retorna el factorial del número, en caso de números negativos retorna 0.
    '''
    
    factorial = 0
    if numero >= 0:
        factorial = 1
        for num in range(1, numero + 1):
            factorial *= num 
    return factorial

def validar_dni(cadena:str)->bool:
    '''
    La función valida que la cantidad de caracteres del DNI de una persona esté comprendida entre 6 y 8
    Recibe una cadena que contiene números.
    Retorna True si el DNI es válido sino retorna False.
    '''

    retorno = False
    largo = largo_cadena(cadena)
    if largo >= 6 and largo <= 8:
        retorno = True
    
    return retorno

def completar_dni(numero:str)->str:
    '''
    La función completa el DNI de una persona con ceros hasta llegar a 8 caracteres.
    Recibe una cadena de caracteres que contiene números.
    Retorna la cadena de 8 caracteres con los ceros a la izquierda. 
    '''

    largo = largo_cadena(numero) 
    resultado = ""

    if largo < 8:
        diferencia = 8 - largo
        for _ in range(diferencia):
            resultado += "0"
        resultado += numero
    else:
        resultado = numero
    return resultado

def transformar_numero_a_letras(cadena: str)->str:
    '''
    La función transforma una cadena a letras.
    Recibe una cadena a transformar
    Retorna el resultado de la transformación en letras
    '''
    numero = int(cadena)
    letras = ''
        
    if numero == 0:
        letras = 'cero'
    elif numero >= 100 and numero <= 199:
        letras = 'cien'
    elif numero >= 200 and numero <= 299:
        letras = 'doscientos'
    elif numero >= 300 and numero <= 399:
        letras = 'trescientos'
    elif numero >= 400 and numero <= 499:
        letras = 'cuatrocientos'
    elif numero >= 500 and numero <= 599:
        letras = 'quinientos'
    elif numero >= 600 and numero <= 799:
        letras = 'seiscientos'
    elif numero >= 800 and numero <= 899:
        letras = 'ochocientos'
    elif numero >= 900 and numero <= 999:
        letras = 'novecientos'
    if numero >= 101 and numero <= 199:
        letras += 'to '
    if numero >= 201 and numero <= 299 or numero >= 301 and numero <= 399 or numero >= 401 and numero <= 499 or numero >= 501 and numero <= 699 or numero >= 701 and numero <= 799 or numero >= 801 and numero <= 899 or numero >= 901 and numero <= 999:
        letras += " "
    if numero >= 16 and numero <= 19 or numero % 100 >= 16 and numero % 100 <= 19:
        letras += 'dieci'
    if numero == 20 or numero % 100 == 20:
        letras += 'veinte'
    if numero >= 21 and numero <= 29 or numero % 100 >= 21 and numero % 100 <= 29:
        letras += 'veinti'
    if numero >= 30 and numero <= 39 or numero % 100 >= 30 and numero % 100 <= 39:
        letras += 'treinta'
    if numero >= 40 and numero <= 49 or numero % 100 >= 40 and numero % 100 <= 49:
        letras += 'cuarenta'
    if numero >= 50 and numero <= 59 or numero % 100 >= 50 and numero % 100 <= 59:
        letras += 'cincuenta'
    if numero >= 60 and numero <= 69 or numero % 100 >= 60 and numero % 100 <= 69:
        letras += 'sesenta'
    if numero >= 70 and numero <= 79 or numero % 100 >= 70 and numero % 100 <= 79:
        letras += 'setenta'
    if numero >= 80 and numero <= 89 or numero % 100 >= 80 and numero % 100 <= 89:
        letras += 'ochenta'
    if numero >= 90 and numero <= 99 or numero % 100 >= 90 and numero % 100 <= 99:
        letras += 'noventa'
    if numero >= 31 and numero <= 39 or numero >= 41 and numero <= 49 or numero >= 51 and numero <= 59 or numero >= 61 and numero <= 69 or numero >= 71 and numero <= 79 or numero >= 81 and numero <= 89 or numero >= 91 and numero <= 99  or numero % 100 >= 31 and numero % 100 <= 39 or numero % 100 >= 41 and numero % 100 <= 49 or numero % 100 >= 51 and numero % 100 <= 59  or numero % 100 >= 61 and numero % 100 <= 69 or numero % 100 >= 71 and numero % 100 <= 79 or numero % 100 >= 81 and numero % 100 <= 89 or numero % 100 >= 91 and numero % 100 <= 99:
        letras += ' y '
    if numero == 1 or numero % 10 == 1 and numero % 100 != 11:
        letras += 'uno'
    if numero == 2 or numero % 10 == 2 and numero % 100 != 12:
        letras += 'dos'
    if numero == 3 or numero % 10 == 3 and numero % 100 != 13:
        letras += 'tres'
    if numero == 4 or numero % 10 == 4 and numero % 100 != 14:
        letras += 'cuatro'
    if numero == 5 or numero % 10 == 5 and numero % 100 != 15:
        letras += 'cinco'
    if numero == 6 or numero % 10 == 6:
        letras += 'seis'
    if numero == 7 or numero % 10 == 7:
        letras += 'siete'
    if numero == 8 or numero % 10 == 8:
        letras += 'ocho'
    if numero == 9 or numero % 10 == 9:
        letras += 'nueve'
    if numero == 10 or numero % 100 == 10:
        letras += 'diez'
    if numero == 11 or numero % 100 == 11:
        letras += 'once'
    if numero == 12 or numero % 100 == 12:
        letras += 'doce'
    if numero == 13 or numero % 100 == 13:
        letras += 'trece'
    if numero == 14 or numero % 100 == 14:
        letras += 'catorce'
    if numero == 15 or numero % 100 == 15:
        letras += 'quince'
    return letras