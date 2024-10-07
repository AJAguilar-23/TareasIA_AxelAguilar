# Ejercicio 7: Tabla de Multiplicar

def tabla(n):
    for i in range(10):
        print(f'{n} x {i+1} = {n*(i+1)}')

print('Ingrese un numero :')
n = input()
print(f'Tabla de multiplicar del {n} :')

tabla(int(n))