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
    email=input("Ingrese un email: ")
    if email.find("@")==-1:
        print("No es un email")
    else:
        print("Es un email")
if __name__ == '__main__':
    main()
