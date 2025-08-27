print("Ejemplo para recorrer una lista")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

print("Ejemplo usando range() para contar")
for i in range(5):
    print(i)

print("Ejemplo para contar con inicio, fin y paso")
for i in range(1, 10, 2):
    print(i)

print("Ejemplo para recorrer una cadena de texto")
for letra in "paz":
    print(letra)

print("Ejemplo para recorrer un diccionario")
persona = {"nombre": "Ana", "edad": 30}
for clave in persona:
    print(clave, ":", persona[clave])

print("Ejemplo para con una condición if (imprimir solo números pares)")
for i in range(10):
    if i % 2 == 0:
        print(i)

print("Ejemplo con break y continue")
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

