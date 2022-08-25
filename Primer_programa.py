#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     25/08/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
     numero1=3
     numero2=4
     print(numero1+numero2)
     # Suma de los numeros enteros 3 y 4 y además se muestra el resultado por pantalla
     string1="Hola "
     string2="mundo"
     print(string1+string2)
     '''
     Se muestra por pantalla la concatenación de las variables
     string1 y string2, cuyos valores son las cadenas de texto "Hola" y "mundo"
     respectivamente
     '''
     nombre=input("Ingrese su nombre")
     dni=input("Ingrese su dni")
     print("El nombre del usuario es " + nombre + " y su DNI es " + dni)
     '''
     i- Se solicita que el usuario ingrese su nombre, que se guarda en
        la variable 'nombre'.
     ii- Luego se solicita que ingrese su DNI, que se guarda en la
        variable 'dni'.
     iii- Por último se muestra por pantalla un mensaje indicando el nombre
        y el DNI ingresado por el usuario.
     '''
if __name__ == '__main__':
    main()
