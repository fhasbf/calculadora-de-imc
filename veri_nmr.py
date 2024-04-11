print ("bem vindo")
numero = int (input ("digite um numero"))
if numero > 0 and numero % 2 == 0:
    print (numero, "é positivo e par")
elif numero >0 and numero % 3 == 0:
    print (numero, "é positivo e múltiplo de 3")
elif numero <0 and numero % 2 != 0:
    print (numero, "é negativo e ímpar")
elif numero == 0:
    print (numero, "é igual a zero")
else:
    print ("nenhum desses")