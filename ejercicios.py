#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     06/09/2022
# Copyright:   (c) HP 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass


## EJERCICIO 1

numero = int(input("Ingrese un numero impar "))
check = numero % 2

while (check == 0):
    numero = input("Ingrese un numero impar nuevamente ")
    check = numero % 2

if (check == 1):
    print("El numero es impar")

## EJERCICIO 2

n1 = int(input("Ingrese un numero"))
n2 = int(input("Ingrese otro numero"))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2

print("Op 1: Suma")
print("Op 2: Resta")
print("Op 3: Multiplicación")
v1 = input("Elija una opción ")
v2 = input("Confirme su opción ")

while v2 != v1:
    v2 = input("Confirme su opción nuevamente ")

if v2 == 1:
    print("Suma: ", suma)
elif (v2 == 2):
    print("Resta: ", resta)
else:
    print("Multiplicación: ", multi)


if __name__ == '__main__':
    main()
