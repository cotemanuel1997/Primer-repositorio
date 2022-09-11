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
    def recortar(numRecortar, limInf, limSup):
        if numRecortar<limInf:
            return limInf
        elif numRecortar>limSup:
            return limSup
        else:
            return numRecortar
    print("Limite inferior: " + str(recortar(2,5,10)))
    print("Limite superior: " + str(recortar(12,5,10)))
    print("No supera los limites: " + str(recortar(8,5,10)))


if __name__ == '__main__':
    main()
