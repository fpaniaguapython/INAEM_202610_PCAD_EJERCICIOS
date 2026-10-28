class ArmaLaser:
    def disparar(self):
        pass

class ArmaBombas:
    def disparar(self):
        pass


class NaveEspacial:
    def __init__(self, nombre, capacidad, velocidad_punta, arma):
        self.nombre = nombre
        self.capacidad = capacidad
        self.velocidad_punta = velocidad_punta
        self.arma = arma

    def desplazarse(self, latitud, longitud):
        print('Me deplazo...')

    def repostar(self):
        print('Repostando...')

    def disparar(self):
        self.arma.disparar()

    