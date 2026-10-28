class Empleado:
    def __init__(self, nombre, identificador, categoria, salario):
        self.nombre = nombre
        self.identificador = identificador
        self.categoria = categoria
        self.__salario = salario

    def get_salario(self, es_de_dia:bool):
        if (es_de_dia==True):
            return self.__salario
        else:
            raise BaseException('No se puede consultar el salario de noche')

    def set_salario(self, nuevo_salario: int):
        if nuevo_salario>self.__salario:
            self.__salario = nuevo_salario
        else:
            raise ValueError('El nuevo salario no puede ser inferior al actual')