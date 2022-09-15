#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     14/09/2022
# Copyright:   (c) HP 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

## EJERCICIO 1 /////////////////////////////////////////////////

def area_rectangulo(base, altura):
    area_rec = base * altura
    return area_rec

area_rectangulo(7, 10)

## EJERCICIO 2 /////////////////////////////////////////////////

def area_circulo(radio):
    area_cir = 3.14159 * (radio * radio)
    return area_cir

area_circulo(9)

if __name__ == '__main__':
    main()
