#Ejercicio 6: Secuencia de Fibonacci

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

print('Ingrese un numero :')
n = input()
fibonacci(int(n))