#Crear un sistema que sume los digitos de cualquier numero, segun el profo
n=int(input("Introduce tu numero prro aorita te  sumo sus digitos:VV →"))
x= n%10
xx= (n//10)%10
xxx= (n//10//10)%10
xxxx=(n//10//10//10)%10
suma= x+xx+xxx+xxxx
print(suma)
#facilito ya lo hice
#ahora veamos como lo hace la ia buey
def suma_digitos(numero):
    return sum(int(digito) for digito in str(abs(numero)))

# Solicitar al usuario un número
numero = int(input("Ingresa un número: "))
resultado = suma_digitos(numero)

print(f"La suma de los dígitos de {numero} es: {resultado}")
