def calcular_area(base_rectangulo: float, altura_rectangulo: float) -> float:
    """
    (Docstring)
    Calcula el área de un rectángulo.

    Params:
    - base_rectangulo: La medida de la base del rectángulo en cm.
    - altura_rectangulo: La media de la altura del rectángulo en cm.

    Return:
    - El área calculada del rectángulo.
    """
    area = base_rectangulo * altura_rectangulo
    return area

area = calcular_area(base_rectangulo=10, altura_rectangulo=15)

def multiplicar(numero_1: int, numero_2:int = 10) -> int:
    return numero_1*numero_2

multiplicar(10, 5) # Argumentos posicionales
multiplicar(10) # Argumentos posicionales
multiplicar(numero_2=8, numero_1=3) # Argumentos keywords
