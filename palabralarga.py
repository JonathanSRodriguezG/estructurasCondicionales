palabra1 = input("Ingrese una palabra:  ")
palabra2 = input("Ingrese una segunda palabra:  ") 

letras1 = len(palabra1)
letras2 = len (palabra2)
diferencia = abs(letras1-letras2)

if letras1 > letras2:
    print(f"La palabra {palabra1} tiene {diferencia} letras más que {palabra2}")
elif letras2 > letras1:
    print(f"La palabra {palabra2} tiene {diferencia} letras más que {palabra1}")
if letras1 == letras2: 
    print("Ambas palabras tienen las mismas letras") 

