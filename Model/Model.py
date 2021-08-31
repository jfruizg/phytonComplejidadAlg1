
from heapq import merge
from math import sin  # para usar la función seno

import time


class modelo:

    def ordenamientoBurbuja(unaLista):
        inicio = time.time()
        for numPasada in range(len(unaLista) - 1, 0, -1):
            for i in range(numPasada):
                if unaLista[i] > unaLista[i + 1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i + 1]
                    unaLista[i + 1] = temp
        fin = time.time()
        return fin-inicio

    def ordenamientoSeleccion(listaDatos):
        inicio = time.time()
        for i in range(len(listaDatos)):
            minimo = i
            for j in range(i, len(listaDatos)):
                if (listaDatos[j] < listaDatos[minimo]):
                    minimo = j
            if (minimo != i):
                aux = listaDatos[i]
                listaDatos[i] = listaDatos[minimo]
                listaDatos[minimo] = aux
        fin = time.time()
        return  fin-inicio



    def countingSortForRadix(inputArray, placeValue):
        countArray = [0] * 10
        inputSize = len(inputArray)

        for i in range(inputSize):
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] += 1

        for i in range(1, 10):
            countArray[i] += countArray[i - 1]

        # Reconstructing the output array
        outputArray = [0] * inputSize
        i = inputSize - 1
        while i >= 0:
            currentEl = inputArray[i]
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] -= 1
            newPosition = countArray[placeElement]
            outputArray[newPosition] = currentEl
            i -= 1
        return outputArray

    def radixSort(listaDato):
        inicio = time.time()
        maxEl = max(listaDato)
        D = 1
        while maxEl > 0:
            maxEl /= 10
            D += 1
        placeVal = 1
        outputArray = listaDato
        while D > 0:
            outputArray = modelo.countingSortForRadix(outputArray, placeVal)
            placeVal *= 10
            D -= 1
        fin = time.time()
        devolver = fin-inicio
        return devolver

    def quicksort(lista):
        inicio = time.time()
        izquierda = []
        centro = []
        derecha = []
        if len(lista) > 1:
            pivote = lista[0]
            for i in lista:
                if i < pivote:
                    izquierda.append(i)
                elif i == pivote:
                    centro.append(i)
                elif i > pivote:
                    derecha.append(i)
            fin = time.time()
            return fin-inicio
        else:
            return lista




    def ordenamientoMerge(lista):
        if len(lista) < 2:
            return lista
        else:
            middle = len(lista) // 2
            right = modelo.ordenamientoMerge(lista[:middle])
            left = modelo.ordenamientoMerge(lista[middle:])
            return merge(right, left)

    def merge(lista1, lista2):
        i, j = 0, 0
        result = []

        while (i < len(lista1) and j < len(lista2)):
            if (lista1[i] < lista2[j]):
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1

        result += lista1[i:]
        result += lista2[j:]

        return result




