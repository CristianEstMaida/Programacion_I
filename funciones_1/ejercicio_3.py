''' 3) Desarrollar una función que reciba como parametros numero de DNI y
 [MASCULINO|FEMENINO|EMPRESA]. Deberá retornar el CUIL/CUIT formado por:
 CUIL/T: Son 11 números en total:
 XY–12345678– Z
 XY: Indican el tipo (Masculino, Femenino o una empresa)
 12345678: Número de DNI
 Z: Código Verificador
 Algoritmo: Se determina XY con las siguientes reglas:
 Masculino: 20
 Femenio: 27
 Empresa: 30
 Se multiplica XY 12345678 por un número de forma separada:
 X*5
 Y *4
 1 * 3
 2 * 2
 3 * 7
 4 *6
 5 * 5
 6 *4
 7 * 3
 8*2
 Se suman dichos resultados. El resultado obtenido se divide por 11. De esa división se obtiene un Resto que
 determina Z.
 Si el resto es 0 = Entonces Z = 0.
 Si el resto es 1 = Entonces se aplica la siguiente regla:
 *Si es hombre: Z = 9 y XY pasa a ser 23
 *Si es mujer: Z = 4 y XY pasa a ser 23
 Caso contrario Z pasa a ser (11- Resto).
 Ejemplo de Cálculo de CUIL CUIT:
 Masculino DNI 12345678
 1-Determinar el Tipo
 XY es 20
 Hacemos el cálculo
 2 * 5=10
 0*4=0
 1 * 3=3
 2 * 2=4
 3 * 7=21
 4 *6=24
 5 * 5=25
 6 *4=24
 7 * 3=21
 8*2=16
 Realizamos la suma de (10+0+3+4+21+24+25+24+21+16) = 148
 Dividimos por 11 para obtener Z (el código verificador)
 148 / 11 = 13,4545 —> 13 (Redondeo)
 Obtenemos el resto de la división:
 148– (13*11) = 5
 Determinamos Z:
 11- 5 = 6
 Conclusión: CUIL-CUIT 20-12345678-6'''

def mostrar_cuit(dni:int, tipo:str)->str:
    '''
    Calcula el CUIL-CUIT.
    Recibe el dni (int) y el tipo (str).
    Devuelve el CUIT-CUIT (str).
    '''
    match tipo:
        case "MASCULINO":
            xy = 20
        case "FEMENINO":
            xy = 27
        case "EMPRESA":
            xy = 30
    
    dni_1 = dni // 10000000
    dni_2 = dni // 1000000 - dni // 10000000 * 10
    dni_3 = dni // 100000 - dni // 1000000 * 10
    dni_4 = dni // 10000 - dni // 100000 * 10
    dni_5 = dni // 1000 - dni // 10000 * 10
    dni_6 = dni // 100 - dni // 1000 * 10
    dni_7 = dni // 10 - dni // 100 * 10
    dni_8 = dni % 10

    suma = 0
    suma += (xy // 10) * 5
    suma += xy % 10 * 4
    suma += dni_1 * 3
    suma += dni_2 * 2
    suma += dni_3 * 7
    suma += dni_4 * 6
    suma += dni_5 * 5
    suma += dni_6 * 4
    suma += dni_7 * 3
    suma += dni_8 * 2
    z = suma // 11 
    z = suma - z * 11
    
    if suma % 11 == 0:
        z = 0
    elif suma % 11 == 1:
        if z == 9 and tipo == "MASCULINO":
            xy = 23
        if z == 4 and tipo == "FEMENINO":
            xy = 23
    else:
        z = 11 - z
    cuil_cuit = str(xy) + "-" + str(dni) + "-" + str(z)
    return cuil_cuit
    

resultado = mostrar_cuit(39550055,"MASCULINO")
print(resultado)