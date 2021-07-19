#DjalmaFelipe
#04/set/2020
#unifacisa
#Sistemas de informação

fragmentos = input().split()

A = int(fragmentos [0])
B = int(fragmentos [1])
C = int(fragmentos [2])
D = int(fragmentos [3])

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0 :
    print('Valores aceitos')
else :
    print('Valores nao aceitos')
