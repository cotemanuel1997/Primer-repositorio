#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      gmoya
#
# Created:     04/10/2022
# Copyright:   (c) gmoya 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():
    # opción El Principito
    principito = 5
    datos = {
        "libros": [ "Don Quijote", "Historia de dos ciudades", "El Señor de los Anillos", "Harry Potter y la piedra filosofal", "El principito" ],
        "sucursales": [ "Almagro", "Belgrano", "Caballito", "Palermo", "Villa Crespo" ],
        "total": 0,
        "registros": []
    }

    # Se ingresará un registro por sucursal
    # y cada sucursal tendrá un producto distinto
    solicitarDatos(datos)


    ##    1. ¿Cuantas ventas de "El principito" se hicieron en cada sucursal?
    for reg in datos["registros"] :
        if (reg['nro_producto'] == principito) :
            print(f'{datos["sucursales"][reg["nro_sucursal"]-1]}: Se vendieron {reg["ventas"]} copias de El Principito')
        else :
            print(f'{datos["sucursales"][reg["nro_sucursal"]-1]}: Se vendieron 0 copias de El Principito')
    print('\n')


    ##    2. ¿Qué producto se vendió más en toda la cadena?
    ##    3. ¿Qué producto se vendió menos en toda la cadena?
    maximo = datos["registros"][0]
    minimo = datos["registros"][0]
    for i in range(0, len(datos["registros"])) :
        if (maximo['ventas'] < datos['registros'][i]['ventas']) :
            maximo = datos["registros"][i]

        if (minimo['ventas'] > datos['registros'][i]['ventas']) :
            minimo = datos["registros"][i]

    print(f'{datos["libros"][minimo["nro_producto"]-1]}: Se vendieron {minimo["ventas"]} copias')
    print(f'{datos["libros"][maximo["nro_producto"]-1]}: Se vendieron {maximo["ventas"]} copias')
    print('\n')


    ##    4. ¿Qué porcentaje representa el total de cada producto sobre el total de ventas
    ##    de la cadena?
    for i in datos["registros"]:
        print(f"El producto {datos['libros'][i['nro_producto']-1]} representa un {i['ventas']*100/datos['total']} % sobre el total de ventas")
    print('\n')

    ##    5. Ordene de mayor a menor las sucursales según la cantidad de ventas
    for i in range(0, len(datos['registros'])-1) :
        for j in range(0, len(datos['registros'])-i-1) :
            if (datos['registros'][j]['ventas'] < datos['registros'][j+1]['ventas']) :
                datos['registros'][j], datos['registros'][j+1] = datos['registros'][j+1], datos['registros'][j]

    for reg in datos['registros'] :
        print(f'{datos["sucursales"][reg["nro_sucursal"]-1]}: {reg["ventas"]} ventas')


def solicitarDatos(datos) :
    nro_registro = int(input("Ingrese Nro. de registro: "))

    while (nro_registro != 0) :
        nro_sucursal = int(input("Ingrese Nro. de sucursal: "))
        nro_producto = int(input("Ingrese Nro. de producto: "))
        ventas = int(input("Ingrese cantidad de ventas: "))

        registro = {
            "nro_registro": nro_registro,
            "nro_sucursal": nro_sucursal,
            "nro_producto": nro_producto,
            "ventas": ventas
        }

        datos['total'] += registro['ventas']
        datos['registros'].append(registro)

        nro_registro = int(input("Ingrese Nro. de registro: "))
    print('\n')

if __name__ == '__main__':
    main()
