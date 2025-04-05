#de abajo para arriba el historial ya sabes

#Programa para ver si es par o impar
y= int(input("Paridad de tu numero→"))
def parimpar(y):
    if y%2 == 0:
        return "El Numero es par:"
    else:
        return "El Numero es impar:"
print (y, parimpar(y))

#Estructuras de control ifs y else alv
x= int(input("Positivo o negativo?→"))
if x <0:
    print("numero menor a 0")
elif x>0:
    print("numero mayor a 0")
else:
    print("pusiste 0 buey")

#sumar ahora 4 digitos con def
def sumardigitos(n):
    ix= n%10
    ixx=(n//10)%10
    ixxx=(n//10//10)%10
    ixiv=(n//10//10//10)%10
    sumador= 1000*ix+100*ixx+10*ixxx+ixiv
    sumadorins= ix+ixx+ixxx+ixiv
    return sumadorins

Num = int(input("Introduce un numero de 4 digitos a sumar→"))
print("Los digitos sumados:",sumardigitos(Num))

#definicion de las cosas prro
from math import sqrt
def hallardistancia(x1,y1,x2,y2):
    d=sqrt((x1-x2)**2+(y2-y1)**2)
    return d

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
distanciafinal= hallardistancia(P1x,P1y,P2x,P2y)
print("La distancia es:",distanciafinal)

#ejemplo 2,raiz cuadrada
from math import sqrt
nradical= float(input("Numero para sacar tu raiz cuadrada→"))
print('sqrt de tu inputeado:',sqrt(nradical))

#ejemplo 1, maximo de un conjunto de numeros
n1= float(input("Numero 1→"))
n2= float(input("Numero 2→"))
n3= float(input("Numero 3→"))
print("Máximo de los numeros inputeados :v",round(max(n1,n2,n3)))
print("Mínimo de los numeros inputeados :v",round(min(n1,n2,n3)))
