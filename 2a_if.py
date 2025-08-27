#Ejemplo de condicional IF
temperatura = 20
if temperatura > 35:
    print('Aviso por alta temperatura')
else:
    print('Parámetros normales')

#Ejemplo de condicional IF anidado con temperatura=22
temperatura = 22
if temperatura < 20:
    if temperatura < 10:
        print('Hace Frío')
    else:
        print('Está un poco fresco')
else:
    if temperatura < 30:
        print('Está agradable')
    else:
        print('Hace calor')

#Ejemplo de condicional IF anidado con temperatura=8
temperatura = 8
if temperatura < 20:
    if temperatura < 10:
        print('Hace Frío')
    else:
        print('Está un poco fresco')
else:
    if temperatura < 30:
        print('Está agradable')
    else:
        print('Hace calor')

