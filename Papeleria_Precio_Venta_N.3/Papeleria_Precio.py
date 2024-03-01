import math
#Programa para calcular el precio de venta de diferentes productos en una papeleria

#entrada
PRECIO_COSTO = int(input("porfavor ingrese el precio en el que se adquirio el producto : "))

#proceso

if PRECIO_COSTO < 3000:
    GANANCIA = PRECIO_COSTO *0.15
elif PRECIO_COSTO > 6000:
    GANANCIA = PRECIO_COSTO*0.25
else:
    GANANCIA = 500
    
PRECIO_VENTA = (GANANCIA + PRECIO_COSTO)
#Salida
print ("el producto adquirido se debe vender a",PRECIO_VENTA,)