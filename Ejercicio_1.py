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
    numero=int(input("ingrese numero impar: "))
    while numero%2==0:
        numero=int(input("ingrese numero impar: "))
    print("El numero es impar")
if __name__ == '__main__':
    main()
