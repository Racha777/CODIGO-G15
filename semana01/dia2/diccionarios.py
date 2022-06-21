capitales={
    'Peru':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Uruguay':'Montevideo'
}

print(capitales)
nuevaCapital={'Brasil':'Brasilia'}
capitales.update(nuevaCapital)
print(capitales)
capitales.update({'Ecuador':'Guayaquil'})
print(capitales)
print(capitales.get('Peru'))
capitales.pop('Ecuador')
print(capitales)

c=capitales.pop('Chile')
print("Se elimino "+c)
print(capitales)

"""
pais=input("Ingrese el pais: ")
capital=capitales.get(pais,'no existe')
print("La capital de "+pais+" es "+capital)
"""
#Iteracion de diccionarios
for capital in capitales:
    print('la capital de '+capital+" es "+capitales[capital])
print(capitales.keys())
print(capitales.values())
print(capitales.items())

for clave in capitales.keys():
    print(clave+" => "+capitales[clave])

for clave,valor in capitales.items():
    print(clave +" -- "+valor)