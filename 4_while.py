print("Ejemplo de bucle con while")
intentos = 0
while intentos < 5:
    print("hola")
    intentos = intentos + 1

# print("Ejecución de bucle while infinito")
# intentos = 0
# while intentos < 5:
#     print("hola")

print("Ejecución de bucle while con la concatenación del número de intentos. (sumando 1 a la variable intentos)")
intentos = 0
while intentos < 5:
    print("intento número:",intentos)
    intentos = intentos + 1

print("Ejecución de bucle while con la concatenación del número de intentos. (modificando la condición intentos < 10)")
intentos = 0
while intentos < 10:
    print("intento número:",intentos)
    intentos = intentos + 1

print("Ejecución de bucle while con la concatenación del número de intentos. (sumando 2 a la variable intentos)")
intentos = 0
while intentos < 10:
    print("intento número:",intentos)
    intentos = intentos + 2


print("Ejecución de bucle while con break y continue")
intentos = 0
while intentos < 10:
    if intentos == 5:
        break
    if intentos == 2:
        intentos = intentos + 1
        continue
    print(intentos)
    intentos = intentos + 1
    