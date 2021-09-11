import random

# Set de las opciones del Cachipún para el coputador
opciones = ["Piedra", "Papel", "Tijeras"]
npc = random.choice(opciones)

# Opción del Jugador
player = (input('¿Piedra, Papel o Tijeras?\n'))

# Pensamos en que el jugador sólo ingrese lo de la lista
if player.capitalize() not in(opciones):
    print('Debes usar las Jugadas Listadas')
    print('Game Over!')
else:
    print(f'\nEl computador eligió {npc}...\n')
    # Empezamos a probar los casos del juego
    if (player == npc):
        print('Empatados....\n')
        print('Fin del juego')
    else:
        if ( player=='Piedra' and npc=='Tijeras') or ( player=='Papel' and npc=='Piedra') or ( player=='Tijeras' and npc=='Papel'):
            print('Has Ganado! Felicitaciones :D \n')
            print('Fin del juego')
        else:
            print('Ding....ding....ding.... El computador Ganó')
            print('Fin del juego')
