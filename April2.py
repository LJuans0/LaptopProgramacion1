#el historial de este script se lee de abajo para arriba
#como hacer anotaciones: SHIFT+2
#Importar librerias
#para no usar sufijos puedes usar "from math import *" pero no es recomendable porque se confunden las llamadas
import math as m
#Programa que lee un numero entero de 3 digitos y que lo imprima alreves
rn=int(input("Introduce un numero de 3 digitos→"))
x= rn%10
xx= (rn//10)%10
xxx= (rn//10//10)%10
print("Numero Invertido:",100*x+10*xx+xxx)

#Programa de  hallar distancia entre 2 puntos
print("Punto 1:(_;_)")
P1x=float(input("Introduce la abcisa de un punto→"))
print("Punto 1:(",P1x,";","_")
P1y=float(input("Introduce la ordenada de un punto→"))
print("Punto 1:(",P1x,";",P1y,")")
P2x=float(input("Introduce la abcisa de otro punto→"))
print("Punto 1:(",P1x,";",P1y,")")
print("Punto 2:(",P2x,";","_")
P2y=float(input("Introduce la ordenada de otro punto→"))
print("Punto 1:(",P1x,";",P1y,")")
print("Punto 2:(",P2x,";",P2y,")")
distancia = m.sqrt((P1x-P2x)**2+(P1y-P2y)**2)
print("La distancia entre los 2 puntos que has introducido es:",distancia)

"""print("Raiz cuadrada:",m.sqrt(16))
print("Factorial:",m.factorial(10))
print("coseno en grados:",m.cos(16))
print("coseno en rad:",m.cos(m.radians(60)))
print("log base 2:",m.log2(64))
print("log natural:",m.log(64))"""

#como hacer anotaciones: SHIFT+2
"""#Como redondear
x = 3.4873652378284569
print("Redondeado con 2 decimales",round(x,2))
print("Redondeado con 3 decimales",round(x,3))
print("Redondeado con 4 decimales",round(x,4))"""

#juego del patito
kg = float(input("Introduzca su peso en gramos→"))
m = float(input("Ahora introduzca su altura en centimetros→"))
IMC = (kg/1000)/(m/100)**2
print ("Su índice de masa corporal es:",IMC)
if IMC <18.5:
    print("Estas bajo en peso")
if IMC >25.0:
    print("Tienes sobrepeso :v")


#pipipipipipipipip no pude hacerlo carajo
#Programa que reciba un numero representando una cantidad de segundos y lo presente en: DD:HH:MM:SS
sec = int(input("Cuantos segundos son:"))
DD=sec//86400
HH=sec//3600
MM=sec//60
SS=sec%60
print("DD:",DD,"HH:",HH,"MM:",MM,"SS:",SS)
#programa que permita ingresar un monto en soles y muestre su equivalente en dólares y euros
PEN=float(input("Cantidad de soles a convertir:"))
USD= PEN/3.68
EUR= PEN/3.96
print(PEN,"Soles son:",USD,"USD al cambio el 2 abr, 5:20p.m. UTC")
print(PEN,"Soles son:",EUR,"EUR al cambio el 2 abr, 11:20a.m. UTC")

#programa que permita hallar volumen de una esfera
r = float(input('Introduce el radio de tu esfera:'))
Area = 4*3.14159265359*r**2
Volume= (4/3)*3.14159265359*r**3
print("Area de tu esfera→", Area)
print("Vólumen de tu esfera→", Volume)