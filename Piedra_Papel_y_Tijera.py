from ast import Break
import random

while True:
     
    aleatorio = random.randrange(0,3)
    elijePc = ""
    
    opcion = int(input("Digita 1 para elejir Piedra, 2 para elejir Papel o 3 para elejir Tijera, ¿Cual elijes?: "))

    if opcion == 1:
        elijeUsuario = "piedra"
    elif opcion == 2:
        elijeUsuario = "papel"
    elif opcion == 3:
        elijeUsuario = "tijera"
    print("Tu elijes: ", elijeUsuario)

    if aleatorio == 0:
        elijePc = "piedra"
    elif aleatorio == 1:
        elijePc = "papel"
    elif aleatorio == 2:
        elijePc = "tijera"
    print("PC elijio: ", elijePc)
    print("...")
    if elijePc == "piedra" and elijeUsuario == "papel":
        print("Ganaste, Porque el papel envulve a la piedra")
    elif elijePc == "papel" and elijeUsuario == "tijera":
        print("Ganaste, Porque La Tijera corta al papel")
    elif elijePc == "tijera" and elijeUsuario == "piedra":
        print("Ganaste, Porque La Piedra rompe a la tijera")
    if elijePc == "papel" and elijeUsuario == "piedra":
        print("perdiste, papel envulve piedra")
    elif elijePc == "tijera" and elijeUsuario == "papel":
        print("Perdiste, Porque la Tijera corta al Papel")
    elif elijePc == "piedra" and elijeUsuario == "tijera":
        print("Perdiste, Porque la Piedra rompe a la Tijera")
    elif elijePc == elijeUsuario:
        print("empate")
    seguirjugando = input("Si quieres seguir jugando digita S  ")
    if seguirjugando.lower() != "s":
      break