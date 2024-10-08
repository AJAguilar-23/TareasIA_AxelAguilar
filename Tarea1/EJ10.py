#Ejercicio 10: Generador de Contraseñas

import random
caracteres = '0123456789'+'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'+'!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
#print(caracteres)

def generador_c(num):
    contra =random.sample(caracteres,num)
    #print("".join(contra))
    return "".join(contra)   

ward = True
while ward:
    n = int(input('Ingrese la cantidad de caracteres que desea en su password '))
    if n >=8:
        c = generador_c(n)
        ward = False    

print('Su password es:', c)