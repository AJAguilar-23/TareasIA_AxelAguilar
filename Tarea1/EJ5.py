#Ejercicio 5: Número Primo

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print('Ingrese un numero :')
n = input()
#print(es_primo(int(n)))


if es_primo(int(n)) == True:
    print('El numero es primo')
else:
    print('El numero no es primo')
    