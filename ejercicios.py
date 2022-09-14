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
    numero = int(input("Ingrese un numero impar nuevamente "))
    check = numero % 2

if (check == 1):
    print("El numero es impar")

## EJERCICIO 2 ///////////////////////////////////////////////

n1 = int(input("Ingrese un numero "))
n2 = int(input("Ingrese otro numero "))

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

## EJERCICIO 3 (no sale) ///////////////////////////////////////////////

correo = str(input("Ingrese un email "))
caracter = ""

while check == "@":
    input("Ingrese una dirección válida ")



## EJERCICIO 4 ///////////////////////////////////////////////

casla = ["Torrico", "Senesi", "Acosta", "Romagnoli", "Correa"]
contador = 0
for nom in casla:
    contador = contador + 1

print("Elementos en la lista: ", contador)


## EJERCICIO 5 ///////////////////////////////////////////////

numeros = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
suma = 0
for num in numeros:
    suma = suma + num

print("Suma total: ", suma)


## EJERCICIO 6 ///////////////////////////////////////////////

lista = [9, 19, 29]
contador = 0
suma = 0

for num in lista:
    contador = contador +1
    suma = suma + num

promedio = suma / contador
print("El valor promedio es ", promedio)


## EJERCICIO 7 (no sale) ///////////////////////////////////////////////

lista = [2, 4, 6, 8, 10, 19]
grande = 0

for num in lista:
    if (num > grande):
        print(num)
        num == grande

print("El numero mas grande de la lista es: ", grande)


## EJERCICIO 8 (no sale) ///////////////////////////////////////////////

lista = [1, 3, 5, 7, 9]
chico = 10

for num in lista:
    if (num < chico):
        print(num)
        num == chico

print("El numero mas chico de la lista es: ", chico)






if __name__ == '__main__':
    main()
