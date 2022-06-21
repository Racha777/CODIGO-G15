class Persona:
    def __init__(self,nom,ema):
        self.nombre=nom
        self.email=ema

    def mostrar(self):
        print("Nombre : "+self.nombre)
        print("Email : "+self.email)

class Alumno(Persona):
    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota=nota

    def mostrar(self):
        super().mostrar()
        print("Nota : "+str(self.nota))

class Profesor(Persona):
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad=esp

    def mostrar(self):
        super().mostrar()
        print("Especialidad : "+self.especialidad)

alu1=Alumno('Javier Ramos','javier@gmail.com',18)
alu1.mostrar()

prof1=Profesor('Cesar Mayta','cesar@gmail.com','backend')
prof1.mostrar()