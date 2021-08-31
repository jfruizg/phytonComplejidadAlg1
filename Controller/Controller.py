from View import Vista
from Model import Model
import random


class Controller:
    Vista = Vista
    Model = Model

    CONS = 1
    listaNumero = []
    while CONS == 1:

        Vista.vista.mostrarDatos(
            "Bienvenido al oirdenamiento full" + "\n" + "Ordenamiento burbuja -> [1]" + "\n"
            + "Ordenamiento por Seleccion -> [2]" + "\n" + "Ordenamiento Radix -> [3]" +"\n" +"Ordenamiento QuickSort -> [4]" + "\n"+"Ordenamiento por MergeSort -> [5]")
        datoMenu = Vista.vista.recibirDatos("")

        if (datoMenu == 1):
            Vista.vista.mostrarDatos("Ordenamiento Burbuja")
            Vista.vista.mostrarDatos("Datos aleatorios -> [1]" + "\n" + "Datos ingresados por ususario -> [2]")
            datoMenuBurbuja = Vista.vista.recibirDatos("")
            if (datoMenuBurbuja == 1):
                cantidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, cantidadDatos):
                    listaNumero.append(random.randrange(0, cantidadDatos))
                Model.modelo.ordenamientoBurbuja(listaNumero)
                Vista.vista.mostrarDatos(listaNumero)
                listaNumero.clear()
            else:
                catidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, catidadDatos):
                    num = Vista.vista.recibirDatos("Dato (" + str(i + 1) + ") = ")
                    listaNumero.append(num)
                Model.modelo.ordenamientoBurbuja(listaNumero)
                Vista.vista.mostrarDatos(listaNumero)
                listaNumero.clear()
        elif (datoMenu == 2):
            Vista.vista.mostrarDatos("Ordenamiento Seleccion")
            Vista.vista.mostrarDatos("Datos aleatorios -> [1]" + "\n" + "Datos ingresados por ususario -> [2]")
            datoMenuSeleccion = Vista.vista.recibirDatos("")
            if (datoMenuSeleccion == 1):
                cantidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, cantidadDatos):
                    listaNumero.append(random.randrange(0, cantidadDatos))
                Model.modelo.ordenamientoSeleccion(listaNumero)
                Vista.vista.mostrarDatos(listaNumero)
                listaNumero.clear()
            else:
                catidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, catidadDatos):
                    num = Vista.vista.recibirDatos("Dato (" + str(i + 1) + ") = ")
                    listaNumero.append(num)
                Model.modelo.ordenamientoSeleccion(listaNumero)
                Vista.vista.mostrarDatos(listaNumero)
                listaNumero.clear()
        elif (datoMenu == 3):
            Vista.vista.mostrarDatos("Ordenamiento Radix")
            Vista.vista.mostrarDatos("Datos aleatorios -> [1]" + "\n" + "Datos ingresados por ususario -> [2]")
            datoMenuRadix = Vista.vista.recibirDatos("")
            if (datoMenuRadix == 1):
                cantidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, cantidadDatos):
                    listaNumero.append(random.randrange(0, cantidadDatos))
                print(Model.modelo.radixSort(listaNumero))
                listaNumero.clear()
            else:
                catidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, catidadDatos):
                    num = Vista.vista.recibirDatos("Dato (" + str(i + 1) + ") = ")
                    listaNumero.append(num)
                (Model.modelo.ordenamientoRadix(listaNumero))
                print(listaNumero)
        elif (datoMenu == 4):
            Vista.vista.mostrarDatos("Ordenamiento Quicksort")
            Vista.vista.mostrarDatos("Datos aleatorios -> [1]" + "\n" + "Datos ingresados por ususario -> [2]")
            datoMenuQuick = Vista.vista.recibirDatos("")
            if (datoMenuQuick == 1):
                cantidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, cantidadDatos):
                    listaNumero.append(random.randrange(0, cantidadDatos))
                print(Model.ordenamientoSort(listaNumero))
                listaNumero.clear()
            else:
                catidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, catidadDatos):
                    num = Vista.vista.recibirDatos("Dato (" + str(i + 1) + ") = ")
                    listaNumero.append(num)
                (Model.modelo.ordenamientoRadix(listaNumero))
                print(Model.ordenamientoSort(listaNumero))
                listaNumero.clear()


        elif (datoMenu == 5):
            Vista.vista.mostrarDatos("Ordenamiento MergeSort")
            Vista.vista.mostrarDatos("Datos aleatorios -> [1]" + "\n" + "Datos ingresados por ususario -> [2]")
            datoMenuMerge = Vista.vista.recibirDatos("")
            if (datoMenuMerge == 1):
                cantidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, cantidadDatos):
                    listaNumero.append(random.randrange(0, cantidadDatos))
                merge = Model.ordenamientoMerge(listaNumero)
                Vista.vista.mostrarDatos(merge)
                listaNumero.clear()

            else:
                catidadDatos = Vista.vista.recibirDatos(
                    "Escribir el dato *N* o la cantidad de datos a organizar" + "\n")
                for i in range(0, catidadDatos):
                    num = Vista.vista.recibirDatos("Dato (" + str(i + 1) + ") = ")
                    listaNumero.append(num)
                merge = Model.ordenamientoMerge(listaNumero)
                Vista.vista.mostrarDatos(merge)
                listaNumero.clear()

        CONS = int(input("Desea volver al menu -> [1]" + "\n" + "Desea finalizar el programa -> [2]" + "\n"))
