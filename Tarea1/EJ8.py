#Ejercicio 8: Contador de Vocales

def count_v(n):
    v = 0
    for i in range(len(n)): 
        if n[i] in ('a','e','i','o','u'):
             #print(n[i])
             v += 1
    #print (v)
    return v

print('Ingrese una frase, para contar las vocales')
n='hola mundo'
print(f"El texto ingresado tiene {count_v(n)} vocales")

