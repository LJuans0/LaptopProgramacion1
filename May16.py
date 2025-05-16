#historial de abajo para arriba
#matrices, ten en cuenta que se cuenta DESDE EL 0


poblacion = [
[ 106, 107, 111, 133, 221, 767, 1766 ],
[ 502, 635, 809, 947, 1402, 3634, 5268 ],
[ 2, 2, 2, 6, 13, 30, 46 ],
[ 163, 203, 276, 408, 547, 729, 628 ],
[ 2, 7, 26, 82, 172, 307, 392 ],
[ 16, 24, 38, 74, 167, 511, 809 ]
]
continentes = [
"Africa",
"Asia",
"Australia",
"Europe",
"North America",
"South America"
]

canthab=0
totalaustr=0
matrizinsana=[]
filas=6
column=7
for q in range(filas):
    canthab+=poblacion[q][5]
print("Canthab en 2000:",canthab)
for a in range (column):
    totalaustr+=poblacion[2][a]
print("Canthab totales en austr:",totalaustr)

for i in range(filas):
    for j in range(column):
        print("%15d"%(poblacion[i][j]),end="")
    print()




"""medaller=[
    ["Canada",  0,3,0],
    ["Italy",   0,0,1],
    ["Germany",0,0,1],
    ["Japan",1,0,0],
    ["Kazakhstan",0,0,1],
    ["Rusia",3,1,1],
    ["South Korea", 0,1,0],
    ["United States",1,0,1]
]
nfila=8
ncolumna=4
for a in range(nfila):
    for b in range(ncolumna):
        print("%3s"%(medaller[a][b]),end="")
    print()

listar= [
    [20,15,18,19],
    [13,12,11,15],
    [20,18,17,11]
]
nfil=3
ncol=4
"""
#calcular soma de todos los elementos
"""suma=0
sumador2=0
sumador3=0

for l in range(nfil):
    for k in range(ncol):
        suma+=listar[l][k]

for o in range(ncol):
    sumador2+=listar[0][o]
    sumador2+=listar[2][o]

for r in range(ncol):
    sumador3+=listar[0][r]
    sumador3+=listar[2][r]
for w in range(ncol):
    if not(w == 1 or w==2):
        sumador3+=listar[1][w]
print("Tarea 1:", suma)
print("Tarea 2:", sumador2)
print("Tarea 3:", sumador3)"""

#imprime la matriz ordenada,buey
"""for i in range(nfil):
    for j in range(ncol):
        print("%3d"%(listar[i][j]),end="")
    print()"""

"""lista=[[1,2,3],[1,2,345,23],[123534,23,9]]
print(lista[0][0])
#sumar elementos de columna 2
print(lista[0][2]+lista[1][2]+lista[2][2])
#sumar elementos de fila 2
print(lista[2][0]+lista[2][1]+lista[2][2])

#imprimir columna 2 de cada fila con for
for i in range(3):
    print(lista[i][2])"""