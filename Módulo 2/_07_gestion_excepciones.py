lista = [3, 5, 8, -1]

indice = int(input('Índice:'))

while (indice!=-1):
    try:
        valor = lista[indice]
        print(valor)
    except IndexError as ie:
        print(f'El índice debe estar entre 0 y {len(lista)}')
    else:
        print('Eso se ejecuta SÓLO si no ha habido error')
    finally:
        print('Esto se ejecuta SIEMPRE')
    indice = int(input('Índice:'))
