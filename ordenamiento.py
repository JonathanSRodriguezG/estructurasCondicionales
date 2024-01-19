lista = []
n = int(input("Ingrese la cantidad de numeros que desea ordenar: "))
for i in range(n):
    lista.append(input(f"Ingrese el dato numero {i+1}: "))

lista.sort()
print("Lista ordemada: ", lista)
