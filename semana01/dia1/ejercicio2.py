monedaOrigen=""
monedaDestino=""
montoOrigen=0
montoDestino=0
opcion=0
while(opcion!=3):
    opcion=int(input("Ingrese una opcion para convertir : "))
    if(opcion==1):
        monedaOrigen="soles"
        montoOrigen = input("Ingrese el monto en "+monedaOrigen+" : ")
        monedaDestino="dolares"
        montoDestino = float(montoOrigen)/3.778
        print("El monto en "+monedaDestino+" es : "+str(montoDestino))
    elif(opcion==2):
        monedaOrigen="dolares"
        montoOrigen = input("Ingrese el monto en "+monedaOrigen+" : ")
        monedaDestino="soles"
        montoDestino = float(montoOrigen)*3.778
        print("El monto en "+monedaDestino+" es : "+str(montoDestino))
    elif(opcion==3):
        print("Se salio del programa")
    else:
        print("Elija una opcion entre 1 y 3")