#pip install faker
#Primeros pasos
from faker import Faker

# Idioma de los datos
# Faker puede generar datos en diferentes idiomas. Por ejemplo, para usar español:
fake = Faker('es_ES')

print(fake.name())       # Genera un nombre completo
print(fake.email())      # Genera un email
print(fake.address())    # Genera una dirección
