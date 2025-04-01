#Matrices
import random


dimension = int(input("Ingrese la dimension del tablero: "))
intentos = 0


def crearTablero(n):
    tablero = []
    for fila in range(n):
        filaNueva = []
        for columna in range(n):
            filaNueva.append('O')
        
        tablero.append(filaNueva)

    return tablero

def colocarTesoro(tablero):
    tamanio = len(tablero)
    fila = random.randint(0, tamanio -1) #se pone -1 porque el rango no incluye el maximo
    columna = random.randint(0, tamanio -1)
    tablero[fila][columna] = 'X'
    return tablero


def encontrarTesoro(tablero, fila, columna):
    if tablero[fila][columna] == 'X':
        print("Encontraste el tesoro")
    else:
        print("No es el tesoro")

tablero = crearTablero(dimension)
tablero = colocarTesoro(tablero)
print("Tablero:", tablero)


fila = int(input("Ingrese la fila: "))
while fila < 0 or fila > dimension:
    fila = int(input("Error. Ingrese la fila: "))

columna = int(input("Ingrese la columna: "))   
while columna < 0 or columna > dimension:
    columna = int(input("Error. Ingrese la columna: "))


if encontrarTesoro(tablero, fila-1, columna-1):
    print("Encontraste el tesoro")
else:
    print("No es el tesoro")    
