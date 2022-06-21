f=open('alumnos.txt','w')
f.write('\njavier ramos,javier@gmail.com,123456789')
print("Archivo creado con exito")

f.write('\njorge ramos,jorge@gmail.com,123456789')
f.write('\nalvaro chang,alvaro@gmail.com,123456789')
f.close()
fr=open('alumnos.txt','r')
dataAlumnos=fr.read()
print(dataAlumnos)
fr.close()

fa=open('alumnos.txt','a')
nombre=input("nombre : ")