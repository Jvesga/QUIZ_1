#Ejercicio_1

#En un programa de tienda, el precio de un producto es de 10. si la cantidad comprada es mayor o igual a 5, se aplica un descuento del 20%.
#si la cantidad es menor a 5 pero mayor a 2, se aplica un descuento del 10%. 
#en cualquier otro caso, no hay descuento. ¿Cual es el precio final si se compran 4 unidades del producto?.

cantidad_comprada=int(input("Inserte la cantidad de productos que desea llevar el cliente:"))


if(cantidad_comprada >= 5 ):
    valor_total=int(cantidad_comprada * 10)
    valor_con_descuento=(valor_total * 0.80)


    print("El descuento aplicado a su compra es del 20%")
    print("El valor total de su compra es de:" , valor_con_descuento)



elif(cantidad_comprada < 5 and cantidad_comprada > 2):
    valor_total2=int(cantidad_comprada * 10)
    valor_con_descuento2=(valor_total2 * 0.10)
   

    print("El descuento aplicado a su compra es del 10%")
    print("El valor total de su compra es de:" , valor_con_descuento2)


else:
    valor_total=int(cantidad_comprada * 10)
    print("Para la cantidad solicitada no se aplica descuento de ningun tipo")
    print("El valor total de su compra es de:" , valor_total)