class Menu:
    def __init__(self,entrada,platoFuerte,Bebidas,Postre):
        self.entrada = entrada
        self.platoFuerte= platoFuerte
        self.Bebidas = Bebidas
        self.Postre = Postre
    

class Mesa:
    def __init__(self,forma,material,cantPersonas):
        self.forma= forma
        self.material= material
        self.cantPersonas = cantPersonas
    
class Cliente:
    def __init__(self,nombre,edad,celular):
        self.nombre= nombre
        self.edad= edad
        self.celular = celular

class Factura:
    def __init__(self,nombre,apellido,cedula,valor):
        self.nombre= nombre
        self.apellido= apellido
        self.cedula = cedula
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
        
    @valor.setter
    def valor(self,newValue):
        if newValue < 0:
            raise ValueError('El valor no puede ser negativo')
        self._valor = newValue

factura1 = Factura('Juan','Perez',1234567,1000)


class Empleado:
    def __init__(self,nombre,edad,celular,cargo,horario):
        self.nombre= nombre
        self.edad= edad
        self.celular = celular
        self.cargo = cargo
        self.horario = horario
        self.valor_hora = 10

    def sueldo(self,horas):
        return self.valor_hora * horas

empleado1 = Empleado('Mateo',19,'044321266','Admin',12)



