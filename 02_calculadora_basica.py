num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        resultado = None
        print("Error: no se puede dividir entre 0.")
    else:
        resultado = num1 / num2
else:
    resultado = None
    print("Operación no válida.")

if resultado is not None:
    print(f"Resultado: {round(resultado, 2)}")
