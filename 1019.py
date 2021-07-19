#Djalma Felipe
#27/08/2020
#sistemas_de_informação
#unifacisa

segundos = int(input())

#calculos
horas = int(segundos / 3600)
resto = segundos % 3600
minutos = int(resto / 60)
segundos = int(resto % 60)

#saida

print(str(horas) + ':' + str(minutos) + ':' + str(segundos))
