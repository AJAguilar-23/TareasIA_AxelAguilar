#Ejercicio 3: Clase CuentaBancaria

class CuentaBancaria:
    saldo = 0

    def __init__(self, titular):
        self.titular = titular
    
    def depositar(self, cantidad):
        self.saldo +=cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -=cantidad
    
    def mostrar_saldo(self):
        print(self.saldo)

c1 = CuentaBancaria("Axel Aguilar")

c1.mostrar_saldo()
c1.depositar(1000)
c1.mostrar_saldo()
c1.retirar(250)
c1.mostrar_saldo()
c1.depositar(500)
c1.mostrar_saldo()

