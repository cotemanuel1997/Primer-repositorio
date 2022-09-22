#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     17/09/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    def sucursales():
        # Inicio
        # Declaración de variables
        regsuc=[]
        datos=[]
        datossuc=[]
        regdatossuc=[]
        sucursales=[]
        acumcan=0
        acumven=0
        acumtot=0
        promedio=0
        contador=0
        # Ingreso de datos en matriz
        while True:
            numsuc=int(input("Ingrese numero de sucursal: "))
            if numsuc == 0:
                break
            canven=int(input("Ingrese cantidad de ventas de la sucursal: "))
            totven=int(input("Ingrese total de ventas de la sucursal: "))
            datos.append(numsuc)
            datos.append(canven)
            datos.append(totven)
            regsuc.append(datos)
            datos=[]
            regsuc.sort()
        # Matriz regsuc ordenada por numero de sucursal
        auxsuc=regsuc[contador][0]
        while contador<len(regsuc):
            suc=regsuc[contador][0]
            can=regsuc[contador][1]
            tot=regsuc[contador][2]     
            if auxsuc==suc:
                # Control
                acumcan=acumcan+can
                acumven=acumven+tot
                # Salto de registro de matriz regsuc
                contador=contador+1
            else:
                # Corte de control por sucursal
                if acumcan!=0:
                    promedio=acumven/acumcan
                acumtot=acumtot+acumven
                sucursales.append(auxsuc)
                datossuc.append(auxsuc)
                datossuc.append(acumcan)
                datossuc.append(acumven)
                datossuc.append(promedio)
                regdatossuc.append(datossuc)
                datossuc=[]
                acumcan=0
                acumven=0
                promedio=0
                auxsuc=suc
        # Fin de archivo
        # Corte de control por sucursal
        if acumcan!=0:
            promedio=acumven/acumcan
        acumtot=acumtot+acumven
        sucursales.append(auxsuc)
        datossuc.append(auxsuc)
        datossuc.append(acumcan)
        datossuc.append(acumven)
        datossuc.append(promedio)
        regdatossuc.append(datossuc)
        datossuc=[]
        acumcan=0
        acumven=0
        promedio=0
        auxsuc=suc
        # Totales
        print(f"Matriz de datos ingresados ordenada por sucursal: {regsuc}")
        print(f"Matriz de acumuladores y promedios de cada sucursal: {regdatossuc}")
        print(f"Las sucursales ingresadas son: {sucursales}")
        print("                      DATOS INGRESADOS")
        print("Sucursal || Cantidad de ventas  || Total de ventas || Promedio de ventas")
        for i in range(len(regdatossuc)):
            print(f"    {regdatossuc[i][0]}                  {regdatossuc[i][1]}                 \
{regdatossuc[i][2]}               {regdatossuc[i][3]}")
        print(f"El total de ventas de toda la cadena es: {acumtot}")
    print(sucursales())

if __name__ == '__main__':
    main()
