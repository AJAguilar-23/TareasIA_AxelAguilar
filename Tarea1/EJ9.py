#Ejercicio 9: Adivina el Número

import random

n = random.randrange(1,101)
intentos = 1

#print(n)
print('Adivine el numero entre 1 y 100')

i = True
while i:
    nu = int(input('Ingrese un numero '))
    if nu < n:
        print('El numero ingresado es menor')
    elif nu > n:
        print('El numero ingresado es mayor')
    elif nu == n:
        print('Felicidades ah adivinado el numero, que era',n)
        print('No de intentos: ', intentos)
        i = False
    intentos += 1