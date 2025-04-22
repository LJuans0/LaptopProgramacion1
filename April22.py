#estructura de control anidadas
#historial de abajo para arriba
from math import factorial

#ejemplo 4: programa que permita leer como dato un numero entero mayor a 1, dato que el programa debe validar desde el bloque principal, luego el programa por medio de una funcion lineal hallara la suma de todos los factoriales desde 1 hasta el numero que se ingreso como dato
#1!+2!+3!+4!......n!
nRDM = int(input("Número a sumar su factoriales→"))
contador=1
sumadorinsano=0
while  contador<=nRDM:
    sumadorinsano += factorial(contador)
    contador +=1

print(sumadorinsano)

#ejemplo 3: hacer un arbol de numeros invertido
numfilas = int(input("Número de filas→"))
cfilas2=1
while numfilas <1 or numfilas>9:
    print("»El número debe ser un valor entre 1 a 9")
    numfilas = int(input("Número de filas→"))
ccounter=1
while cfilas2<=numfilas:
    ccounter = 1
    #hacer que imprima desde 1 hasta filas pero invertido, osea de filas a 1
    while ccounter<=numfilas-cfilas2+1:
        print(ccounter,end="")
        ccounter+=1
    cfilas2 -=1
    print()


#ejemplo 2 insanote: hacer un arbol de numeros
"""numfilas = int(input("Número de filas→"))
cfilas2=1
while numfilas <1 or numfilas>9:
    print("»El número debe ser un valor entre 1 a 9")
    numfilas = int(input("Número de filas→"))
ccounter=1
while cfilas2<=numfilas:
    ccounter = 1
    while ccounter<=cfilas2:
        print(ccounter,end="")
        ccounter+=1
    cfilas2 +=1
    print()"""

#ejemplo 1 programa que perimta leer como dato cantidad de alumnos y la cantidad de notas por alumno y el programa halle para cada alumno el promedio
numalumnos=int(input("Numero de alumnos:"))
calumnos=1
numnotasporalumno=int(input("Notas por alumno:"))
while calumnos<=numalumnos:
    cnotas=1
    sumnotas = 0
    while cnotas <= numnotasporalumno:
        nota = int(input(f"Nota {cnotas} de alumno {calumnos}:"))
        cnotas += 1
        sumnotas +=nota
    promedio = sumnotas/(cnotas-1)
    print(f"Promedio del alumno {calumnos}: {promedio}")
    calumnos+=1

#bucles anidados asi insanotes
ancho=int(input("Ancho:"))
alto=int(input("Alto:"))
cfilas=1
while cfilas<=alto:
    cc=1
    while cc<=ancho:
        print("#", end="")
        cc+=1
    print("")
    cfilas +=1