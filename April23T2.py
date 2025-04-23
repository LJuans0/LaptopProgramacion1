def pregunta_1(n: int) -> int:
    """
    Parámetros:
    n (int): la posición n-ésima en la secuencia de Fibonacci

    Retorna:
    int: el valor del término F(n)
    """
    res=(1/(5**0.5))*(((1+5**0.5)/2)**n)-(((1-5**0.5)/2)**n)
    return round(res)


def pregunta_2(n: int) -> int:
    """
    Parámetros:
    n (int): el número de términos a sumar en la serie alternada

    Retorna:
    int: el resultado de la suma alternante
    """
    counter=1
    sum=0
    while counter <= n:
        if counter%2==0:
            sum-=counter
        else:
            sum+=counter
        counter+=1
    return sum

def pregunta_3(dinero_inicial: int, tasa_interes: float) -> int:
    """
    Parámetros:
    dinero_inicial (int): Cantidad inicial de dinero depositado.
    tasa_interes (float): Tasa de interés anual en formato decimal (por ejemplo, 0.05 para 5%).

    Retorna:
    int: El número de años que tomará duplicar el dinero.
    """
    tasa=0
    contadorinsanote=1
    while tasa<=dinero_inicial*2:
        tasa=dinero_inicial*(1+tasa_interes)**contadorinsanote
        contadorinsanote+=1
    return contadorinsanote-1

def pregunta_4(sea_wave: int, step: int) -> int:
    """
    Parámetros:
    sea_wave (int): Oleaje incial del dia 1 en cms
    step (int): Valor de incremento o disminución en centímetros del oleaje por día.

    Retorna:
    int: Retorna la suma de la cantidad de días con oleaje fuerte y muy fuerte
    """
    suma=0
    daycounter=1
    if (sea_wave >= 101):
        suma += 1
    while daycounter<=4:
        sea_wave += step
        if (sea_wave >= 101):
            suma+=1
        daycounter+=1
    return suma
print(pregunta_4(6,2)) #debe ser =0
print(pregunta_4(90,5)) #debe ser =2
print(pregunta_4(120,-5)) #debe ser =4