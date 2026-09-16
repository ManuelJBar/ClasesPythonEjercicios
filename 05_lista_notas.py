def calcular_promedio(lista):
    return sum(lista) / len(lista)


notas = []
for i in range(5):
    nota = float(input(f"Introduce la nota {i + 1}: "))
    notas.append(nota)

promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {round(promedio, 2)}")
print(f"La nota más alta es: {max(notas)}")
print(f"La nota más baja es: {min(notas)}")
