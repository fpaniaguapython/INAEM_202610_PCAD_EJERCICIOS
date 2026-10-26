def sumar(sumando_1: int, sumando_2: int) -> int:
    resultado = sumando_1 + sumando_2
    return resultado

def validar_dia_semana(dia_a_verificar: str) -> bool:
    DIAS_SEMANA = ['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES']
    es_valido = dia_a_verificar in DIAS_SEMANA
    return es_valido

def leer_ccaa(nombre_fichero: str) -> list:
    with open(nombre_fichero, mode='rt', encoding='utf-8') as fichero:
        ccaa = fichero.readlines()
    ccaa = [comunidad.strip() for comunidad in ccaa]
    return ccaa

ccaa = leer_ccaa('ccaa.txt')

def validar_ccaa(comunidades_autonomas: list, comunidad: str) -> bool:
    comunidad_valida = comunidad in comunidades_autonomas
    return comunidad_valida


print(validar_ccaa(ccaa, 'ARAGORN'))





