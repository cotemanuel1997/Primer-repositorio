#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     02/09/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lista=[7,99,25,2,7,607,3,4]
    numeroMax=lista[0]
    for numeroActual in lista:
        if numeroActual>numeroMax:
            numeroMax=numeroActual
    print(f"El mayor numero de la lista es: {numeroMax}")




if __name__ == '__main__':
    main()
