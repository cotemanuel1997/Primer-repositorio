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
    numero1=int(input("ingrese primer numero: "))
    numero2=int(input("ingrese segundo numero: "))
    while True:
        opcion=input("ingrese una opción: sumar, restar o multiplicar")
        if opcion=="sumar":
            print("la suma es: " + str(numero1+numero2))
            break
        if opcion=="restar":
            print("la resta es: " + str(numero1-numero2))
            break
        if opcion=="multiplicar":
            print("la multiplicación es: " + str(numero1*numero2))
            break
if __name__ == '__main__':
    main()
