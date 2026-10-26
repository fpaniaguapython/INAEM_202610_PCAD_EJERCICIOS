lista = ['Elemento 1', 'Elemento 2', 'Elemento 3', 'Elemento 4',
         'Elemento 5', 'Elemento 6', 'Elemento 7', 'Elemento 8']

for item in lista:
    if ('2' in item):
        print(f'Descartado {item}')
        continue
    if ('6' in item):
        print(f'Encontrado {item}')
        break
    print(f'Procesado {item}')
