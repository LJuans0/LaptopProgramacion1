def pregunta_1(numVuelosDeIDa: int, numVuelosDeRegreso: int) -> float:
    # Tu solución inicia aquí
    numefectivos=numVuelosDeIDa + numVuelosDeRegreso
    cantidad= numefectivos*180*22.5
    return cantidad
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.

def pregunta_2(anguloEnRadianes: float) -> float:
    # Tu solución inicia aquí
    pi = 3.1415
    calc = anguloEnRadianes/(pi/180)
    anguloEnSexagesimales = round(calc,2)
    return anguloEnSexagesimales
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.    

def pregunta_3(magnitud: float) -> str:
    # Tu solución inicia aquí<>
    if magnitud >= 10:
        tipoDeSismo = "Meteorico"
    elif 8<=magnitud<10:
        tipoDeSismo = "Cataclismo"
    elif 7<=magnitud<8:
        tipoDeSismo = "Mayor"
    elif 6<=magnitud<7:
        tipoDeSismo = "Fuerte"
    elif 5<=magnitud<6:
        tipoDeSismo = "Moderado"
    elif 4<=magnitud<5:
        tipoDeSismo = "Ligero"
    elif 3<=magnitud<4:
        tipoDeSismo = "Menor"
    elif 2<=magnitud<3:
        tipoDeSismo = "Muy Menor"
    elif magnitud<2:
        tipoDeSismo = "Micro"

    return "El sismo es " + tipoDeSismo
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.

def pregunta_4(peso: float, altura: float) -> str:
    # Tu solución inicia aquí
    IMC=peso/altura**2
    if IMC >= 40:
        tipoDePeso = "Obesidad Morbida"
    elif 35<=IMC<40:
        tipoDePeso = "Obesidad Media"
    elif 30<=IMC<35:
        tipoDePeso = "Obesidad Leve"
    elif 25<=IMC<30:
        tipoDePeso = "Sobrepeso"
    elif 18.5<=IMC<25:
        tipoDePeso = "un peso normal"
    elif IMC<18.5:
        tipoDePeso = "Bajo Peso"
    else:
        tipoDePeso = "pon cifras reales w"
    return "Ud tiene " + tipoDePeso
# Tu solución termina aquí. Recuerda retornar lo que hayas calculado.
