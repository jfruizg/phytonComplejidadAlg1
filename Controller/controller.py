from View import Vista
from Model import Model
import random

unaLista = []
for i in range(0,4000):
    unaLista.append(random.randrange(30))

Vista.mostrarDatos(unaLista)
Model.ordenamientoBurbuja(unaLista)
Vista.mostrarDatos(unaLista)