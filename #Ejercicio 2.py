#Ejercicio 2

#Se pide a un usuario que ingrese su edad. si la edad es mayor de 18, el programa debe calcular la diferencia entre su edad y 25: 
#si la edad es 18 o menos, debe calcular el resultado de la edad multiplicada por 2. 
#si un usuario ingresa la edad de 16, ¿Cual sera el valor del resultado final?.

edad=int(input("Ingrese su edad:"))

if(edad > 18):
    calculo=(edad - 25)
    print("El calculo de diferencia entre su edad y 25 es igual a:" , calculo)
else:
    (edad == 18 and edad < 18)
    calculo=(edad * 2)
    print("El calculo de Multiplicar su edad y 2 es igual a:" , calculo)