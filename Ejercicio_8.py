#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     03/09/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    lista=[7,99,25,2,7,607,3,4]
    numeroMin=lista[0]
    for numeroActual in lista:
        if numeroActual<numeroMin:
            numeroMin=numeroActual
    print(f"El menor numero de la lista es: {numeroMin}")

if __name__ == '__main__':
    main()
