from View import Vista
from Model import Model
import random


class Controller:

    Vista = Vista
    Model = Model

    Vista.mostrarDatos(
        "Bienvenido al oirdenamiento full" + "\n" + "Ordenamiento burbuja -> [1]" + "\n"
        + "Ordenamiento por Seleccion -> [2]")
    datoMenu = Vista.recibirDatos("")

    if(datoMenu == 1):
        Vista.mostrarDatos("Ordenamiento Burbuja")
        Vista.mostrarDatos("Datos aleatorios -> [1]"+"\n"+"Datos ingresados por ususario -> [2]")
        datoMenuBurbuja=Vista.recibirDatos("")
        listaNumero = []
        if(datoMenuBurbuja == 1):
            cantidadDatos = Vista.recibirDatos("Escribir el dato *N* o la cantidad de datos a organizar"+"\n")
            for i in range(0,cantidadDatos):
                listaNumero.append(random.randrange(0,cantidadDatos))
            Model.modelo.ordenamientoBurbuja(listaNumero)
            Vista.mostrarDatos(listaNumero)
        else:
            catidadDatos = Vista.recibirDatos("Escribir el dato *N* o la cantidad de datos a organizar"+"\n")
            for i in range(0,catidadDatos):
                num = Vista.recibirDatos("Dato ("+str(i+1)+") = ")
                listaNumero.append(num)
            Model.modelo.ordenamientoBurbuja(listaNumero)
            Vista.mostrarDatos(listaNumero)

    elif(datoMenu == 2):
        Vista.mostrarDatos("Ordenamiento Seleccion")
        Vista.mostrarDatos("Datos aleatorios -> [1]" + "\n" + "Datos ingresados por ususario -> [2]")
        datoMenuSeleccion = Vista.recibirDatos("")
        listaNumero = []
        if (datoMenuSeleccion == 1):
            cantidadDatos = Vista.recibirDatos("Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
            for i in range(0, cantidadDatos):
                listaNumero.append(random.randrange(0, cantidadDatos))
            Model.modelo.ordenamientoSeleccion(listaNumero)
            Vista.mostrarDatos(listaNumero)
        else:
            catidadDatos = Vista.recibirDatos("Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
            for i in range(0, catidadDatos):
                num = Vista.recibirDatos("Dato (" + str(i + 1) + ") = ")
                listaNumero.append(num)
            Model.modelo.ordenamientoSeleccion(listaNumero)
            Vista.mostrarDatos(listaNumero)
    elif (datoMenu == 3):
        Vista.mostrarDatos("Ordenamiento Radix")
        Vista.mostrarDatos("Datos aleatorios -> [1]" + "\n" + "Datos ingresados por ususario -> [2]")
        datoMenuRadix = Vista.recibirDatos("")
        listaNumero = []
        if (datoMenuRadix == 1):
            cantidadDatos = Vista.recibirDatos("Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
            for i in range(0, cantidadDatos):
                listaNumero.append(random.randrange(0, cantidadDatos))
            Model.modelo.ordenamientoSeleccion(listaNumero)
            Vista.mostrarDatos(listaNumero)
        else:
            catidadDatos = Vista.recibirDatos("Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
            for i in range(0, catidadDatos):
                num = Vista.recibirDatos("Dato (" + str(i + 1) + ") = ")
                listaNumero.append(num)
            Model.modelo.ordenamientoSeleccion(listaNumero)
            Vista.mostrarDatos(listaNumero)





