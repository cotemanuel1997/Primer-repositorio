#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     10/09/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    def relacion(num1,num2):
        if num1>num2:
            return 1
        elif num1<num2:
            return -1
        else:
            return 0
    print(relacion(4,2))
    print(relacion(2,4))
    print(relacion(2,2))

if __name__ == '__main__':
    main()
