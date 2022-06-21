palabraInicial=input("Escribe una palabra : ")
palabraInicial=palabraInicial.replace(' ','')
palabraInicial=palabraInicial.lower()
palabraReversa=palabraInicial[::-1]

if(palabraInicial==palabraReversa):
    print("Es un palindromo")
else:
    print("No es un palindromo")
