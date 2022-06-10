# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#numero = [ 25,65,85,12]
#for edad in numero:
 #   print(edad)


#for i in range(len(numero)):
   #(numero[i])
#numero.sort()
#print(numero)


#append: agregar un elemento a la lista 
#lista.count(numero):cuenta la veces que se repite el elemento 
#index: Indicas el elemento dentro de la lista y devuelve su posicion 
#inset: Inserta el elemento x en la lista , en el indice i 
#pop: 

#prueba=[20,41,6,18,41,23]
#print(prueba.index(41,0))

total_compra= int(input("importe_a_pagar")) 
if total_compra >100:
    tasa_descuento = 10
    importe_descuento = total_compra * tasa_descuento/100
    importe_a_pagar = total_compra-importe_descuento
    print(importe_a_pagar)
else:
    print(total_compra)