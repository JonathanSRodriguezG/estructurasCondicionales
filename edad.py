from time import localtime
t = localtime()
t.tm_mday
18
t.tm_mon
1
t.tm_year
2024

meshoy= t.tm_mon
diahoy= t.tm_mday
añohoy= t.tm_year

año = int(input("En que año nacio?:    ")) 
mes = int(input("En que mes nacio?:    ")) 
dia = int(input("En que día nacio?:    ")) 


edad= añohoy - año

if meshoy < mes or (meshoy == mes and diahoy < dia):
    edad = edad - 1

print(f"Usted tiene {edad} años.")