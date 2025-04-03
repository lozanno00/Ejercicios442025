def determinnate(martriz):
    if len(martriz)!=3 or len(martriz[0])!=3:
        print("la matriz debera de ser una matriz 3x3")

    a,b,c = martriz[0]
    d,e,f = martriz[1]
    g,h,i = martriz[2]

matriz_3x3 = [
    [1,2,3],
    [3,7,2],
    [3,8,2]
]
solucion = determinnate(matriz_3x3)
print(solucion)