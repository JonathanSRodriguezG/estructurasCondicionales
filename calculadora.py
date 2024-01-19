numero1 = float(input("Ingrese un numero:    "))
numero2 = float(input("Ingrese otro numero:    ")) 
def calcular(operador,numero1,numero2):
    if operador == "+":
        return numero1+numero2
    elif operador == "-":
        return numero1-numero2
    elif operador =="*":
        return numero1*numero2
    elif operador =="**":
        return numero1**numero2
    elif operador =="/":
        if numero2 != 0:
            return numero1/numero2
        else: return "Error: No se puede dividir entre 0"
    else: 
        return "Error: operador no valido"
    
operador = input("Ingrese un operador ( + , - , / , * , **): ")
resultado = calcular(operador, numero1, numero2)
print("Resultado:  ", resultado)

