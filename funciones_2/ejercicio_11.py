from biblioteca import *

def completar_dni(numero:str)->str:
    '''
    La función completa el DNI de una persona con ceros hasta llegar a 8 caracteres.
    Recibe una cadena de caracteres que contiene números.
    Retorna la cadena cadena de 8 caracteres con los ceros correspondientes. 
    '''
    dni = numero

    if largo_cadena(numero) == 6:
        dni = '00' + numero
    elif largo_cadena(numero) == 7:
        dni = '0' + numero
    return dni    

mensaje = "Ingrese el DNI: "
numero = input(mensaje)
while validar_numero_entero(numero) != True:
    numero = input(mensaje)
while validar_dni(numero) != True:
    numero = input(mensaje)

print(completar_dni(numero))
