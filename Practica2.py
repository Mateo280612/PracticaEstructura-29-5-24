class Personas:
    def __init__(self,nombre,edad,celular):
        self.nombre= nombre
        self.edad= edad
        self.celular = celular
    def saludar(self):
        return f'Hola mi nombre es: {self.nombre}'
    def despedirse(self):
        return f'Adios mi nombre es {self.nombre}'

class Cliente(Personas):
    def __init__(self, nombre, edad, celular):
        super().__init__(nombre, edad, celular)

cliente1 = Cliente('Juan',23,1234567)

class Empleado(Personas):
    def __init__(self, nombre, edad, celular,cargo,horario):
        super().__init__(nombre, edad, celular)
        self.cargo = cargo
        self.horario = horario
        self.valor = 10

    def sueldo(self,horas):
        return self.valor_hora * horas
    
    def saludar(self):
        return f'Hola mi nombre es: {self.nombre} y soy {self.cargo}'
    def despedirse(self):
        return f'Adios mi nombre es {self.nombre} y que tenga un excelente dia'
    
    
empleado1 = Empleado('Pepe',19,1234567,'Mesero',20)
print(empleado1.saludar())
print(cliente1.saludar())
print(empleado1.despedirse())
print(cliente1.despedirse())
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