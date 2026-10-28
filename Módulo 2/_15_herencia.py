class ElementoTransporte:
    def __init__(self, nombre, capacidad, velocidad_punta):
        self.nombre = nombre
        self.capacidad = capacidad
        self.velocidad_punta = velocidad_punta

    def desplazarse(self, latitud, longitud):
        print('Me deplazo...')

    def repostar(self):
        print('Repostando...')

class ElementoTransporteAereo(ElementoTransporte):
    def despegar(self):
        print('Despegando...')

    def aterrizar(self):
        print('Aterrizando...')

f18 = ElementoTransporteAereo('F18', 1, 2_000)
f18.repostar()
f18.despegar()
f18.desplazarse(longitud=15.0, latitud=8.12)
f18.aterrizar()

borrico = ElementoTransporte('Borrico', 1, 15)
borrico.repostar()
borrico.desplazarse(longitud=15.1, latitud=8.4)