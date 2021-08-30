class modelo:

    def ordenamientoBurbuja(unaLista):

        for numPasada in range(len(unaLista) - 1, 0, -1):
            for i in range(numPasada):
                if unaLista[i] > unaLista[i + 1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i + 1]
                    unaLista[i + 1] = temp

    def ordenamientoSeleccion(listaDatos):

        for i in range(len(listaDatos)):
            minimo = i
            for j in range(i, len(listaDatos)):
                if (listaDatos[j] < listaDatos[minimo]):
                    minimo = j
            if (minimo != i):
                aux = listaDatos[i]
                listaDatos[i] = listaDatos[minimo]
                listaDatos[minimo] = aux


