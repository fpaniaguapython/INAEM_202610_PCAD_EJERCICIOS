import json

# Declaración de la clase
class Factura:
    def __init__(self, # Constructor
                 numero: int, 
                 proveedor: str, 
                 fecha: str, 
                 items: list,
                 pendiente_pago = True):
        self.numero = numero
        self.proveedor = proveedor
        self.fecha = fecha
        self.items = items
        self.pendiente_pago = pendiente_pago
        self.activa = True

    def guardar(self): # Método guardar
        """
        Guarda en un fichero json el contenido de la factura
        """
        with open(f'factura_{self.numero}.json', mode='w', encoding='utf-8') as fichero:
            fichero.write(json.dumps(self.__dict__))

# Instanciación de los objetos
factura_1 = Factura(
    numero=1, 
    proveedor='Gobierno', 
    fecha='28/10/2026', 
    items=['Papel', 'Tóner'])

factura_1.guardar()



