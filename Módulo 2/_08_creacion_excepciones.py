"""Módulo de ejemplo para la creación de excepciones personalizadas.

Este archivo muestra cómo validar los argumentos de una función y lanzar
excepciones de tipo `TypeError` y `ValueError` cuando los datos de entrada no
son válidos.
"""


def calcular_area(base: int, altura: int) -> int:
    """Calcula el área de un rectángulo.

    Args:
        base: La base del rectángulo, debe ser un entero positivo.
        altura: La altura del rectángulo, debe ser un entero positivo.

    Returns:
        El producto de la base por la altura.

    Raises:
        TypeError: Si `base` o `altura` no son enteros.
        ValueError: Si `base` o `altura` no son mayores que cero.
    """
    if not isinstance(base, int) or not isinstance(altura, int):
        raise TypeError('Los argumentos deben ser números enteros')
    if base <= 0 or altura <= 0:
        raise ValueError('Los argumentos deben ser enteros > 0')
    return base * altura

try:
    area = calcular_area(15, 3)
    print(f'El área del rectángulo es: {area}')
except TypeError as te:
    print('Error: los tipos de los argumentos deben ser enteros:' + te)
except ValueError as ve:
    print('Error: los valores de los argumentos deben ser enteros positivos:' + ve)
except BaseException as be:
    print('Error: ha ocurrido un error inesperado:' + be)