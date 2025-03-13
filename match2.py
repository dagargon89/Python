#Capture un pokemon y ver su ataque de acuardo a los puntos.
while True:
    Salir = input("Salir:").lower()
    if Salir == "si":
        break
    elif Salir == "no":
        pass
    pokemon = input("Captura pokemon: ").lower()
    ataque = int(input("Captura el ataque: ")) 

    match pokemon:
            case "bulbasaur":
                print(f"El ataque de {pokemon} es: ")
                if ataque <= 49:
                    print("Placaje")
                elif ataque >= 50 and ataque <= 99:
                    print("Latigo cepa")
                elif ataque >= 100:
                    print("Rayo solar")
                else:
                    print("Semilla sanguijuela")
            case "charmander":
                print(f"El ataque de {pokemon} es: ")
                if ataque <= 49:
                    print("Arañazo")
                elif ataque >= 50 and ataque <= 99:
                    print("Ascuas")
                elif ataque >= 100:
                    print("Lanzallamas")
                else:
                    print("Garra dragon")
            case "squirtle":
                print(f"El ataque de {pokemon} es: ")
                if ataque <= 49:
                    print("Placaje")
                elif ataque >= 50 and ataque <= 99:
                    print("Pistola agua")
                elif ataque >= 100:
                    print("Hidrobomba")
                else:
                    print("Hidropulso")
            case _:
                print("Pokemon no valido")