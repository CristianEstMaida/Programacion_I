def calcular_fibonacci(numero:str)->int:
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
    for i in range(numero + 1):
        print(calcular_fibonacci(i))

def determinar_suma_consecutiva(numero:int, x = 1)->bool:
    if x >= numero:
        resultado = False
    elif 2 * x + 1 == numero:
        resultado = True
    else:
        resultado = determinar_suma_consecutiva(numero, x + 1)
    return resultado

def calcular_factorial(numero:int)->int:
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    return resultado