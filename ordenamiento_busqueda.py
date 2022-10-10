#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     08/10/2022
# Copyright:   (c) HP 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import random
import time

tiempos = []
cant_comp = []

def rango_numeros(num_max):
    lista = []
    for i in range(0, num_max):
        lista.append(random.randint(0, num_max))
    return lista

numero = rango_numeros(1000)

bur = {'comparaciones' : 0, 'tiempo':0}


def burbuja(lista):
    inicio = time.time()
    for i in range(0,len(lista) -1):
        for j in range(0,len(lista)-i-1):
            bur['comparaciones'] += 1
            if(lista[j]) > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    fin = time.time()
    bur['tiempo'] = fin - inicio
    tiempos.append(bur['tiempo'])
    cant_comp.append(bur['comparaciones'])
    print("TIEMPO Método BURBUJA: ", bur['tiempo'])
    print("COMPARACIONES Método BURBUJA: ", bur['comparaciones'])
    return bur

resultado = burbuja([i for i in numero])


sel = {'comparaciones' : 0, 'tiempo':0}


def seleccion(lista):
    inicio = time.time()
    for i in range(0, len(lista)-1):
        sel['comparaciones'] += 1
        minimo= i
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[minimo]):
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
        fin = time.time()
    sel['tiempo'] = fin - inicio
    tiempos.append(sel['tiempo'])
    cant_comp.append(sel['comparaciones'])
    print("TIEMPO Método SELECCIÓN: ", sel['tiempo'])
    print("COMPARACIONES Método SELECCIÓN: ", sel['comparaciones'])
    return sel

resultado = seleccion([i for i in numero])

ins = {'comparaciones' : 0, 'tiempo':0}

def insercion(lista):
    inicio = time.time()
    for i in range(1, len(lista)+1):
        ins['comparaciones'] += 1
        k=i-1
        while (k > 0) and (lista[k] < lista[k-1]):
            ins['comparaciones'] += 1
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1
            fin = time.time()
    ins['tiempo'] = fin - inicio
    tiempos.append(ins['tiempo'])
    cant_comp.append(ins['comparaciones'])
    print("TIEMPO Método INSERCIÓN: ", ins['tiempo'])
    print("COMPARACIONES Método INSERCIÓN: ", ins['comparaciones'])
    return ins

resultado = insercion([i for i in numero])

qui = {'comparaciones' : 0, 'tiempo':0}


def quicksort(lista, primero, ultimo) :
    inicio = time.time()
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo

    while (izquierda < derecha) :
        qui['comparaciones'] += 1
        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha) :
            izquierda += 1

        qui['comparaciones'] += 1
        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda) :
            derecha -= 1

        qui['comparaciones'] += 1
        if (izquierda < derecha) :
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    qui['comparaciones'] += 1
    if (lista[pivote] < lista[izquierda]) :
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

    qui['comparaciones'] += 1
    if (primero < izquierda) :
        return quicksort(lista, primero, izquierda-1)

    qui['comparaciones'] += 1
    if (ultimo > izquierda) :
        return quicksort(lista, izquierda+1, ultimo)

    qui['tiempo'] = fin - inicio
    tiempos.append(qui['tiempo'])
    cant_comp.append(qui['comparaciones'])
    print("TIEMPO Método QUICKSORT: ", qui['tiempo'])
    print("COMPARACIONES Método QUICKSORT: ", qui['comparaciones'])
    return lista

resultado = quicksort([i for i in numero], 0, len(numero)-1)



print(tiempos)
print(cant_comp)



if __name__ == '__main__':
    main()
