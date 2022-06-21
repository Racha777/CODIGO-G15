import os
alumnos = []

if(os.path.isfile('alumnos.csv')):
    archivoAlumnos = open('alumnos.csv', 'r')
else:
    archivoAlumnos = open('alumnos.csv', 'a')
    archivoAlumnos.write('javier ramos,javier@gmail.com,123456789')
    archivoAlumnos.write('\njorge ramos,jorge@gmail.com,123456789')
    archivoAlumnos.write('\nalvaro chang,alvaro@gmail.com,123456789')

strAlumnos=archivoAlumnos.read()
print(strAlumnos)
archivoAlumnos.close()

lstAlumnos=strAlumnos.splitlines()
print(lstAlumnos)
for l in lstAlumnos:
    alumnoData=l.split(',')
    dictAlumno={
        'nombre':alumnoData[0],
        'email':alumnoData[1],
        'celular':alumnoData[2]
    }
    alumnos.append(dictAlumno)