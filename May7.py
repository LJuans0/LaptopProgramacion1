#historial de abajo para arriba
#cadenas de strings
#que es el string? dato en python que consiste en una secuencia ordenada de caracteres

#mandar una letra al final
"""def rotaciones(frase,n):
    for i in range(n):
        frase=frase[1:]+frase[0]
    return frase
print(rotaciones("hola",2))"""

#programa que permita escribir un texto y devolver el tesxto alternando las mayusculas y minusculas
"""texto=input("Pon tu texto:")
textofinal=""
for i in range(len(texto)):
    if i%2==0:
        textofinal+=texto.upper()[i]

    else:
        textofinal+=texto.lower()[i]
print(textofinal)"""
#programa que tome los ultimos caracteres de un string que ingrese el usuario y cree uno nuevo que repita esa secuencia de 2 caracteres
"""texto=input("Pon tu texto:")
if len(texto)<2:
    print("No cumple")
else:
    textoplus=texto[-2:]
    print(texto+textoplus*3)"""

#programa que agregue ing al final de cualquier string, si ya termina en ing entonces agregar ly
"""textoprueba="Dying"
if textoprueba[-3:]=="ing":
    textoprueba+="ly"
else:
    textoprueba+="ing"
print(textoprueba)"""

#programa que imprima todas las posiciones de la a
"""txt="wazaaA"
for i in range(len(txt)):
    if txt[i]=="a" or txt[i]=="A":
        print(i,end=", ")"""

#programa que cuente as
"""txt="WAZAAAAAAaaaa"
txtlowered=txt.lower()
print(txtlowered.count("a"))"""

"""z="como se papea"
print(z[4]) #imprime el espacio increible
print(z.capitalize())
print(z.upper())
print(z.lower())
print(z.replace("c","r")) #no estas cambiando la variable
print(z.replace(" ","")) #no estas cambiando la variable
print(z.find("c"))
print(z.count("c"))
print(z[:4:])
for i in z:
    print(i)
print("-".join(z)) #c-o-m-o...
print(z.split(" ") #hace una lista con cada palabra
"""