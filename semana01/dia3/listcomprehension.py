listaNombre=[]
strNombre="cesar mayta"
for strLetra in strNombre:
    listaNombre.append(strLetra)

print(listaNombre)

listaNombre=[strLetra for strLetra in strNombre]
print(listaNombre)