'''
if anidados:
if dentro de otro if
syntax:
if condicion:
     print("Instruccion")
else:
     print("Instruccion")

No confundir el elif (if en cascada)
'''
#Ejemplo 1:
#Modifique el ejercisio de la edad para las siguientes condiciones
#1.Si es mayor de 18 años 
#pero no tiene documento no puede votar
#de lo contrario si puede votar
#2. Si es menor de 18 años no puede votar
#Utilize estructura de if anidados

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    documento = input("¿Tiene documento de identidad? (Si/No): ")
    if documento == "Si":
        print("Puede votar")
    else:
        print("No puede votar")
else:
    print("No puede votar")