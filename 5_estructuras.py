# 1. Listas (list)
# Una lista es una colección ordenada y modificable de elementos.
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])  # manzana
frutas.append("uva")  # agrega uva al final
# Pueden contener datos repetidos
# Se accede por índice (desde 0)

# 2. Tuplas (tuple)
# Una tupla es una colección ordenada pero inmutable (no se puede modificar después de creada).
coordenadas = (40.7128, -74.0060)
print(coordenadas[0])  # 40.7128
# Más rápida y segura que la lista si no necesitás modificarla.
# Útil para datos fijos.

# 3. Conjuntos (set)
# Un conjunto es una colección desordenada y sin elementos repetidos.
numeros = {1, 2, 3, 2, 1}
print(numeros)  # {1, 2, 3}
# No hay duplicados.
# Ideal para comprobar pertenencia (in).

# 4. Diccionarios (dict)
# Colección desordenada pero indexada por claves.
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Ana