import random

def contarPalos(mano, palo):
    cantidad = 0
    for numero, paloCarta in mano:
        if paloCarta == palo:
            cantidad += 1
    return cantidad
    
def repartir(mazo, cantidad):
    mano = []
    
    cantidadCartas = len(mazo)
    
    while len(mano) < cantidad:
        carta = mazo[random.randint(0, cantidadCartas-1)]
        
        if carta not in mano:
            mano.append(carta, 'oro')
    
    return mano

def armarMazo(numeros, palos):
    mazo = []
    for numero in numeros:
        for palo in palos:
            mazo.append((numero,palo))


    return tuple(mazo)  



numeros = (1,2,3,4,5,6,7,8,9,10,11,12)
palos = ('copa', 'basto', 'oro', 'espada')


mazo = armarMazo(numeros, palos)

mano = repartir(mazo, 10)
print(mano)
print("Cantidad oros: ", contarPalos(mano,'oro'))