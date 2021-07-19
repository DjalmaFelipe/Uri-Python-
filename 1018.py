#Djalma Felipe
#28/ago/2020
#unifacisa
#Sistemas de informação

#entrada
valor = int(input())

#calculo
notas_100 = int(valor/100)
resto = valor % 100
notas_50 = int(resto / 50)
resto = resto % 50
notas_20 = int(resto/20)
resto = resto % 20
notas_10 = int(Rest/10)
resto = resto % 10
notas_5 = int(rest/5)
resto = resto % 5
notas_2 = int(Rest/2)
resto = resto % 2
notas_1 = int(resto/1)


#exibição
print(valor)
print(str(notas_100) + ' nota(s) de R$ 100,00') 
print(str(notas_50) + ' nota(s) de R$ 50,00') 
print(str(notas_20) + ' nota(s) de R$ 20,00') 
print(str(notas_10) + ' nota(s) de R$ 10,00') 
print(str(notas_5) + ' nota(s) de R$ 5,00') 
print(str(notas_2) + ' nota(s) de R$ 2,00')
print(str(notas_1) + ' nota(s) de R$ 1,00')
