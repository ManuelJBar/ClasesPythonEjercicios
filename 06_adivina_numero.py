import random

numero_secreto = random.randint(1, 100)
intentos = 0
numero_usuario = None

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Adivina el número (1-100): "))
    intentos += 1

    if numero_usuario < numero_secreto:
        print("El número secreto es mayor.")
    elif numero_usuario > numero_secreto:
        print("El número secreto es menor.")
    else:
        print(f"¡Enhorabuena! Has acertado en {intentos} intentos.")
