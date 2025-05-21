def tablero(matriz):
    for fila in matriz:
        print(" ".join(str(celda) for celda in fila))
    print()

def vecinos(fila, col, matriz):
    vecinos = 0
    filas = len(matriz)
    columnas = len(matriz[0])
    if col - 1 >= 0:
        vecinos += matriz[fila][col - 1]
    if col + 1 < columnas:
        vecinos += matriz[fila][col + 1]
    return vecinos
def generacion(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    nueva_matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            vecinos = vecinos(i, j, matriz)

            if matriz[i][j] == 1:
                if vecinos == 1 or vecinos == 2:
                    nueva_matriz[i][j] = 1
                else:
                    nueva_matriz[i][j] = 0
            else:
                if vecinos == 1:
                    nueva_matriz[i][j] = 1
                else:
                    nueva_matriz[i][j] = 0 

    return nueva_matriz
matriz = [
    [0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
]


print("Generación 0:")
tablero(matriz)

generacion1 = generacion(matriz)
print("Generación 1:")
tablero(generacion1)

generacion2 = generacion(generacion1)
print("Generación 2:")
tablero(generacion2)
