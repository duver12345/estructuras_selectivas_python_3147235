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
=>Para el caso de prestacion de servicios 
Se debe solicitar:
- El valor del contrato
- El numero de meses del contrato
- La antiguedad del empleado (años)
El salario neto en este caso se calcula
1 - Hay que dividir el valor de contrato 
  por el numero de meses (salario mensual)
2 - Restar el 15% del salario mensual,
    por concepto de EPS (Salud)
3 - Restar el 10% del salario mensual,
    por concepto de pension 
4 - Si el empleado tiene una antiguedad igual o superior a 10 año:
    tendra una bonificacion del 0,5% sobre el salario mensual

=> Para el caso de contrato a termino indefinido
Se debe solicitar:
  - Antiguedad (años)
  - Grado o escalafon (1 - 5)
  El salario neto se calcula deacuerdo 
  a la siguiente tabla:
  - grado 1: 1.5 SM
  - grado 2: 1.7 SM
  - grado 3: 2.0 SM
  - grado 4: 2.5 SM
  - grado 5: 3.0 SM
  La bonificacion estara acorde a 
  Los siguientes rangos segun la antiguedad:
  - Entre 1 y 5 años: 1% del salario mensual
  - Entre 6 y 10 años: 2%
  - Superior a los 10 años: 3%
Para  esta caso,los descuentos de ley son:
- 25% por concepto de EPS
- 22%  por concepto de pension
- 0.1% por concepto ARL 
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
    valor_contrato = float(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese el numero de meses del contrato: "))
    antiguedad = int(input("Ingrese la antiguedad del empleado (años): "))
    salario_mensual = valor_contrato / numero_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.05 
    salario_neto = salario_mensual - eps - pension 
    if antiguedad >= 10:
        salario_neto = salario_neto + bonificacion

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