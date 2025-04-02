#el historial de este script se lee de abajo para arriba
#

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