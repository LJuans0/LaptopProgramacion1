#listas y esas kks
#historial de abajo para arriba
import random
from random import randint
from traceback import print_tb


#.pop elimina de la lista los elementos ultimamente
#.append añade elementos a la lista ultimamente
#del elmina elementos de la posicion de la lista
#.remove elimina los valores de una lista qwertyuiopasdfghjklñzxcvbnm    wyx<v>z

#Ejercicio cuatrote pipipipipi
def procesar(frase):
    listar=frase.lower().split(" ")
    vocalist=[]
    consolist=[]
    for i in listar:
        if i[-1] in ["a","e","i","o","u"]:
            vocalist.append(i)
        else:
            consolist.append(i)
    return vocalist,consolist
print(procesar("Waza pibes como se papea xdd"))

#programa que genere una lista de n numeros enteros de 9 al 10 y encuentre las posiciones de un determinado numero en ese lista
#creando otra lista, ufff me salio goty este, profo menso no pone ejemplos y aun asi lo logre siuuuuu.
#generar una lsita aleatoria
"""listaa=[]
for i in range(0,10):
    listaa.append(randint(1,9))

print(listaa)
def posiciones(lista,numero):
    listanueva=[]
    for i in range(0,len(lista)):
        if lista[i] == numero:
            listanueva.append(i)
    return listanueva
print(posiciones(listaa,4))"""

#NO USAR APPEND DE LISTAS; SOLO SUMALAS W

#AQUI SI COPIA SU VALOR, usa .copy
"""x=[10,20,30,40]
y=x.copy()
x[0]=-100
x.append(50)"""

#LAS VARIALES APUNTAN A LA LISTA; NO TOMAN SU VALOR
"""x=[10,20,30,40]
y=x
x[0]=-100
x.append(50)"""

#recorrer una lista
"""lista2=[";v",1,2,3,1]
for i in lista2:
    print(i)

lista=[":v"]
lista.append("HailGrasa")
lista.append("mr.Graso")
lista.append("Grasa1")
lista.append("Grasa2")
lista.append("Grasa3")
print(":v"in lista)
print(":v"not in lista)
print(lista)
lista.pop()
lista.pop(0)
del lista[0]
lista.remove("Grasa2")
print(lista)"""