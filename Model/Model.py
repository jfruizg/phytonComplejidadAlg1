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

    def ordenamientoRadix(listaDatos):
        n = 0;
        for e in listaDatos:
            if len(e) > n:
                n = len(e)

        for i in range(0, len(listaDatos)):
            while len(listaDatos[i]) < n:
                listaDatos[i] = "0" + listaDatos[i]

        for j in range(n, -1, -1, -1):
            grupos = [[]for i in range(10)]

            for i in range(len(listaDatos)):
                grupos[int(lista[i][j])].append(lista[i])

            lista = []
            for g in grupos:
                lista += g
        return [int(i) for i in lista]
