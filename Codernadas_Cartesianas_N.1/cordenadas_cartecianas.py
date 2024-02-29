#programa para calcular en que cuadrante esta un punto,de un plano cartesiano

#entrada
X = int(input("ingrese la coordenada x: "))
Y = int(input("ingrese la coordenada y: "))

#proceso
if X == 0:
    if Y == 0:
        print("esta en el origen del plano cartesiano(0,0)")
    else:
        print("estas en el eje Y")
elif Y == 0:
    print("estas en el eje X")
elif X > 0:
    if Y > 0:
        print("estas en el cuadrante 1")
    else:
        print("estas en el cuadrante 4")
elif Y < 0:
    print("estas en el cuadrante 3")
else:
    print("estas en el cuadrante 2")


