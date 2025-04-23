
def pregunta_1( dia : int, mes: int) ->str: 
    """
    Halla el nombre de la estacion del anio en que una persona nacio
    Parametros:
        dia (int) :  Es el dia en que nacio
        mes (int) :  Es el numero del mes en que nacio
    Retorna:
        str : la cadena indica en nombre del mes en que nacio, de acuerdo a la tabla
    
        |===========|==============|===============|
        |  Estación |    Inicio    |      Fin      |
        |===========|==============|===============|
        | Verano    | 21 Diciembre | 20 Marzo      |
        | Otonno    | 21 Marzo     | 21 Junio      |
        | Invierno  | 22 Junio     | 22 Setiembre  |
        | Primavera | 23 Setiembre | 20 Diciembre  |
        |===========|==============|===============|
    """
    if mes==12 or 1<=mes<=3:
        if (dia>=21 and mes==12) or (mes == 3 and dia<=20):
            return "Verano"
        elif 1<=mes<=2:
            return "Verano"
    elif (mes==3 and dia>=21) or (4<=mes<=5) or (mes == 6 and dia<=21):
        return "Otonno"
    elif (mes==6 and dia>=22) or (7<=mes<=8) or (mes == 9 and dia<=22):
        return "Invierno"
    else:
        return "Primavera"

def pregunta_2( n1 :  int, n2: int) ->int: 
    """
    Halla la suma de todos los numeros desde n1 hasta n2, que cumplan al menos una de las condiciones
    Parametros:
        n1 (int) : es el primer numero
        n2 (int) : es el segundo numero
    Retorna:
        int : es la suma 
    """
    ccccounter=n1
    sumador=0
    while ccccounter<=n2:
        if((ccccounter%7==0 and ccccounter%5==0) or (ccccounter%3==0 and ccccounter%4==0)):
            sumador += ccccounter

        ccccounter+=1
    return sumador

def pregunta_3(numero : int)-> int:
    """
    Determina la suma de los divisores menores del numero
    Parametros:
        numero (int) : un numero entero 
    Retorna:
        int : Es la  suma de los divisores menores del numero
    """
    cccounter=1
    sum2=0
    while  cccounter<numero:
        cociente=numero%cccounter
        if(cociente==0):
            sum2+=cccounter
        cccounter+=1

    return sum2

def pregunta_4( numeroDeTerminos :  int) -> int: 
    """
    Halla la sumatoria de los terminos de la serie
    Parametros:
    	numeroDeTerminos (int) :  Indica la cantidad de terminos
    Retorna:
    	 int :  La suma de los terminos de la serie
    """
    sum=0
    ccounter=1
    while ccounter<=numeroDeTerminos:
        sum += ccounter ** 3
        ccounter+=1

    return sum