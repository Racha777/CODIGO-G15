import os
import time
from tabulate import tabulate
from libCrud import buscarAlumnos, menu, insertarAlumno, actualizarAlumno, cargarAlumnos, grabarAlumnos


def crudAlumnos():
    if(os.path.isfile('alumnos.csv')):
        f = open('alumnos.csv', 'r')
        strAlumnos = f.read()
        alumnos = cargarAlumnos(strAlumnos)
        f.close()
    else:
        alumnos = []

    opcion = "0"
    while(opcion != "5"):
        if(opcion != "0"):
            time.sleep(3)
            os.system("clear")
        menu()
        opcion = input("INGRESE LA OPCIÓN A EJECUTAR : ")
        os.system("clear")
        if(opcion == "1"):
            print(
                """
                =====================
                [1] REGISTRAR ALUMNO
                =====================
                """
            )
            insertarAlumno(alumnos)
            print(
                """
                ==========================
                    ALUMNO REGISTRADO
                ==========================
                """
            )
        elif(opcion == "2"):
            print(
                """
                =============================================================
                                    [2] LISTADO DE ALUMNOS
                =============================================================
                """
            )
            columnas = ["nombre", "email", "celular"]
            tablaAlumnos = [alumno.values() for alumno in alumnos]
            print(tabulate(tablaAlumnos, headers=columnas, tablefmt="grid"))
            input("Presione una tecla para continuar")
        elif(opcion == "3"):
            print(
                """
                ======================
                [3] ACTUALIZAR ALUMNO
                ======================
                """
            )
            valorBusqueda = input("Ingrese alumno que desea actualizar")
            indiceAlumno = buscarAlumnos(valorBusqueda, alumnos)
            if(indiceAlumno == -1):
                print("No se encontro el alumno")
            else:
                actualizarAlumno(indiceAlumno, alumnos)
                print("ALUMNO ACTUALIZADO")

        elif(opcion == "4"):
            print(
                """
                ======================
                [4] ELIMINAR ALUMNO
                ======================
                """
            )
            valorBusqueda = input("Ingrese alumno a eliminar")
            indiceAlumno = buscarAlumnos(valorBusqueda, alumnos)
            if(indiceAlumno == -1):
                print("No se encontro el alumno")
            else:
                alumnos.pop(indiceAlumno)
                print("ALUMNO ELIMINADO")

        elif(opcion == "5"):
            print(
                """
                ======================
                [5] SALIR DEL SISTEMA
                ======================
                """
            )
            strAlumnos = grabarAlumnos(alumnos)
            fw = open('alumnos.csv', 'w')
            fw.write(strAlumnos)
            fw.close()
        else:
            print("""
            ===========================
                OPCIÓN INCORRECTA!!!
            ===========================
            """)


if __name__ == "__main__":
    crudAlumnos()
