class Alumno:
    def __init__(self,nom,ema,nota):
        self.nombre=nom
        self.email=ema
        self.nota=nota

    def mostrar(self):
        print("Nombre : "+self.nombre)
        print("Email : "+self.email)
        print("Nota : "+str(self.nota))

class Profesor:
    def __init__(self,nom,ema,esp):
        self.nombre=nom
        self.email=ema
        self.especialidad=esp
    
    def mostrar(self):
        print("Nombre : "+self.nombre)
        print("Email : "+self.email)
        print("Especialidades : "+self.especialidad)

alumnoJavier=Alumno('Javier Ramos','javier@gmail.com',18)
alumnoJavier.mostrar()

alumnoNuevo=Alumno('Jorge Perez','jorge@gmail.com',20)
alumnoNuevo.mostrar()

prof1=Profesor('Cesar Mayta','cesar@gmail.com','backend')
prof1.mostrar()