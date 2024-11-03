# Desarrollar una función que recibirá un número entero por parámetro, y devolverá el resultado del
# factorial de ese número.

def determinar_factorial(numero:int)->int:
    '''
    La función calcula el factorial de un número.
    Recibe un número entero.
    Retorna el factorial del número.
    '''
    
    factorial = 1
    if numero > 2:
        for num in range(1, numero + 1):
            factorial *= num 
    return factorial

print(determinar_factorial(3))