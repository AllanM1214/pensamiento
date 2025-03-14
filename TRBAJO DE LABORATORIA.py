#1 COSTO DE AGUA
habitantes=int(input("ingrese el numero de habitantes en su hogar: "))
consumo=float(input("ingrese el consumo de agua en su hogar: "))
if consumo < 15:
    tarifa = 5
elif consumo <= 30:
    if habitantes > 30:
        tarifa = 4
    elif habitantes == 3:
        tarifa = 4.5
    else:
        tarifa = 5
total= consumo*tarifa
print ("el costo del agua es de: Q",total)
#2 PLACAS DE CARRO
modelo = int(input("Ingrese el modelo del carro: "))
placa = input("Ingrese la placa del carro: ")
if modelo >= 2001:
        ultimo_digito = int(placa[-1])  # Último dígito de la placa
        if ultimo_digito in [0, 2, 4, 6, 8]:
            restriccion = "NO circula los lunes."
        else:
            restriccion = "NO circula los viernes."

        if modelo % 2 == 0:
            restriccion += " Además, los sábados solo circula hasta el mediodía."
elif 2025 - modelo > 25:  # Más de 25 años de antigüedad
        restriccion = "Advertencia: mantenimiento obligatorio."
else:
        restriccion = "No tiene restricciones."
        print (restriccion)                    