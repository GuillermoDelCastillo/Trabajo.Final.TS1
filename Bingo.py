def pedirNum():
 
    incorrecto = False
    num=0
    while(not correcto):
        try:
            num = int(input("Indica la opción: "))
            incorrecto = True
        except ValueError:
            print("Error, introduce opción.")
 
    return num
 
salir = False
opcion = 0
 
while not salir:
    print("-----------BINGO---------")
    print("1.---------Jugar---------")
    print("2.-------Resultado-------")
    print("3.----Reiniciar juego----")
    print("4.----Finalizar juego----")
 
    print("----Elije una opción----")
 
    opcion = pedirNum()
 
    if opcion == 1:
        print("Jugar")
    elif opcion ==2:
        print("Resultado")
    elif opcion ==3:
        print("Reiniciar juego")
    elif opcion ==4:
        salir = True
    else:
        print("Introduce una opcion entre 1 y 4.")
 
print("Fin")
    