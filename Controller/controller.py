from View import Vista
from Model import Model
import random

rango = 4000
unaLista = []
for i in range(0,rango):
    unaLista.append(random.randrange(rango))

Model.ordenamientoBurbuja(unaLista)
Vista.mostrarDatos(unaLista)