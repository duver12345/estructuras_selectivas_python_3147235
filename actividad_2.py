edad = int(input("¿Cual es su edad?: "))
estrato = int(input("cual es su estrato? (1-2): "))
valor = int(input("¿Cual es el valor de su matricula? :"))

if edad < 18 and estrato == 1:
    print("Su descuento sera del 20%")
    valorfinal = valor * 0.2
    valortotal = valor - valorfinal
    print ("El descuento de su matricula sera de: ",valorfinal)
    print ("El total de la matricula con descuento es de: ",valortotal )

elif edad > 18 and estrato == 1:
    print ("Su descuento sera del 15%")
    valorfinal = valor * 0.15
    valortotal = valor - valorfinal
    print ("El descuento de su matricula sera de: ",valorfinal)
    print ("El total de la matricula con descuento es de: ",valortotal )

elif edad < 18 and estrato == 2:
    print ("Su descuento sera del 10%")
    valorfinal = valor * 0.10
    valortotal = valor - valorfinal
    print ("El descuento de su matricula sera de: ",valorfinal)
    print ("El total de la matricula con descuento es de: ",valortotal )

elif edad == 18 and estrato == 2:
    print ("Su descuento sera del 5%")
    valorfinal = valor * 0.05
    valortotal =  valor - valorfinal
    print ("El descuento de su matricula sera de: ",valorfinal)
    print ("El total de la matricula con descuento es de: ",valortotal )


else :
    print("No aplica para el descuento")