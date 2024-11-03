# Desarrollar una función que determine si un número que recibirá por parámetro es primo. Si es primo
# deberá devolver un True, de lo contrario False.

def determinar_primo(numero:int)->bool:
    '''
    La función determina si un número es primo o no.
    Recibe un número entero.
    Retorna True en caso de que el número sea primo, sino retorna False.
    '''
    
    contador = 0
    es_primo = True

    if numero < 2:
        es_primo = False

    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
        if contador > 2:
            es_primo = False
            break
        
    return es_primo


numero = int(input("Ingrese un número: "))
print(determinar_primo(numero))