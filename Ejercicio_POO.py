class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido}'


class Cliente(Persona):

    def __init__(self,nombre,apellido, num_cuenta,balance):
        super(Cliente, self).__init__(nombre,apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return f'{super} Numero de Cuenta: {self.num_cuentar} Balance: {self.balance}'

cliente = Cliente