#HISTORIAL DE ABAJO PARA ARRIBA
import random

#calcular si es primo o no es primo
def esPrimo(num):
    if num==1:
        return False
    for divisor in range(2,num):
        if num%divisor==0:
            return False
    return True

#hacer un factorial solo con for
def factorial(numero:int) -> int:
    f=1
    for fact in range(1,numero+1):
        f *= fact
    return  f

#funcion sumo
def suma(n1,n2):
    suma=n1+n2
    return suma

#simular el tiro de 10 dados
"""for a in range(1,11):
    print(f"Lanzamiento {a}: {random.randint(1,6)}")"""

#funciones otra vez ppipipipipipipiipípipipipip´´i´´pip´pii´ppi´pi´pi´pipi´pi´pi´pi´pi´pi´pi´pi´pi´pi´pi´pi´pi´p´pi´pi´pi´pi´pi´pi´pi´pi´pi´pi´pi´pi´pi
def volumen_cubo(lado):
    volumen=lado**3
    return volumen

#secuendia ce 90 a 25
"""for wda in range(90,25,-5):
    print(wda,end=", ")"""

#secuencia 0,-1,-2,......,-8
"""for awda in range(0,-9,-1):
    print(awda)"""

#primer ejercicio: imprimir 7 veces la palabra rio
"""for wdaw in range(7):
    print("Rio")"""

#usando la funcion range
#range(inicio, fin, step)
#range(fin)
"""for numero in range(34,1,-3):
    print(numero)

for numero in range(2,7,2):
    print(numero)"""

#iterar sobre una lista, aqui lo hago pero con int porque ya lo hice abajo:v
"""waza="HOLAAAsa"
for chariz in waza:
    print(chariz)"""

#imprime asi por separado
"""lista=["hola","prros","xd","xddd"]
for char in lista:
    print(char)"""

#imprimir 100 veces sorry
"""for _ in range(100):
    print("waza")"""