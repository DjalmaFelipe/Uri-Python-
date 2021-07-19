#Djalma Felipe
#27/08/2020
#sistemas_de_informação
#unifacisa

#entrada
fragmentos = input().split()
A = int(fragmentos[0])
B = int(fragmentos[1])
C = int(fragmentos[2])

#calculo
MAIOR_AB = ((A+B)+abs(A-B))/2
MAIOR = int(((MAIOR_AB+C)+abs(MAIOR_AB-C))/2)

#apresentação
print(str(MAIOR) + ' eh o maior')
