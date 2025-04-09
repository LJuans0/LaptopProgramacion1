#el historial de este script se lee de abajo para arriba

#ejemplo 4

#ejemplo 3
pi= int(input('Paridad de tu numero:'))
print((pi%2==0)*"Par"+(pi%2!=0)*"ImPar")

#ejemplo 2
consumo= float(input('Pon tu consumo en kW:'))
condicionsota1 = (consumo<=100)*(consumo*0.4522)
condicionsota2 = (consumo>100)*(45.22+(consumo-100)*0.7)

print(condicionsota1 + condicionsota2)

#ejemplo 1 waza
edad2= int(input('Pon tu edad:'))
condicionsita = edad2<18
mayor = (not condicionsita)*("Mayorsito")
menor = (condicionsita)*('Menorsito')
print('Eres', mayor + menor)
print((edad2<18)*"menorsito"+(edad2>=18)*'mayorsito')
#ay un kahoot que miedo

#ejemplos de and, or, not
"""print("true and false?",True and False)
print("true and true?",True and True)
print("true or false?",True or False)
print("false or false?",False or False)
print("not true?",not True)
print("4<10",4<10)
print("4<=10",4<=10)
print("4>=5",4>=5)
print("4==4",4==4)
print("4!=4",4!=4)
print("4<5<8",4<5<8)
print("casa"<"salon") #esto hace segun el orden alfabetico
print("casa"<"sol")
print((2<5)+(5<10))
print(2+4<10)"""
