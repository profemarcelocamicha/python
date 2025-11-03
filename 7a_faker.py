#pip install faker
#Primeros pasos
from faker import Faker

# Idioma de los datos
# Faker puede generar datos en diferentes idiomas. Por ejemplo, para usar español:
fake = Faker('es_ES')

print(fake.name())       # Genera un nombre completo
print(fake.email())      # Genera un email
print(fake.address())    # Genera una dirección


# Almacenar datos dentro de una lista
usuarios = []
for _ in range(10):
    usuarios.append({
        "nombre": fake.name(),
        "email": fake.email(),
        "telefono": fake.phone_number(),
        "direccion": fake.address(),
        "sexo": fake.random_element(elements=('M', 'F')),
        "edad": fake.random_int(min=0, max=100)        
    })

print(usuarios)