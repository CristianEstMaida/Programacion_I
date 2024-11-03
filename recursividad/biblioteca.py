def calcular_fibonacci(numero:int)->int:
    '''
    La funcion calcula el fibonacci de un numero.
    Recibe el numero (str).
    Retorna el resultado del calculo.
    '''
    if numero < 2:
        resultado = numero
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
    return resultado

def mostrar_serie_fibonacci(numero:int)->None:
    '''
    La funcion muestra la serie fibonacci.
    Recibe un numero (int).
    Retorna None.
    '''
    for i in range(numero + 1):
        print(calcular_fibonacci(i))

def determinar_suma_consecutiva(numero:int, x = 1)->bool:
    '''
    La funciona determina si el numero es resultado de la suma de numeros consecutivos.
    Recibe un numero.
    Retorna la True si es una suma consecutiva o False en caso contrario.
    '''
    if x >= numero:
        resultado = False
    elif 2 * x + 1 == numero:
        resultado = True
    else:
        resultado = determinar_suma_consecutiva(numero, x + 1)
    return resultado

def calcular_factorial(numero:int)->int:
    '''
    La funcion calcula el factorial de un numero.
    Recibe el numero (int).
    Retorna el factorial.
    '''
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    return resultado
