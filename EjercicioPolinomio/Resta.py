def Resta(p1,p2):
    while len(p1)<len(p2):
        p1.insert(0,0)
    while len(p2)>len(p1):
        p2.insert(0,0)

    return [coef1-coef2 for coef1, coef2 in zip(p1,p1)]

p1=[1,2,3] #Seria X^2+2X+3
p2=[4,5,6] #Seria 4X^2+5X+6
print(Resta(p1,p2))

    