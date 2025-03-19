'''
if en cascada:
es una estructura selectiva 
compuesta por condicionales,
 seguidos unos de otros
 sintaxis:
 if condicional1:
    instruccion1
    instruccion2

elif condicional2:
    instruccion3
    instruccion4

elif condicional3:
    instruccion5
    instruccion6

NOTA: cada condicional es mutuamente excliyente
'''
#Ejemplo
#Vamos a hacer un pequeño traductor
#Traductor
#El programa debe permitir leer una fruta en español
#y debe mostrar esa fruta en ingles

fruta_es = input("Ingrese fruta: ")

if fruta_es=="manzana" or fruta_es=="Manzana":
        print("Apple")

elif fruta_es=="naranja" or fruta_es=="Naranja":
    print("orange")

elif fruta_es=="uva" or fruta_es=="Uva":
    print("grape")

elif fruta_es=="piña" or fruta_es=="Piña":
    print("pineapple")

#caso por defecto 
#default

else:
     print("No se encontro la traduccion de esa fruta")
