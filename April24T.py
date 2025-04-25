import math
def pregunta_1(radio: float, angulo: float) -> float:

    """
    Parámetros:
    radio (float): el radio de la circunferencia
    angulo (float): el ángulo del arco en grados sexagesimales

    Retorna:
    float: la longitud del arco, redondeada a dos decimales
    """
    longarco=radio*(angulo*math.pi/180)

    return round(longarco,2)
print(pregunta_1(10,20))
def pregunta_2(largo: float, ancho: float, profundidad: float, radio: float) -> int:
    """
    Parámetros:
    largo (float): largo de la piscina
    ancho (float): ancho de la piscina
    profundidad (float): profundidad de la piscina
    radio (float): radio de cada pelota

    Retorna:
    int: cantidad máxima de pelotas que pueden colocarse
    """
    cantmax=(largo//(2*radio))*(ancho//(2*radio))*(profundidad//(2*radio))
    return round(cantmax)

def pregunta_3(temp: float, humedad: float) -> str:

    """
    Parámetros:
    temp (float): temperatura en grados Celsius
    humedad (float): porcentaje de humedad relativa

    Retorna:
    str: nivel de riesgo
    """
    if temp>35 and humedad<30:
        return "Riesgo muy alto"
    elif 30<temp<=35 and humedad<40:
        return "Riesgo alto"
    elif 25<temp<=30 and humedad <30:
        return  "Riesgo alto"
    elif 25<=temp<=30 and 30<=humedad<=60:
        return "Riesgo moderado"
    else:
        return  "Riesgo bajo"

def pregunta_4(peso: int, altura: float) -> str:
    """
    Parámetros:
    peso (int): Peso en kilogramos (kg).
    altura (float): Altura en metros (m).

    Retorna:
    str: La categoría del IMC según la OMS.
    """
    indicedemasaprro=peso/altura**2
    if indicedemasaprro<18.5:
        return "Bajo peso"
    elif 18.5<=indicedemasaprro<25:
        return "Normal"
    elif 25<=indicedemasaprro<30:
        return "Sobrepeso"
    elif indicedemasaprro>=30:
        return "Obesidad"



