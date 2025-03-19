'''
if else:
determinar dos caminos
de ejecucion,basada en 
la evaluacion de una condicional

sintaxis:
if condicional:
   instruccion1
   instruccion2
else:
   instruccion3
   instruccion4   
'''
#Elabore un programa en python que determine 
# si una persona es mayor o menor de edad y 
# por tanto,habilitada para votar

Edad = int (input ("Ingrese su edad: "))
documento =input ("Tienes documento ?(SI/NO):")
if Edad >= 18 and documento == "SI" :
    print("Usted es mayor de edad")
    print("Puede votar")

else:
    print ("Usted  es menor de edad")
    print ("o")
    print ("No puede votar")
print("Fin de programa")