#historial de abajo para arriba

#para añadir cosas a una lista
lista=[0]
lista.append("Ho")
lista.append(1)
lista.append(1==1)
s=lista[0:4:2]
print(lista)
print("Rangeado:",s)
#listas
"""listas=33,44,55

print(listas[1])
contador=0
sumador=0
while contador<len(listas):
    sumador+=listas[contador]
    contador+=1
print(sumador/len(listas))
"""

#cortes
"""cadena="Ingenio en acción"
print(cadena[0:7:1]) #es como el range
print(cadena[::-1]) #es como el range
print(cadena[-1:-7:-1]) #es como el range"""

#metodos
"""texto="Hola papus"
print(texto.find("p")) #encuentra desde el primero
print(texto.rfind("p")) #encuentra desde el ultimo
print(texto.count("o"))
if texto.find("z")==-1:
    print("no existe z")"""

#programa que lea una grase e imprima del ultimo hacia el primero
"""texto="Ingenio en acción"
cont=len(texto)-1
while cont>=0:
    print(texto[cont],end="")
    cont-=1"""

#programa que lee cuantas a hay en un texto, usando while y for
"""contador=0
contadordea=0
asenuntxt="pApUtS WaZA"

for letra in asenuntxt:
    if letra=="a" or letra=="A":
        contadordea+=1
print(contadordea)
contadordea=0

while contador<len(asenuntxt):
    if "a" in asenuntxt[contador] or "A" in asenuntxt[contador]:
        contadordea+=1
    contador+=1
print(contadordea)"""

#iteracion de textos
"""texto="Waza"
print(texto+"aaaaa")
print(texto*3)
print("W" in texto)
print("w" in texto)"""

#deletrear utec con while
"""name=input("waza")
cont=0
while cont<len(name):
    print(name[cont])
    cont+=1"""

 #imprimamos utec
"""nombre="UTEC"
print(nombre[-4])
print(nombre[-3])
print(nombre[-2])
print(nombre[-1])"""
