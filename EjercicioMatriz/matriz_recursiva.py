def determinnate(matriz):
    det = 0
    for i in range(len(matriz)):
        sub_matriz = [row[:i] + row[i+1:] for row in matriz[1:]]
        det += ((-1) ** i) * matriz[0][i] * determinnate(sub_matriz)

    return det

matriz=[
    [1,2,3],
    [3,7,2],
    [3,8,2]
]
solucion= determinnate(matriz)
print(solucion)