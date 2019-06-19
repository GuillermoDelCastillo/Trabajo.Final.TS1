import random

deposito = list(range(1,80))
random.shuffle(deposito)

jugadores = []
bolillas = []
pregunta = True
continuar = 0
ejecucion = True
dato = True

nJ = int(input("Ingrese el numero de participantes: "))
nC = int(input("Ingrese el numero de cartillas vendidas: "))

pozo = nC * 5

i = 0
n = 0

while i < nJ:

    nombre = (input("Ingrese el nombre del jugador: "))
    jugadores.append(nombre)

    i+= 1

while (ejecucion):
    print("Digite 1 para empezar a jugar.")
    print("Digite 2 para ver el registro de bolillas.")
    print("Digite 3 para reiniciar el juego.")        
    print("Digite 4 para finalizar.")
    dato = True
    pregunta = True
    while dato:
        opcion = input("Ingrese la opcion: ")
        try:
            opcion = int(opcion)
            if opcion >=1 and opcion<=4:

                if opcion == 1:
                    while (pregunta):
                        for i in range (1):
                            e = deposito[0]
                            deposito.remove(e)
                            bolillas.append(e)
                            bolillas.reverse()
                            print ("La bolilla es: ",bolillas[i])
                            continuar = input("Desea continuar: Si(1) o No(2): ")
                            if deposito:
                                print("Aun quedan bolillas.")
                            else:
                                print("Se acabaron las bolillas :( nadie ganó.")
                                print("Reiniciando deposito de bolillas.")
                                deposito = list(range(1,80))
                                random.shuffle(deposito)
                                break
                            try:
                                continuar = int(continuar)
                                if 1 <= continuar <= 2:
                                    if continuar == 2:
                                        pregunta = False
                                        dato = False
                                    elif continuar == 1:
                                        pregunta = True
                                else:
                                    print("Debe presionar 1 o 2")
                                    pregunta = False
                                    dato = False
                                
                            except ValueError:
                                print("Debe presionar 1 o 2")
                         
                elif opcion == 2:
                        print(bolillas)
                        pregunta = False
                        dato = False
                elif opcion == 3:
                        bolillas.clear()
                        pregunta = False
                        dato = False
                        print("Reiniciando...")
                        print("Las bolillas fueron devueltas al depósito")
                elif opcion == 4:
                    print("El monto ganado es: s/.", pozo)
                    ejecucion = False
                    pregunta = False
                    dato = False
                    break

            else:
                print("opción incorrecta")
        except ValueError:
            print ("Opcion equivocada ingrese una opcion valida")

print("FIN")
