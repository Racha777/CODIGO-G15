import os
import time
"""
APLICACION CRUD
"""
alumnos=[
    {'nombre':'cesar mayta',
    'email':'cesarmayta@gmail.com',
    'ceular':'956290589'}
    ]

opcion="0"
while(opcion!="5"):
    if(opcion!="0"):
        time.sleep(5)
        os.system("clear")
    print(
        """
        ==================================================
                SISTEMA DE MATRICULA DE ALUMNOS
        ==================================================
        [1] REGISTRAR ALUMNO
        [2] MOSTRAR ALUMNO
        [3] ACTUALIZR ALUMNO
        [4] ELIMINAR ALUMNO
        [5] SALIR DEL SISTEMA
        """
    )
    opcion = input("INGRESE LA OPCIÓN A EJECUTAR : ")
    os.system("clear")
    if(opcion=="1"):
        print(
            """
            =====================
            [1] REGISTRAR ALUMNO
            =====================
            """
        )
        nombre=input("NOMBRE : ")
        email=input("EMAIL : ")
        celular=input("CELULAR : ")
        dictNuevoAlumno={
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictNuevoAlumno)
        print(
            """
            ==========================
                ALUMNO REGISTRADO
            ==========================
            """
        )
    elif(opcion=="2"):
        print(
            """
            =============================================================
                                [2] LISTADO DE ALUMNOS
            =============================================================
            =       NOMBRE      =       EMAIL       =      CELULAR      =
            """
        )
        for alumno in alumnos:
            print("         ",end=' ')
            for values in alumno.values():
                print("| "+values,end=' ')
            print()
        print("         =============================================================")
        input("Presione una tecla para continuar")
    elif(opcion=="3"):
        print(
            """
            ======================
            [3] ACTUALIZAR ALUMNO
            ======================
            """
        )
        valorBusqueda=input("Ingrese alumno que desea actualizar")
        indiceAlumno=-1
        for indice in range(len(alumnos)):
            alumno=alumnos[indice]
            for clave,valor in alumno.items():
                if(clave=='email' and valor==valorBusqueda):
                    indiceAlumno=indice
                    break
        if(indiceAlumno==-1):
            print("No se encontro el alumno")
        else:
            print("Alumno a editar : "+alumnos[indiceAlumno].get("nombre"))
            print("NUEVOS VALORES PARA ALUMNO : ")
            nombre=input("NOMBRE ("+alumnos[indiceAlumno].get("nombre") +") : ")
            if(nombre==''):
                alumnos[indiceAlumno].get("nombre")
            email=input("EMAIL ("+alumnos[indiceAlumno].get("email") +") : ")
            if(email==''):
                alumnos[indiceAlumno].get("email")
            celular=input("CELULAR ("+alumnos[indiceAlumno].get("celular") +") : ")
            if(celular==''):
                alumnos[indiceAlumno].get("celular")
            dictAlumnoEditar={
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos[indiceAlumno]=dictAlumnoEditar
        print("ALUMNO ACTUALIZADO")


    elif(opcion=="4"):
        print(
            """
            ======================
            [4] ELIMINAR ALUMNO
            ======================
            """
        )
        valorBusqueda=input("Ingrese alumno a eliminar")
        indiceAlumno=-1
        for indice in range(len(alumnos)):
            alumno=alumnos[indice]
            for clave,valor in alumno.items():
                if(clave=='email' and valor==valorBusqueda):
                    indiceAlumno=indice
                    break
        if(indiceAlumno==-1):
            print("No se encontro el alumno")
        else:
            alumnos.pop(indiceAlumno)
            print("ALUMNO ELIMINADO")
        
    elif(opcion=="5"):
        print(
            """
            ======================
            [5] SALIR DEL SISTEMA
            ======================
            """
        )