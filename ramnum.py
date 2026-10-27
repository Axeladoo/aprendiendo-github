import random
print ("iniciando juego amor...")
# Adivina el número entre 1 y 10
secreto = random.randint(1, 10)
print("¡Adivina un número del 1 al 10!")

while True:
    try:
        intento = int(input("Tu número: "))
        if intento == secreto:
            print("¡Felicidades, acertaste!")
            break
        elif intento < secreto:
            print("Es mayor...")
        else:
            print("Es menor...")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Estadística simple añadida al final
print(f"El número secreto era exactamente: {secreto}")
