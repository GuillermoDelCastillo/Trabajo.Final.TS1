import random

bolillas  =  [ ]
jugadores = [ ]
def pedirNum():
 
    incorrecto = False
    num=0
    while(not incorrecto):
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
 
    print("  ---Elije una opción---")
 
    opcion = pedirNum()
 
    if opcion == 1:
        print("Jugar")
      
        n = int(input("Ingresar el número de jugadores: "))

        i=0
        
        while i < n:
            nombre = (input("Ingrese el nombre del jugador: "))

            i+= 1
            
        seguir = False
        jugando = 0
        while (not seguir):
           
            for i in range (1):
                bolillas.append(random.randint(1, 80))
            num = int(input("Marque 1 para obtener bolilla: "))
            seguir = False

            print ("La bolilla es: ",bolillas)

       
    elif opcion ==2:
        print("Resultado")
        
    elif opcion ==3:
        print("Reiniciar juego")
    elif opcion ==4:
        salir = True
    else:
        print("Introduce una opcion entre 1 y 3.")
 
print("Fin")
    