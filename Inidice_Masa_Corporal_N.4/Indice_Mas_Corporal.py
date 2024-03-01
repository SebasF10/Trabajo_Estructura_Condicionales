#programa para saber deacuerdo a tu estatura y tu peso tu estado de salus deacuerdo al IMC

# input
PESO= int(input("porfavor ingrese su peso : "))
ALTURA = float(input("porfavor ingrese su altura : "))

# processing
IMC = PESO/ALTURA**2

if IMC < 16:
    RESULTADO ="criterio de ingreso en hospital"
elif IMC <= 17:
    RESULTADO = "infrapeso" 
elif IMC <= 18.5:
    RESULTADO = "bajo peso"
elif IMC <= 25:
    RESULTADO = "peso normal (saludable)"
elif IMC <= 30:
    RESULTADO = "sobrepeso(obesidad de grado I)"
elif IMC <= 35:
    RESULTADO = "sobrepeso crónico(obesidad de grado II)"
elif IMC <= 40:
    RESULTADO = "obesidad premórbida(obesidad de grado III)"
elif IMC > 40:
    RESULTADO = "obesidad mórbida(obesidad de grado IV)"

# output

print("si IMC es",IMC,"y sus resultados son",RESULTADO,)