# El módulo copy forma parte de las librerías estándar de Python
import copy

lista1 = [1, 2, 3, [4, 5, 6]]
# lista2 = lista1 # Son la misma lista
# lista2 = lista1[:] # Shallow copy. Copia el primer nivel.
# lista2 = lista1.copy() # Shallow copy. Copia el primer nivel.
lista2 = copy.deepcopy(lista1) # Deep copy. Copia todos los niveles