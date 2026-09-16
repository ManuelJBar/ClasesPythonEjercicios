"""
Ejercicio 6: Adivina el número
----------------------------------
1. Genera un número secreto aleatorio entre 1 y 100 (módulo random).
2. Usa un bucle while para que el usuario vaya intentando adivinarlo.
3. En cada intento, dile si el número secreto es "mayor" o "menor"
   que el que ha introducido.
4. Cuando acierte, felicítale y muestra cuántos intentos ha necesitado.

Pistas:
- import random
- random.randint(1, 100) genera un entero aleatorio entre 1 y 100.
- Usa una variable "intentos" que sumes 1 en cada vuelta del bucle.
- El bucle termina cuando el número introducido == número secreto.
"""

import random

numero_secreto = None  # TODO: genera el número aleatorio
intentos = 0

# TODO: bucle while que pida números hasta acertar
