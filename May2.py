#historial de abajo para arriba

#parametros por defecto
def registro(nomvre,cod,pais="Peru"):
    """waza"""
    print("hola",nomvre)
    print(cod,"guardando en el registro de los",pais)

registro("julio","2010256")
registro("juan","2010256","peru")
registro("julio","2010256","waza")
registro(cod="12314",nomvre="perro")



#alcance de una variable
def funcion(a):
    a=2
    b=3
    global x
    x=1
    return x+b+a

#programa que convierte segundos a :dias,horas, minutos y segundos
def convertir(seg):
    dias=seg//86400
    sobra=seg%86400
    horas=sobra//3600
    sobra=sobra%3600
    minutos=sobra//60
    segundos=sobra%60
    return dias,horas,minutos,segundos

def tripleRetorno(n1,n2,n3):
    mayor=max(n1,n2,n3)
    menor=min(n1,n2,n3)
    medio=(n1+n2+n3)-(mayor+menor)
    return  mayor, menor, medio
major, menor, medio=tripleRetorno(78,123,45)

def menu():
    while True:
        print("MENU")
        print("1. Registrar un usuario")
        print("2. Exit")
        n = int(input("Seleccione una opción:"))
        if n == 1:
            nombre = input("Ingrese nombre:")
        elif n == 2:
            break
        else:
            print("Opción Invalida")

def cuadrado(x:float):
    return x**2