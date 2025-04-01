listaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def valoresPares(listaNumeros):
    return [numero for numero in listaNumeros if numero % 2 == 0]

print("Lista de números pares:", valoresPares(listaNumeros))