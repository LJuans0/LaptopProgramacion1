def pregunta_1(cristales: list[int]) -> int:
    """
    Retorna la cantidad de cristales que Jin-Woo puede usar para abrir la puerta dimensional.
    Parametros:
        cristales (list[int]): lista de valores enteros de energia magica.
    Retorna:
        int: numero de cristales validos.
    """
    sumador=0
    crisvalidos=0
    for i in cristales:
        sumador=0
        for digit in str(i):
            numero=int(digit)
            sumador+=numero
        if sumador%4==0 and i%2!=0:
            crisvalidos+=1
    return crisvalidos

def potencial(valor: int) -> int:
    """
    Calcula el potencial de energia maligna de un cristal de acuerdo a las reglas establecidas.
    """
    potencial=0
    if valor%2==0:
        potencial=valor/2
    else:
        potencial=valor*3+1

    return potencial

def pregunta_2(cristales: list[int]) -> list[int]:
    """
    Usa la funcion 'potencial' para evaluar cada cristal y retorna
    solo aquellos cuyo potencial de energia maligna es mayor a 50.
    
    Parametros:
        cristales (list[int]): lista de valores de los cristales.
    Retorna:
        list[int]: cristales cuyo potencial de energia maligna supera 50.
    """
    crislist=[]
    for i in cristales:
        valorar= potencial(i)
        if valorar>50:
            crislist.append(i)
    return crislist

def pregunta_3(datos: list[str], nombres: list[str]) -> list[str]:
    """
    Verifica si se puede formar un equipo para la operacion en la isla Jeju.
    Si es posible, retorna los nombres que cumplen los requisitos minimos.
    Si no, retorna lista vacia.
    """
    tanknum=0
    assnum=0
    healer=0
    listadenombres=[]
    for i in range(len(datos)): #indexador para saber posiciones en cada lista
        if datos[i][0]=="t" and (datos[i][-1]=="S" or datos[i][-1]=="A"):
            tanknum+=1
            listadenombres.append(nombres[i])
        if datos[i][0]=="a" and (datos[i][-1]=="A" or datos[i][-1]=="B"):
            assnum+=1
            listadenombres.append(nombres[i])
        if datos[i][0]=="s" and (datos[i][-1]=="S"):
            healer+=1
            listadenombres.append(nombres[i])
    if tanknum>=1 and assnum>=2 and healer>=1:
        return listadenombres
    else:
        return []
print(pregunta_3([ "tanque - S" , "asesino - A" , "asesino - B" , "sanador - S" , "tanque - B" , "tanque - S" ],[ "Baek Yoonho" , "Choi Jong - In" , "Kang Taeshik" , "Min Byung - Gu" ,
"Hwang Dongsoo" , "Lee Sung" ]))


def pregunta_4(objetos: list[int]) -> list[int]:
    """
    Modifica los poderes de los objetos segun las reglas de entrenamiento, 
    y filtra los objetos que no sean multiplos de 3, retornando la lista modificada.
    Parametros:
        objetos (list[int]): lista de poderes de los objetos.
    Retorna:
        list[int]: lista con los poderes modificados y filtrados.
    """
    objpoder=0
    objetosfinales=[]
    resultadfo=[]
    for i in objetos:
        if 50<=i<=100:
            if i%2==0:
                objetosfinales.append(i * 2)
            else:
                objetosfinales.append(i+20)#aqui mira bie nsi lo que se duplica es el obj o el objeto en si xdd
        elif i>100:
            objetosfinales.append(i)
    for y in objetosfinales:
        if y%3==0:
            resultadfo.append(y)
    return resultadfo
print(pregunta_4([40,60,170,120,80]))