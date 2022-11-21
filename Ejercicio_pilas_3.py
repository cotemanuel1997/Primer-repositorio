#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     09/11/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    # Ejercicio 3

    # Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como
    # estructura extra.


    class nodoPila(object) :
        """Clase nodo pila"""
        info, sig = None, None

    class Pila(object) :
        """Clase Pila"""
        def __init__(self) :
            self.cima = None
            self.tamanio = 0

        def apilar(self, dato) :
            """Apila el elemento sobre la cima de la pila"""
            nodo = nodoPila()
            nodo.info = dato
            nodo.sig = self.cima

            self.cima = nodo
            self.tamanio += 1

        def desapilar(self) :
            """Desapila el elemento de la cima de la pila y lo devuelve"""
            x = self.cima.info
            self.cima = self.cima.sig
            self.tamanio -= 1

            return x

        def pila_vacia(self) :
            """Devuelve true si la pila está vacía"""
            return self.cima is None

        def en_cima(self) :
            """Devuelve el valor almacenado en la cima de la pila"""
            if self.cima is not None :
                return self.cima.info
            else :
                return None

        def tamanio(self) :
            """Devuelve el nro de elementos en la pila"""
            return self.tamanio

    pila = Pila()
    elementos = [5,7,6,8,2,4,3,4,9,4,2,4,9,6,1,3,4,9,4,1,3,8,7,6,1,4,3,5,5,6,8,4,5,4,6]

    # ingreso los elementos a la pila

    for nro in elementos :
        pila.apilar(nro)
        print(pila.cima.info)
    print("\n")
    
    # creo una segunda pila e ingreso los elementos en la segunda pila"

    pila2=Pila()
    for nro in elementos :
        pila2.apilar(nro)

    # vacio la primera pila y apilo los elemntos de la segunda en esta, quedando invertido el contenido
    # de la primera

    while(not pila.pila_vacia()):
        x= pila.desapilar()

    while(not pila2.pila_vacia()):
        x= pila2.desapilar()
        pila.apilar(x)
        print(pila.cima.info)
if __name__ == '__main__':
    main()