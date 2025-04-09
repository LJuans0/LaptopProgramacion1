#el historial de este script se lee de abajo para arriba
#ejemplo 8
z1= int(input('Numero entero 1:'))
z2= int(input('Numero entero 2:'))
z3= int(input('Numero entero 3:'))
mayor = max(z1,z2,z3)
menor = min(z1,z2,z3)
medio = z1+z2+z3 - mayor - menor
print(menor,medio,mayor)

#ejemplo 5
costo = float(input('Sutotal:'))
monto = costo*0.23+costo
print("Total:", monto)

#ejemplo 4
tri1= int(input('Lado 1 de tu triangulo:'))
tri2= int(input('Lado 2 de tu triangulo:'))
tri3= int(input('Lado 3 de tu triangulo:'))
ec1=tri1+tri2>tri3
ec2=tri2+tri3>tri1
ec3=tri1+tri3>tri2
print((ec1 and ec2 and ec3)*"Es Triangulo"+(not(ec1 and ec2 and ec3))*"No es triangulo")
#print((ec1*ec2*ec3)*("Es triangulo")+(ec1*ec2*ec3)*("No es triangulo"))

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
