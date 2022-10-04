#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emanuel
#
# Created:     26/09/2022
# Copyright:   (c) Emanuel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    libro={}
    conjuntoLibros={}
    num=1
    contador=0
    acumcan=0
    acumpre=0
    promedio=0
    #Control
    while True:
        isbn=int(input("Ingrese ISBN: "))
        if isbn == 0:
            break
        nombreLibro=(input("Ingrese nombre del libro: "))
        stock=int(input("Ingrese stock del libro: "))
        precioLibro=int(input("Ingrese el precio del libro: "))
        
        libro["isbn"]=isbn
        libro["nombreLibro"]=nombreLibro
        libro["stock"]=stock
        libro["precioLibro"]=precioLibro
        conjuntoLibros[f"libro {num}"]=libro
        libro={}
        acumcan=acumcan+stock
        acumpre=acumpre+precioLibro
        if acumcan != 0:
            promedio=acumpre/acumcan
        num=num+1
        contador+=1
    num=1
    print(contador)
    print(conjuntoLibros)
    # Totales
    print(f"Cantidad total de libros: {acumcan}")
    print(f"Monto total de todos los libros: {acumpre}")
    print(f"Promedio de todos los libros: {promedio}")
    while num!=contador+1:
        sublibro=conjuntoLibros[f"libro {num}"]
        isbn=sublibro["isbn"]
        nombreLibro=sublibro["nombreLibro"]
        stock=sublibro["stock"]
        precioLibro=sublibro["precioLibro"]
        num=num+1
        print("NOMBRE DEL LIBRO:", end=" ")
        print(nombreLibro)
        print("Isbn:", end=" ")
        print(isbn)
        print("Stock:", end=" ")
        print(stock)
        print("Precio: ", end=" ")
        print(precioLibro)

if __name__ == '__main__':
    main()
