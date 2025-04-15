import math


def pregunta_1(radio: float) -> float:
    PI = 3.1416
    area = round(PI*radio**2,2)
    return area

def pregunta_2(a: float, b: float) -> float:
    hipotenusa = round(math.sqrt(a**2+b**2),2)
    return hipotenusa


def pregunta_3(cadena: str) -> int:
    longitud = len(cadena)
    return longitud


def pregunta_4(n: int) -> int:
    contador=0
    contador2=contador
    while contador<n:
        contador+=1
        contador2+=contador
    return contador2