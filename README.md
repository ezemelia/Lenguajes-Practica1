# Práctica 1 - Lenguajes 2025

### Ezequiel Melía

## Ejecución del programa
_(Se asume que ya se tiene instalado Python 3.X)_
1. Abrir consola
2. Dirigirse a la ruta donde se ubica el archivo **piedra_papel_tijerav2.py**
3. Ejecutar: `python piedra_papel_tijerav2.py`

## Qué hace el programa
- Se simula una partida de "Piedra, Papel o Tijera" entre el usuario y la computadora.
- La cantidad máxima de rondas que se jugarán se define en la variable `rondas_maximas`.
- Se juega "al mejor de X rondas". Si un jugador ya no puede alcanzar al otro en puntos, la partida finaliza.\
Esta situación se da si la diferencia de puntos entre ambos jugadores es mayor que la cantidad de rondas que quedan por jugarse.
- Las rondas empatadas se cuentan.
- Si el usuario ingresa una opción inválida se le solicita un nuevo ingreso, sin contar la ronda.

