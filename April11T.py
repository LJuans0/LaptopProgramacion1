def pregunta_1(arista:  float) -> float:
    """
    Halla el area de un cuadrilatero ciclico 
    Parametros:
    	arista (float) :  Es la arista
    Retorna:
    	float : el volumen, valor expresado con 3 cifras decimales
    """
    Volumen = (1/4)*(15+7*5**0.5)*arista**3
    volumen = round(Volumen, 3)
    return volumen

def pregunta_2(lado1: float, lado2: float, lado3: float, lado4:float) ->float: 
    """
    Halla el area de un cuadrilatero ciclico 
    Parametros:
    	lado1 (float) :  El primer lado
            lado2 (float) :  El segundo lado
            lado3 (float) :  El tercer lado
            lado4 (float) :  El cuarto lado
    Retorna:
    	float : el area, valor expresado con 3 cifras decimales
    """
    s=(lado1 + lado2 + lado3 + lado4)/2
    k=((s-lado1)*(s-lado2)*(s-lado3)*(s-lado4))**0.5
    fin= round(k,3)
    return fin

def pregunta_3(numero : int)->str:
    """
    Determina la cantidad de digitos iguales que tiene un numero
    Parametros:
        numero (int) : un entero de 3 digitos
    Retorna:
        Str : Es la cadena que contiene el mensaje
    """
    x=numero % 10
    xx=(numero//10)%10
    xxx=(numero//10//10)%10
    if x == xx == xxx:
        return "Tiene tres digitos iguales"
    elif x == xx or x == xxx or xx == xxx:
        return "Tiene solo dos digitos iguales"
    else:
        return "Tiene tres digitos diferentes"

def pregunta_4( rango :  int) -> str: 
    """
    Halla la clasificacion de IQ 
    Parametros:
    	rango (int) :  Es el rango de IQ
    Retorna:
    	Str :  Es la clasificacion que corresponde segun el rango IQ
    	 ><
    """
    mensaje =""
    if(rango >= 130):
        return "Muy Superior"
    elif(120<=rango<=129):
        return "Superior"
    elif (110 <= rango <= 119):
        return "Arriba del Promedio"
    elif (90 <= rango <= 109):
        return "Promedio"
    elif (80 <= rango <= 89):
        return "Abajo del Promedio"
    elif (70 <= rango <= 79):
        return "Inferior"
    elif (rango <= 69):
        return "Deficiente"
    else:
        return "Ese es un numero negativo prro"