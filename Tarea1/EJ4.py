#Ejercicio 4: Clase Calculadora

class Calculadora:
    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            return('No se puede divir entre 0')
        else:
            return a/b
        
c1 = Calculadora()

print(c1.sumar(2,2))
print(c1.restar(3,3))
print(c1.multiplicar(4,5))
print(c1.dividir(6,0))
print(c1.dividir(6,6))