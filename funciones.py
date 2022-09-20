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
    return print(area_rec)

area_rectangulo(7, 10)

## EJERCICIO 2 /////////////////////////////////////////////////

def area_circulo(radio):
    area_cir = 3.14159 * (radio * radio)
    return print(area_cir)

area_circulo(9)

## EJERCICIO 3 /////////////////////////////////////////////////

def relacion(nro1, nro2):
    if (nro1 > nro2):
        return print(1)
    elif (nro2 > nro1):
        return print(-1)
    else:
        return print(0) # Imprimo resultado para verificación.
                        # También modifiqué los demás ejercicios.

relacion(2, 3)

## EJERCICIO 4 /////////////////////////////////////////////////

def intermedio(n1, n2):
    int = (n1/2) + (n2/2)
    return print(int)

intermedio(10, 24)

## EJERCICIO 5 /////////////////////////////////////////////////

def recortar(rec, inf, sup):
    if (rec < inf):
        return print(inf)
    elif (rec > sup):
        return print(sup)
    else:
        return print(rec)

recortar(5, 2, 7)










if __name__ == '__main__':
    main()
