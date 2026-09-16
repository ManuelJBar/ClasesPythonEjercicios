numero = int(input("Introduce un número entero: "))

if numero % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"

if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

if numero == 0:
    print(f"El número {numero} es {paridad}.")
else:
    print(f"El número {numero} es {paridad} y {signo}.")
