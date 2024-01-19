JuegosA = int(input("Juegos ganados por A:    ")) 
JuegosB = int(input("Juegos ganados por B:    ")) 

diferencia=abs(JuegosA-JuegosB)

if JuegosA == 6 and JuegosB < 5:
    print("Jugador A ha ganado el set")
elif JuegosB == 6 and JuegosA < 5:
    print("Jugador B ha ganado el set")
elif JuegosA == 7 and JuegosB  in [5, 6]:
    print("Jugador A ha ganado el set")
elif JuegosB == 7 and JuegosA in [5, 6]:
    print("Jugador B ha ganado el set")
elif JuegosA == 6 and JuegosB == 6:
    print("El set todavía no termina, se juega un último juego")
elif JuegosA >= 8 or JuegosB >= 8 or diferencia > 3:
    print("Resultado no valido")
elif JuegosA ==7 and JuegosB ==7:
    print("Resultado no valido")
else:
    print("El set aun no termina")