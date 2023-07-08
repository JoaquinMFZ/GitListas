# Método append(): Agrega un elemento al final de la lista
def agregar_elemento(lista, elemento):
    lista.append(elemento)

# Método remove(): Elimina la primera aparición de un elemento en la lista
def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)

# Método sort(): Ordena la lista de forma ascendente
def ordenar_lista(lista):
    lista.sort()

# Método reverse(): Invierte el orden de los elementos en la lista
def invertir_lista(lista):
    lista.reverse()

# Método extend(): Une dos listas
def unir_listas(lista1, lista2):
    lista1.extend(lista2)

# Ingresar los valores de la lista
valores = input("Ingrese los valores de la lista separados por comas: ")
lista = valores.split(',')

# Convierte los elementos de la lista a enteros
lista = [int(elemento) for elemento in lista]

# Ejemplo de su uso
print("Lista original:", lista)

nuevo_elemento = int(input("Ingrese un elemento para agregar a la lista: "))
agregar_elemento(lista, nuevo_elemento)
print("Después de agregar un elemento:", lista)

elemento_eliminar = int(input("Ingrese un elemento para eliminar de la lista: "))
eliminar_elemento(lista, elemento_eliminar)
print("Después de eliminar un elemento:", lista)

ordenar_lista(lista)
print("Después de ordenar la lista:", lista)

invertir_lista(lista)
print("Después de invertir la lista:", lista)

otra_lista_valores = input("Ingrese los valores de otra lista separados por comas: ")
otra_lista = otra_lista_valores.split(',')
otra_lista = [int(elemento) for elemento in otra_lista]

unir_listas(lista, otra_lista)
print("Después de unir dos listas:", lista)