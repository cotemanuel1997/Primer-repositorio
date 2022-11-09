#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     19/10/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():

    #   a) Generar una lista de elementos aleatorios de distintos tamaños (100.000,
    #   1.000.000, 10.000.000)
    #   b) Medir y mostrar su tiempo de ejecución
    #   c) Medir y mostrar la cantidad de comparaciones realizadas
    #   d) Deberá indicar nombre y tiempo del método más rápido
    #   e) Deberá indicar nombre y cantidad del método que realiza menos comparaciones


    #   a) Generar una lista de elementos aleatorios de distintos tamaños (100.000,
    #   1.000.000, 10.000.000)

    import random

    lista_mil=[]
    lista_diez_mil=[]


    def listas():
        
        for i in range(0,1000):
            lista_mil.append(random.randint(0, 100))

        for i in range(0,10000):
            lista_diez_mil.append(random.randint(0, 100))

    import time

    def burbuja(lista) :
    #"""Método de ordenamiento burbuja"""
        contadorBurbuja=0
        for i in range(0, len(lista)-1) :
            for j in range(0, len(lista)-i-1) :
                if (lista[j] > lista[j+1]) :
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    contadorBurbuja+=1
        return contadorBurbuja

        #print("Burbuja comparaciones realizadas : ", contadorBurbuja)
        

    def seleccion(lista) :
    #"""Método de ordenamiento selección"""
        contadorSeleccion=0
        for i in range(0, len(lista)-1) :
            minimo = i
            for j in range(i+1, len(lista)) :
                if (lista[j] < lista[minimo]) :
                    minimo = j
                    contadorSeleccion+=1
            lista[i], lista[minimo] = lista[minimo], lista[i]
        return contadorSeleccion
        

    def insercion(lista) :
    #""Método de ordenamiento inserción"""

        contadorInsercion=0

        for i in range(1, len(lista)+1) :
            k = i-1
            while (k > 0) and (lista[k] < lista[k-1]) :
                lista[k], lista[k-1] = lista[k-1], lista[k]
                k -= 1
                contadorInsercion+=1
        return contadorInsercion


    def merge(izquierda, derecha) :
        #"""Funcion para mezclar listas"""

        lista_mezclada = []

        while (len(izquierda) > 0) and (len(derecha) > 0) :
            if (izquierda[0] < derecha[0]) :
                lista_mezclada.append(izquierda.pop(0))
            else :
                lista_mezclada.append(derecha.pop(0))

        if (len(izquierda) > 0) :
            lista_mezclada += izquierda

        if (len(derecha) > 0) :
            lista_mezclada += derecha

        return lista_mezclada

        

    def mergesort(lista) :
    #"""Metodo de ordenamiento mergesort"""
        global contador_mergesort
        contador_mergesort=0
        if (len(lista) <= 1) :
            return lista
        else :
            medio = len(lista) // 2
            izquierda = []

            for i in range(0, medio) :
                izquierda.append(lista[i])

            derecha = []

            for i in range(medio, len(lista)) :
                derecha.append(lista[i])

            izquierda= mergesort(izquierda)
            derecha = mergesort(derecha)

            if (izquierda[medio-1] <= derecha[0]) :
                izquierda += derecha
                contador_mergesort+=1

                return izquierda

            resultado = merge(izquierda, derecha)

            return resultado

       


    #   b) Medir y mostrar su tiempo de ejecución

    #   c) Medir y mostrar la cantidad de comparaciones realizadas

    # Tiempo de ejecucion del metodo burbuja con una lista de mil elementos

    listas()


    inicio=time.time()

    contadorBurbuja=burbuja(lista_mil)


    fin=time.time()

    tiempo_burbuja = fin - inicio

    print("Tiempo de burbuja con mil elementos: ", tiempo_burbuja )

    # cantidad de comparaciones realizadas en burbuja

    print("Burbuja comparaciones realizadas : ", contadorBurbuja)

    print('\n')

    lista_mil=[]

    # Tiempo de ejecucion del metodo seleccion con una lista de mil elementos

    listas()


    inicio=time.time()

    contadorSeleccion = seleccion(lista_mil)

    fin=time.time()

    tiempo_seleccion = fin - inicio

    print("Tiempo de seleccion con mil elementos: ", tiempo_seleccion )

    # cantidad de comparaciones realizadas en seleccion

    print("Seleccion comparaciones realizadas : ", contadorSeleccion)
    print('\n')
   
    lista_mil=[]

    # Tiempo de ejecucion del metodo insercion con una lista de mil elementos

    listas()


    inicio=time.time()

    contadorInsercion = insercion(lista_mil)

    fin=time.time()

    tiempo_insercion = fin - inicio

    print("Tiempo de insercion con mil elementos: ", tiempo_insercion )

    # cantidad de comparaciones realizadas en insercion

    print("insercion comparaciones realizadas : ", contadorInsercion)  

    print('\n')


    lista_mil=[]

    # Tiempo de ejecucion del metodo mergesort con una lista de mil elementos

    listas()


    inicio=time.time()

    mergesort(lista_mil)

    print("mergesort comparaciones realizadas con mil elementos: ", contador_mergesort)

    fin=time.time()

    tiempo_mergesort_mil_elementos = fin - inicio

    print("Tiempo de mergesort con mil elementos: ", tiempo_mergesort_mil_elementos )

    print("\n")

    lista_mil=[]

    # Tiempo de ejecucion del metodo mergesort con una lista de diez mil elementos

    listas()


    inicio=time.time()

    mergesort(lista_diez_mil)

    print("mergesort comparaciones realizadas con diez mil elementos: ", contador_mergesort)

    fin=time.time()

    tiempo_mergesort_diez_mil_elementos = fin - inicio

    print("Tiempo de mergesort con diez mil elementos: ", tiempo_mergesort_diez_mil_elementos )

    print("\n")

    lista_diez_mil=[]

    #   d) Deberá indicar nombre y tiempo del método más rápido

    tiempos = {

        tiempo_burbuja:"Metodo burbuja",
        tiempo_seleccion:"Metodo seleccion",
        tiempo_insercion:"Metodo insercion",
        tiempo_mergesort_mil_elementos:"Metodo mergesort",

    }    

    registro_tiempos = [

        tiempo_burbuja,
        tiempo_seleccion,
        tiempo_insercion,
        tiempo_mergesort_mil_elementos

    ]

    minimo=registro_tiempos[0]
    for i in range(0,len(registro_tiempos)):
        if registro_tiempos[i] < minimo:
            minimo=registro_tiempos[i]
    print(f"El metodo más rápido es: {tiempos[minimo]}")

    print("\n")

    #   e) Deberá indicar nombre y cantidad del método que realiza menos comparaciones

    comparaciones = {

        contadorBurbuja:"Metodo burbuja",
        contadorSeleccion:"Metodo seleccion",
        contadorInsercion:"Metodo insercion",
        contador_mergesort:"Metodo mergesort",

    }

    registro_comparaciones = [

        contadorBurbuja,
        contadorSeleccion,
        contadorInsercion,
        contador_mergesort

    ]

    minimo=registro_comparaciones[0]
    for i in range(0,len(registro_comparaciones)):
       if registro_comparaciones[i] < minimo:
            minimo=registro_comparaciones[i]
    print(f"El metodo que realiza menos comparaciones es: {comparaciones[minimo]}")


if __name__ == '__main__':
    main()
