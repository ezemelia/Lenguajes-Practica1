import random

opciones = ["piedra", "papel", "tijera"]

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")

print("Escribí tu jugada (piedra/papel/tijera).")

ronda = 1

puntos_usuario = 0

puntos_pc = 0

rondas_maximas = 7

diferencia_de_puntos = 0

rondas_que_quedan = rondas_maximas - ronda

while (ronda <= rondas_maximas) and (diferencia_de_puntos <= rondas_que_quedan):
    print(f"\nRonda {ronda}")
    jugada_usuario = input("Tu jugada: ").strip().lower()
    if jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera.")
        continue

    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")
    if jugada_usuario == jugada_pc:
        print("Empate.")
    elif (
            (jugada_usuario == "piedra" and jugada_pc == "tijera") or
            (jugada_usuario == "papel" and jugada_pc == "piedra") or
            (jugada_usuario == "tijera" and jugada_pc == "papel")
        ):
            print("¡Ganaste la ronda!")
            puntos_usuario += 1
    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
    print("\n=== Resultado final ===")
    print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

    diferencia_de_puntos = abs(puntos_pc - puntos_usuario)
    rondas_que_quedan = rondas_maximas - ronda

    ronda += 1

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")
elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")
else:
    print("Empate total.")