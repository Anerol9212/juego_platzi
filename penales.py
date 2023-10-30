import os
import random
import time

eleccion_jugador = 0
eleccion_computadora = 0
puntos_jugador = 0
puntos_computadora = 0

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def pintar_pantalla():
    print(              f"   Jugador {puntos_jugador} - Computadora {puntos_computadora}    ")

    print(" -----------------------------------------------------------------------------")
    print("|                                  |                                         |")
    print("|                                  |                           --------------|")
    print("|                                  |                           |             |")
    print("|                                  |                           |             |")
    print("|                                  |                           |             |")
    print("|                                  |                           |             |")
    print("|                                  |                           |             |")
    print("|                                  |                           |             |")
    print("|                                  |                           --------------|")
    print("|                                  |                                         |")
    print("|__________________________________|_________________________________________|")

def pantalla_gol():
     print(                 f"Jugador {puntos_jugador} - Computadora {puntos_computadora} ")

     print(" -----------------------------------------------------------------------------")
     print("|                                  |                                         |")
     print("|                                  |                           --------------|")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                        ¡GOOOOOOOOOOOOOOOOOOOOL!              |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           --------------|")
     print("|                                  |                                         |")
     print("|__________________________________|_________________________________________|")

def victoria():   
     print("                            MARCADOR FINAL                                    ")
     print(              f"   Jugador {puntos_jugador} - Computadora {puntos_computadora}    ")
     print(" -----------------------------------------------------------------------------")
     print("|                                  |                                         |")
     print("|                                  |                           --------------|")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                            ¡HAZ GANADO!                      |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           --------------|")
     print("|                                  |                                         |")
     print("|__________________________________|_________________________________________|")

def perdiste():   
     print("                            MARCADOR FINAL                                    ")
     print(              f"   Jugador {puntos_jugador} - Computadora {puntos_computadora}    ")
     print(" -----------------------------------------------------------------------------")
     print("|                                  |                                         |")
     print("|                                  |                           --------------|")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                            ¡HAZ PERDIDO!                     |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           |             |")
     print("|                                  |                           --------------|")
     print("|                                  |                                         |")
     print("|__________________________________|_________________________________________|")

'''Derecha = 1, izquierda = 2, centro = 0'''

print("********************************************")
print("**************           *******************")
print("**************  PENALES  *******************")
print("**************           *******************")
print("********************************************")

seleccion = input("Ingrese 1 para iniciar: ")
if seleccion == "1":
    clear()
    pintar_pantalla()  

    while(puntos_jugador < 5 and puntos_computadora < 5):
        print("Presione la tecla elegida: ")
        print("1 :tirar a la Izquierda, 2: Tirar al centro y 3: Tirar a la derecha.")
        eleccion = input("Elección: ")
   
        if eleccion == '1':
            eleccion_jugador = 1
            print("Elegiste DERECHA")
        elif eleccion == '2':
            eleccion_jugador = 2
            print("Elegiste CENTRO")
        elif eleccion == '3':
            eleccion_jugador = 3
            print("Elegiste IZQUIERDA")
        else: 
            print("Elige una opción valida")
            continue

        eleccion_computadora = random.randint(1, 3)
        if(eleccion_computadora == 1):
         print(f"La computadora eligio: DERECHA")
        elif(eleccion_computadora == 2):
            print(f"La computadora eligio: CENTRO")
        elif(eleccion_computadora == 3):
            print(f"La computadora eligio: IZQUIERDA")
        if (int(eleccion_computadora) == int(eleccion_jugador)):
            print("El portero ha detenido el tiro.")
            puntos_computadora += 1
            time.sleep(1)
            clear()
            pintar_pantalla()
        else:           
            puntos_jugador += 1
            time.sleep(1)
            clear()
            pantalla_gol()
            time.sleep(1)
            clear()
            pintar_pantalla()       

    if(puntos_computadora < puntos_jugador):
        time.sleep(1)
        clear()
        victoria()
    else:
        time.sleep(1)
        clear()
        perdiste()       
else:
    print("Opcion no valida.")
        
