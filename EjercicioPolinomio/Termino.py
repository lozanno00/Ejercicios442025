def eliminar_termino(p1, grado):
    if grado < len(p1):
        p1[-(grado+1)]=0
    return p1

p1=[1,2,3] #Seria X^2+2X+3
grado = 1
resultado = eliminar_termino(p1, grado)
print(resultado)
