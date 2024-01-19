caracter = input("Ingrese un caracter:  ")

if caracter.isalpha():
    if caracter.isupper():
        print(f"{caracter} es una letra mayuscula.")
    elif caracter.islower():
        print(f"{caracter} es una letra minuscula.")
elif caracter.isdigit():
        print(f"{caracter} es un numero.")
else:
     print(f"{caracter} no es letra ni numero.")

