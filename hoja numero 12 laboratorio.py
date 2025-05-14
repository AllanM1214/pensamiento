dias = ("lunes", "martes", "miercoles", "jueves", "viernes")
niveles_azucar = [130, 160, 95, 175, 160] 
NIVELES_SAL = [2000, 2400, 1800, 2400, 2700]
presion = [115, 130, 110, 125, 175]
suma_azucar = 0
suma_sal = 0
suma_presion = 0
def nivelazucar(nivel):
    if 70 <= nivel <= 140:
        print ("nivel de azucar normal")
    else:
        print ("nivel de azucar alto")

def nivelsal(nivel):
    if nivel <= 2300:
        print ("nivel de sal normal")
    else:
        print ("nivel de sal alto")        

def nivel_de_presion(sistolica):
    if sistolica < 120:
        print("Presion Normal")
    elif 120 <= sistolica <= 129:
        print ("Presion Elevada")
    elif 130 <= sistolica <= 139:
        print ("Hipertensin Etapa 1")
    else:
        print ("Hipertension Etapa 2")

print("Resultados")
for i in range(len(dias)):
    print(f"\nDia: {dias[i]}")
    
    azucar = niveles_azucar[i]
    sal = NIVELES_SAL[i]
    presion = presion[i]

    resultado_azucar = nivelazucar(azucar)
    resultado_sal = nivelsal(sal)
    clasificacion_presion = nivel_de_presion(presion)

    print(f"Nivel de azucar: {azucar} mg/dL - {resultado_azucar}")
    print(f"Consumo de sal: {sal} mg - {resultado_sal}")
    print(f"Presion sistolica: {presion} mmHg - {clasificacion_presion}")

    suma_azucar += azucar
    suma_sal += sal
    suma_presion += presion

promedio_azucar = suma_azucar / len(dias)
promedio_sal = suma_sal / len(dias)
promedio_presion = suma_presion / len(dias)

print("\nPromedios Semanales")
print(f"Promedio de azucar en sangre: {promedio_azucar:.2f} mg/dL - {azucar(promedio_azucar)}")
print(f"Promedio de consumo de sal: {promedio_sal:.2f} mg - {sal(promedio_sal)}")
print(f"Promedio de presion sistolica: {promedio_presion:.2f} mmHg - {nivel_de_presion(promedio_presion)}")