num1 = int(input("Ingrese el dividendo:  "))
num2 = int(input("Ingrese el divisor:  ")) 
division = num1 / num2
if division % 2 == 0:
    print("La division es exacta")
else:
    print("La división es inexacta")

cociente= num1 // num2
print(f"Cociente: {cociente}")

resto= num1 % num2
print(f"Resto: {resto}")

