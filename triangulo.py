def triangulo(A ,B ,C):
    if A+B > C and A+C> B and B+C >A:
      if A == B == C:
       return "Triangulo Equilatero"
      elif A == B or A == C or B==C:
       return "Triangulo Isoceles"
      else:
       return "Triangulo Escaleno"
    else: 
      return "Triangulo inválido"

Lado1 = float(input("Ingrese la longitud del primer lado:    ")) 
Lado2 = float(input("Ingrese la longitud del segundo lado:    ")) 
Lado3 = float(input("Ingrese la longitud del tercer lado:    ")) 

resultado = triangulo(Lado1,Lado2,Lado3)
print(resultado)