from random import randint

dado1 = randint(1,6)
dado2 = randint(1,6)

while True:

    if dado1 == 1 and dado2 == 1:
        
        print("Ganó")
    elif dado1 == 6 and dado2 == 6:
        print("Ganó")
    elif dado1 == 1 and dado2 == 2:
        print("Ganó")
    elif dado1 == 2 and dado2 == 1:
        print("Ganó")
    elif dado1 == 1 and dado2 == 6:
        print("Ganó")
    elif dado1 == 6 and dado2 == 1:
        print("Ganó")
    elif dado1 == 2 and dado2 == 5:
        print("Ganó")
    elif dado1 == 5 and dado2 == 2:
        print("Ganó")
    elif dado1 == 3 and dado2 == 4:
        print("Ganó")
    elif dado1 == 4 and dado2 == 3:
        print("Ganó")
    elif dado1 == 5 and dado2 == 6:
        print("Ganó")
    elif dado1 == 6 and dado2 == 5:
        print("Ganó")
    else:
        print("Resultado")
    break