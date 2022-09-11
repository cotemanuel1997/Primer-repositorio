#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     11/09/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lista1=[3,9,5,7,1,13,51,6,12,4,2,8]
    def separar(lista):
        listaPares=[]
        listaImpares=[]
        for i in lista:
            if i % 2 == 0:
                listaPares.append(i)
            else:
                listaImpares.append(i)
        listaPares.sort()
        listaImpares.sort()
        return listaPares,listaImpares

    listaPares,listaImpares=separar(lista1)
    print(f"Lista de numeros pares: {listaPares}")
    print(f"Lista de numeros impares: {listaImpares}")



if __name__ == '__main__':
    main()
