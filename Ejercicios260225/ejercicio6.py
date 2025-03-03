videojuegos_mmorpg = ['World of Warcraft', 'Final Fantasy XIV', 'Guild Wars 2', 'The Elder Scrolls Online', 'Black Desert Online', 'Star Wars: The Old Republic', 'EVE Online']

# Mostrar solo los elementos en posiciones pares (0, 2, 4, 6)
print("Videojuegos MMORPG en posiciones pares:")
for indice in range(0, len(videojuegos_mmorpg), 2):
    print(f"{indice}: {videojuegos_mmorpg[indice]}")
