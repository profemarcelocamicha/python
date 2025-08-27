def saludar():
    print("Hola, ¿cómo estás?")
# Para llamarla:
saludar()

# Funciones con parámetros
# Una función puede recibir parámetros, que son datos que se le pasan para que trabaje con ellos. Dentro de la función, esos valores se pueden usar como variables normales.
# Ejemplo:
def saludar_persona(nombre):
    print("Hola", nombre)
saludar_persona("Ana")
# Diferencias:
# Parámetro: variable definida en la función (nombre).
# Argumento: valor que se pasa al llamar la función ("Ana").


# Funciones que retornan valores
# A veces, queremos que una función nos devuelva un resultado. Para eso usamos la palabra clave return.
# Ejemplo:
def cuadrado(numero):
    return numero * numero
resultado = cuadrado(4)
print("El resultado es:", resultado)