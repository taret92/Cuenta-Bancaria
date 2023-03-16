from os import system
from random import randint


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"


    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print(f"Su nuevo balance es: ${self.balance}")
        else:
            print(f"No tiene saldo suficiente para realizar el retiro, su saldo es\n {self.balance}")


def crear_cliente():
    nombre_cl= input("Por favor ingrese su nombre: \n")
    apellido_cl = input("Por favor ingrese su apellido: \n")
    nuevo_numerocuenta = randint(000000, 999999)
    print(f"Su nuevo numero de cuenta es {nuevo_numerocuenta}")
    cliente = Cliente(nombre_cl, apellido_cl, nuevo_numerocuenta)
    return cliente

def inicio():
    mi_cliente= crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != "S":
        print("[D] - Deposito")
        print("[R] - Retiro")
        print("[S] - Finalizar programa")
        opcion = input("Por favor seleccione una opcion: \n").upper()

        if opcion == 'D':
            monto_dep= int(input("Monto a depositar: $"))
            mi_cliente.depositar(monto_dep)

        elif opcion == 'R':
            monto_ret= int(input("Por favor ingrese el monto a retirar: $"))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar con NuestroBanco")


inicio()