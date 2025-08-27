# Exportar datos a CSV (ejemplo)
from faker import Faker
import csv

fake = Faker('es_ES')

with open('usuarios.csv', 'w', newline='', encoding='utf-8') as archivo:
    campos = ['nombre', 'email', 'telefono']
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for _ in range(20):
        writer.writerow({
            "nombre": fake.name(),
            "email": fake.email(),
            "telefono": fake.phone_number()
        })

