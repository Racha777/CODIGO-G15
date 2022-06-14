"""
EJERCICIOS 01:
INGRESE UN TEXTO Y UN DIVISOR, Y LUEGO MUESTRE EL MISMO TEXTO PERO DIVIDIDO POR EL DIVISOR
"""
texto=input("ingrese un texto : ")
divisor=int(input("ingrese un divisor : "))

textoLongitud=len(texto)

for contador in range(0,textoLongitud,divisor):
    print(texto[contador:contador+divisor])