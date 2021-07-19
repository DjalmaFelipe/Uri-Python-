fragmentos1 = input().split()
fragmentos2 = input().split()

#primeiro produto

COD_1 = int(fragmentos1[0])
NUMBER_1 = int(fragmentos1[1])
UNIT_PRICE_1 = float(fragmentos1[2])

#segundo produto

COD_2 = int(fragmentos2[0])
NUMBER_2 = int(fragmentos2[1])
UNIT_PRICE_2 = float(fragmentos2[2])

#calculos

VALUE_1 = NUMBER_1*UNIT_PRICE_1
VALUE_2 = NUMBER_2*UNIT_PRICE_2
FINAL_VALUE = VALUE_1+VALUE_2 

#apresentação

print('VALOR A PAGAR: R$ ' + "%.2F" %FINAL_VALUE)
