
# Un programa para calcular el costo de agua por m3 

# Input

GASTO = int(input("Digite el gasto de agua en su vivienda: "))
PRECIO = 10000
# Processing

if GASTO <= 50:
    PRECIO = 10000
elif GASTO < 200:
    PRECIO = 2000+10000
else:
    PRECIO = 3000+10000

# Output 

print ("El dinero a pagar por el gasto del agua es: ",PRECIO,)