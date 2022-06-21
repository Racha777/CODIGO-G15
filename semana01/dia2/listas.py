#En paythin los array se llaman listas
dias=["lunes","martes","miercoles"]
print(dias)
print(dias[1])
dias.append("miercoles")
print(dias)
dias.pop()
print(dias)
dias[0]="domingo"
print(dias)

for dia in dias:
    print(dia,end=" ")

alumnos=[]
totalAlumnos=int(input("Ingrese el total de alumnos a registrar"))
for contador in range(totalAlumnos):
    nuevoAlumno=input("Nombre del alumno "+str(contador)+" : ")
    alumnos.append(nuevoAlumno)
print("relacion de alumnos : ")
for alumno in alumnos:
    print(alumno,end=" | ")