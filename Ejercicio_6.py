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
    lista=[2,4,3]
    contador=0
    suma=0
    for elemento in lista:
        suma=suma+elemento
        contador=contador+1
    promedio=suma/contador
    print(f"El promedio es: {promedio}")
if __name__ == '__main__':
    main()
