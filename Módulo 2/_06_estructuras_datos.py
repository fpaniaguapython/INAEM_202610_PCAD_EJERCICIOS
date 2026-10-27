###########################
# Lista (list)
###########################
# Mutable
# Heterogénea
# Mantiene el órden de sus elementos
# Admite duplicados
lista = ['Ítem 1', 'Ítem 3', 'Ítem 8', True, 10.8]
print(lista[3]) # Acceso a la posición 3 -> True
lista.append('Ítem 10') # Añadir al final
print(lista[2:4]) # ['Ítem 8', True]
lista.remove('Ítem 3') # Borra el elemento correspondiente
del lista[1] # Elimina 'Ítem 8'
print(lista) # ['Ítem 1', True, 10.8, 'Ítem 10']

# Recorrer todos los elementos de una lista
for cosa in lista:
    print(cosa)

###########################
# Tupla (tuple)
###########################
# INMUTABLE
# Heterogénea
# Mantiene el órden de sus elementos
# Admite duplicados
cesta_compra = ('Pan', True, 10.8, 'Leche')
print(cesta_compra[3]) # Acceso a la posición 3 ->Leche
print(cesta_compra[:2]) # ('Pan', True)
# NO SE PUEDE BORRAR DE UNA TUPLA

# Recorrer todos los elementos de una tupla
for producto in cesta_compra:
    print(producto)

###########################
# Diccionario (dict)
###########################
# Mutable
# Heterogéneo
# ¿Mantiene el orden? Da igual
# NO admite claves duplicadas
ingredientes = {
    'gazpacho': ('Tomate', 'Aceite', 'Ajo', 'Sal', 'Pepino', 'Pimiento'),
    'huevos_con_chorizo': ('Huevo', 'Chorizo', 'Aceite', 'Sal'),
    'arroz_con_leche': ('Arroz', 'Leche', 'Azúcar', 'Canela')
}
ingredientes_gazpacho = ingredientes['gazpacho']
print(ingredientes_gazpacho) # ('Tomate', 'Aceite', 'Ajo', 'Sal', 'Pepino', 'Pimiento')
ingredientes_huevos = ingredientes.get('huevos_con_chorizo')
print(ingredientes_huevos) # ('Huevo', 'Chorizo', 'Aceite', 'Sal')
ingredientes_sardinas = ingredientes.get('sardinas')
print(ingredientes_sardinas) # None
ingredientes_caldo = ingredientes.get('caldo', ('Agua', 'Sal', 'Repollo', 'Hueso de jamón'))
print(ingredientes_caldo) # ('Agua', 'Sal', 'Repollo', 'Hueso de jamón')

del ingredientes['huevos_con_chorizo']
print(ingredientes)

# Claves
for clave in ingredientes.keys():
    print(clave)

# Valores
for valor in ingredientes.values():
    print(valor)

# Claves y valores
for clave, valor in ingredientes.items():
    print(clave, valor)

###########################
# Conjuntos (set)
###########################
# Mutable
# Heterogénea
# NO Mantiene el órden de sus elementos
# NO Admite duplicados
conjunto = {1, 2, 'Patata', 5, 5, 3, 7, 0, 1, 4}
conjunto.add(8)
print(conjunto)

alergias = ('Pescado', 'Marisco', 'Legumbre', 'Huevo')
receta = ('Maiz', 'Aceite', 'Pimiento', 'Marisco')

alergias = set(alergias)
print(type(alergias)) # <class 'set'>

comunes = alergias.intersection(receta)
print(comunes)