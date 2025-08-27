#Ejemplo de condicional match con temperatura=22
t = 22
match t:
    case t if t < 10:
        print('hace frío')
    case t if t < 20:
        print('Está un poco fresco')
    case t if t < 30:
        print('Está agradable')
    case _:
        print('Hace calor')

#Ejemplo de condicional match con temperatura=32
t = 32
match t:
    case t if t < 10:
        print('hace frío')
    case t if t < 20:
        print('Está un poco fresco')
    case t if t < 30:
        print('Está agradable')
    case _:
        print('Hace calor')

