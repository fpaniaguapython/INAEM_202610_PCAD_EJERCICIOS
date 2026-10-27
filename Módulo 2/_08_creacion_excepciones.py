def calcular_area(base: int, altura: int) ->int:
    if not isinstance(base, int) or not isinstance(altura, int):
        raise TypeError('Los argumentos deben ser números enteros')
    if base<=0 or altura<=0:
        raise ValueError('Los argumentos deben ser enteros > 0')
    return base * altura