#historial de abajo para arriba
from contextlib import nullcontext

#programa que determine cuando pones un 0 y cuente si los numeros que pusiste son pares o no
n=int(input("numero [con 0 termina]:"))
cdnl=0
conpar=0
conimpar=0
while n!=0:
    if n%2==0:
        conpar+=1
    else:
        conimpar+=1
    cdnl+=1
    n=int(input("Numero [con 0 termina]"))
print("Numeros leidos:",cdnl)
if conpar!=0:
    print("Numeros pares:", conpar)
if conimpar!=0:
    print("Numeros impares:", conimpar)

#funcion que suma determinados numeros de una serie tal que: 1**2 + 2**2 + 3**2 + 4**2 + 5**2... ...
def hallarSuma(nter:int) -> int:
    i = 1
    opr = 0
    while i <= nter:
        opr += i ** 2
        i += 1
    return (opr)

#suma 2**1 + 2**2 + 2**3 + 2**4 + 2**5 + 2**6 + 2**7 + 2**8
"""i=1
opr=0
while i<=100:
    opr+=i
    i+=1
print(opr)"""

#suma 2**1 + 2**2 + 2**3 + 2**4 + 2**5 + 2**6 + 2**7 + 2**8
"""i=1
opr=0
while i<=8:
    opr+=2**i
    i+=1
print(opr)"""

#suma 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2
"""i=1
opr=0
while i<=6:
    opr+=i**2
    i+=1
print(opr)"""

#suma 1/1 + 1/2 + 1/3 + 1/4 + 1/5
"""i=1
opr=0
while i<=5:
    opr+=1/i
    i+=1
print(opr)"""

#programa que permita leer como dato unnumero y el programa imprima la tabla de multiplicardel numero que se ha ingresado con ese dato
nn0=int(input("Tabla de multiplicacion de este numero:"))
nn0r=1
while nn0r<=10:
    print(nn0,"x",nn0r, "=", nn0*nn0r)
    nn0r += 1

#programa que imprima los 15 numeros naturales que son multiples de 7
"""nn=1
nn2=0
while nn<=15:
    nn2+=7
    print(nn, "-", nn2)
    nn += 1"""

#programa que imprima 7 veces utec
"""numeror=1
while numeror <=7:
    numeror +=1
    print("UTEC")"""

#programa que imprime 9,8,7,6,5,4
"""numerouniversal=9
while numerouniversal >=4:
    print(numerouniversal, end="")
    numerouniversal -=1"""

#programa que imprime 5,10,,15,20,25,30
"""numerouniversal=5
while numerouniversal <=30:
    print(numerouniversal, end="")
    numerouniversal +=5"""

#programa que imprime ,2,3,4,5,6,7,8
"""numerouniversal=2
while numerouniversal <= 8:
    print(numerouniversal, end="")
    numerouniversal +=2"""

#programa que imprime 1,2,3,4,5,6,7,8
"""numerouniversal=1
while numerouniversal <= 8:
    print(numerouniversal, end="")
    numerouniversal +=1"""