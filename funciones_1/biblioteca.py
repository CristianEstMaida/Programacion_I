def calcular_iva(importe: int, iva: float = 0.21) -> float:
    '''
    Suma el importe con su respectivo IVA.
    Recibe el importe (int) y opcionalmente el porcentaje de IVA (float).
    Devuelve el importe con el IVA aplicado (float).
    '''
    resultado = importe * (1 + iva)
    return resultado

def mostrar_edad(fecha_actual:str, fecha_de_nacimiento:str)->int:
    '''
    Calcula la edad.
    Recibe la fecha actual (str) y la fecha de nacimiento (str).
    Devuelve la edad (int).
    '''
    posicion_actual = 0
    posicion_nacimiento = 0
    anio_actual = ""
    mes_actual = ""
    dia_actual = ""
    anio_de_nacimiento = ""
    mes_de_nacimiento = ""
    dia_de_nacimiento = ""    

    for digito in fecha_actual:
        if posicion_actual == 0 or posicion_actual == 1:
            dia_actual += digito
        if posicion_actual == 3 or posicion_actual == 4:
            mes_actual += digito
        if posicion_actual == 6 or posicion_actual == 7 or posicion_actual == 8 or posicion_actual == 9:
            anio_actual += digito
        posicion_actual += 1

    for digito in fecha_de_nacimiento:
        if posicion_nacimiento == 0 or posicion_nacimiento == 1:
            dia_de_nacimiento += digito
        if posicion_nacimiento == 3 or posicion_nacimiento == 4:
            mes_de_nacimiento += digito
        if posicion_nacimiento == 6 or posicion_nacimiento == 7 or posicion_nacimiento == 8 or posicion_nacimiento == 9:
            anio_de_nacimiento += digito
        posicion_nacimiento += 1
    
    anio_actual = int(anio_actual)
    mes_actual = int(mes_actual)
    dia_actual = int(dia_actual)
    anio_de_nacimiento = int(anio_de_nacimiento)
    mes_de_nacimiento = int(mes_de_nacimiento)
    dia_de_nacimiento = int(dia_de_nacimiento)
    edad = anio_actual - anio_de_nacimiento

    if mes_actual < mes_de_nacimiento or (
        mes_actual == mes_de_nacimiento and dia_actual < dia_de_nacimiento):
        edad -= 1

    return edad

def obtener_tipo_vehiculo(patente:str)->str:
    '''
    Dependiendo el formato obtiene el tipo de vehículo.
    Recibe la patente (str).
    Devuelve el tipo de vehículo (str).
    '''
    for i in patente:
        if ord(i) >= 65 and ord(i) <= 90:
            vehiculo = "auto"
        else:
            vehiculo = "moto"
        break
    return vehiculo

def calcular_cuil(dni:str, tipo:str)->str:
    '''Calcula el CUIL-CUIT.
    Recibe el dni (int) y el tipo (str).
    Devuelve el CUIT-CUIT (str).'''
    
    if tipo == 'M':
        xy = "20"
    elif tipo == "F":
        xy = "27"
    else:
        xy = "30"
    acumulador = 0
    posicion = 1
    cuil_incompleto = xy + dni

    for digito in cuil_incompleto:
        if posicion == 1 or posicion == 7:
            multiplicacion = 5
        elif posicion == 2 or posicion == 8:
            multiplicacion = 4
        elif posicion == 3 or posicion == 9:
            multiplicacion = 3
        elif posicion == 4 or posicion == 10:
            multiplicacion = 2
        elif posicion == 5:
            multiplicacion = 7
        elif posicion == 6:
            multiplicacion = 6
        posicion += 1
        digito = int(digito)
        acumulador += digito * multiplicacion
    resto = acumulador % 11
    if resto == 0:
        z = "0"
    elif resto == 1:
        if tipo == "M":
            z = "9"
            xy = "23"
        elif tipo == "F":
            z = "4"
            xy = "23"
        else:
            z = str(11 - resto)
    else:
        z = str(11 - resto)

    cuil = xy + "-" + dni + "-" + z
    return cuil

def sumar_numeros(num_a:int, num_b:int)->int:
    '''
    Calcula la suma de dos numeros
    Recibe dos numeros (int)
    Retorna el resultado de la suma
    '''
    resultado = num_a + num_b
    return resultado

def dividir_numeros(num_a:int, num_b:int)->float:
    '''
    Calcula la division entre dos numeros
    Recibe dos numeros (int)
    Retorna el resultado de la division
    '''
    resultado = num_a / num_b
    return resultado