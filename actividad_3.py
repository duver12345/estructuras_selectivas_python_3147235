'''
actividad 3
Elabore un programa que permita
calcular el salario neto de un empleado
despues de descontar 
descuentos por conceptos de salud,pension,ARL

1.El problema debe solicitar 
  el tipo de empleado:
  a - contrato a termino indefinido
  b - contraro por prestacion de servicios 
  c - contrato de Aprendizaje
  d - contrato por Jornal(Freelance)
=>Pata el caso del jornal
Se debe solicitar:
- Numero de horas trabajadas
- Valor de la hora
*El total del salario se calcula de multiplicar
el numero de horas por el valor a pagar por hora

'''
contrato = input("Ingrese el tipo de contrato: ")
#Inicializar variables:
# dar valor inicial a una variable
# asi no se utilice en el momento
salario_neto = 0
if contrato == "a":
    print ("Eligio:Contrato a termino indefinido")
elif contrato == "b":
    print ("Eligio:Contrato por prestacion de servicios")
elif contrato == "c":
    print ("Eligio:Contrato de Aprendizaje")
    salario_minimo = int(input("Ingrese el valor del salario minimo:"))
    salario_neto = salario_minimo - (salario_minimo * 0.25)

elif contrato == "d":
    print ("Eligio:Contrato por Jornal(Freelance)")
    #Variable local
    #Variable que solo se utiliza 
    #en un bloque de codigo
    numero_horas = int(input("Ingrese el numero de horas trabajadas: "))
    valor_hora = int(input("Ingrese el valor de la hora: "))
    salario_neto = numero_horas * valor_hora
else:
    print ("El tipo de contrato no es valido")
print ("El salario neto es: " , salario_neto)
print("Fin del programa")