#Crear una Clase
class Automovil:
    def __init__(self,aa,pl,col,mar):
        self.año=aa
        self.placa=pl
        self.color=col
        self.marca=mar
    
    #crear metodos
    def encender(self):
        print('encender '+self.marca)

    def avanzar(self):
        print('avanzar '+self.marca)

    def acelerar(self):
        print('encender '+self.marca)
    
    def frenar(self):
        print('frenar '+self.marca)

#creacion de objetos
vw=Automovil(1970,'CH-1234','amarillo','volkswagen')
print("se creo el objeto vw con los siguientes datos : ")

print("año: "+str(vw.año))
print("color: "+vw.color)
print("placa: "+vw.placa)
print("marca: "+vw.marca)

vw.encender()