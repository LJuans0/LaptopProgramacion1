#historial de abajo para arriba
#for trabaja sobre iterables (toda secuencia ordenada es iterable, asi como strings "HOLA")

#calculando pi alavergota
suma=True
pi=0
for i in range(1,50+1):
    if suma:
        pi += 4 /(2*i-1)*(-1)**(i+1)
print(round(pi,10))

#programa que determina numeros primos
"""def esPrimo(n:int):
    bool=True
    for i in range(2, n):
        if n % i == 0:
            bool= False
    return bool"""

#programa que lea como un dato un numero mayor a cero y el programa imprima un triangulo como se muestra en el ejemplo
"""target=5
for i in range (1,target+1):
    espacios =(target-i)*"  "
    michis = i*"#"
    print(espacios+michis)"""


#realizar un programa que permita contar con pilotos. el programa lee como dato un numero cyo rango puede estar del 1 al 100
"""numpalitos=int(input("Introduce un numero:"))
contador=0

while not(1<=numpalitos<=100):
    numpalitos=int(input("Introduce un numero:"))

for i in range(1,numpalitos+1):
    if contador==5:
        print(end=" ")
        contador=0
    print("I", end="")
    contador+=1"""


#immprimir los divisores del numero 200
"""for i in range(1,200):
    if 200%i==0:
        print(i,end=" ")"""

#imprimir 9,7...-7
"""for i in range(9,-8,-2):
    print(i,end=",")"""

#imprimir -5...3
"""for i in range(-5,4):
    print(i,end=",")"""

#imprimir 5,10..35
"""for i in range(5,36,5):
    print(i,end=",")"""

#imprimir 2,4,6...18
"""for i in range(2,19,2):
    print(i,end=",")"""

#imprimir 1,2,3,4,5,6,7,8,9,10,11
"""for i in range(1,12):
    print(i,end=",")
"""
"""for i in range(2,5): #nomas imprime el inicial pero no el final chchchch
    print(i)"""

"""for i in ["hola",4,False,7.5]:
    print(i, end="-")"""

"""for i in "Waza":
    print(i)"""