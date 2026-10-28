class Automovil:
    def __init__(self, marca, modelo, precio, color):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        self.color=color

    def __eq__(self, other):
        return self.color==other.color

seat_ibiza = Automovil('Seat', 'Ibiza', 10_000, 'Blanco')
seat_ibiza2 = Automovil('Seat', 'Ibiza', 10_000, 'Blanco')
seat_ibiza3 = seat_ibiza2
bmw_z8 = Automovil('BMW', 'Z8', 50_000, 'Blanco')

# Operador is pregunta por la identidad del objeto
# Operador == pregunta por el contenido del objeto (__eq__)

print(seat_ibiza is bmw_z8) # False
print(seat_ibiza==bmw_z8) # True (porque son blancos los dos)

print(seat_ibiza is seat_ibiza2) # False

print(seat_ibiza2 is seat_ibiza3) # True