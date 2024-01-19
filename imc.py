peso= float(input("Ingrese su peso:  "))
altura = float(input("Ingrese su altura:  "))
edad= int(input("Ingrese su edad:  "))
import math
imc = peso / (altura **2)

if edad < 45 and imc <22.0:
    print(f"{imc} : Bajo")
elif edad >= 45 and imc <22.0:
    print(f"{imc} : Medio")
elif edad < 45 and imc >= 22.0:
    print(f"{imc} : Medio")
elif edad >= 45 and imc >=22.0:
    print(f"{imc} : Alto")