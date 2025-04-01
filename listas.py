#QUE ES UNA LISTA? COMO SE COMPONE? QUE PROPIEDADES TIENE? COMO SE ARMAN Y COMO SE RECORREN?

#Una lista es una estructura de datos que permite almacenar una colección de elementos.
#Puede contener elementos de diferentes tipos (números, cadenas, listas, etc.).
#Las listas son mutables, lo que significa que se pueden modificar después de su creación.

#La primera posicion de la lista, se conoce como la posición 0
ejemploLista = [1, 2, 3, 4, 5]

otroEjemplo = ["a", "b", "c", "d", "e"]


#Como acceder a un elemento de la lista?
#Acceder al primer elemento de la lista. se puede acceder al primer elemento de la lista utilizando el índice 0.
print("Primer elemento de la lista:", ejemploLista[0])

#Acceder al último elemento de la lista. se puede acceder al último elemento de la lista utilizando el índice -1.
print("Ultimo elemento de la lista:", ejemploLista[-1])


#Como añadir elementos a una lista?
#Para añadir elementos a una lista, se puede utilizar el método append() 

ejemploLista.append(6)

otroEjemplo.append("f")

print("Lista después de añadir un elemento:", ejemploLista)
print("Lista después de añadir un elemento:", otroEjemplo)

#También se puede anidar listas 

#nuevaLista = ejemploLista + otroEjemplo
#print("Lista después de añadir una lista:", nuevaLista)

#Modificar elementos de una lista

ejemploLista[0] = 11
print("Lista después de modificar un elemento:", ejemploLista)

#Eliminar elementos de una lista
#Tenemos algunas sentencias para eliminar elementos de una lista:
#del(), remove(), pop()

#El método del() elimina un elemento de la lista en una posición específica.
del ejemploLista[0]
print("Lista después de eliminar un elemento:", ejemploLista)

#El método remove() elimina el primer elemento de la lista que coincide con el valor especificado.
ejemploLista.remove(2)
print("Lista después de eliminar un elemento:", ejemploLista)

#Si uso pop, y no especifico, elimina el último elemento de la lista.
ejemploLista.pop()
print("Lista después de eliminar un elemento:", ejemploLista)

#Otro ejemplo de pop, especificando la posición
ejemploLista.pop(2)
print("Lista después de eliminar un elemento:", ejemploLista)