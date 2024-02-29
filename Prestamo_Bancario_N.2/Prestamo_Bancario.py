#Programa para saber si se le permite aceder a un prestamo bancario

#entrada
Salario = int(input("cuanto es su salario : "))
Deuda = input("usted tiene otra deuda que no ha pagado (si o no) : ")

#proceso y salida
if Salario >= 945200:
    if Deuda == "no":
        print("su prestamo ha sido aprobado")
else:
    print("su prestamo ha sido denegado")


