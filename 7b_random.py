# Combinar random con fake
import random
from faker import Faker

fake = Faker('es_ES')
generos = ['Masculino', 'Femenino']

for _ in range(5):
    genero = random.choice(generos)
    if genero == 'Masculino':
        nombre = fake.first_name_male()
    else:
        nombre = fake.first_name_female()
    apellido = fake.last_name()

    persona = {
        "nombre": f"{nombre} {apellido}",
        "genero": genero,
        "email": fake.email(),
        "telefono": fake.phone_number()
    }
    print(persona)


