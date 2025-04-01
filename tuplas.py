#Tuplas

#Escritas con paréntesis y separadas por comas. Distintos tipos de datos

#tupla = (1, 2, 3, 4, 5, "Hola", True, 3.14)

#Si quiero crear una tupla con un único valor, debo poner una coma al final

#tuplaValorUnico = (1,)

#For in para iteración de tuplas

notas = (10, 8, 9, 7, 6, 5)

for nota in notas:
    print(nota)

#porque pasar de tupla a lista? => para poder modificarla => TUPLAS SON INMUTABLES 

#cambiar de tupla a lista
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
print(lista)

#Desempaquetado
persona = ("Franco", 23, "Argentina")
nombre, edad, pais = persona
print("nombre: ",nombre, ". Edad: ", edad, "Pais: ", pais)


#Y SI TENGO LISTA DENTRO DE TUPLAS? Ejemplo nomnbre de alumnos y notas

#Comparación de tuplas
# por ejemplo si quiero comparar dos alumnos por su nota
alumno1 = ("Juan", 10)
alumno2 = ("Pedro", 9)
alumno3 = ("Maria", 10)
alumno4 = ("Ana", 8)

#alumno1>alumno2 => True
#alumno1<alumno4 => False

#alumno1==alumno3 => True   

#fechas en tuplas
fecha = (2023, 10, 5) # año, mes, dia

#tablas

personas = [("Juan", 23), ("Pedro", 25), ("Maria", 22), ("Ana", 24)]

for nombre, edad in personas:
    print("Nombre: ", nombre, "Edad: ", edad)
