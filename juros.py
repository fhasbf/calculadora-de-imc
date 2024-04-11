print  ("bem vindo, vamos calcular os juros")
valor = float (input ("digite o valor da divida"))
juros = float (input ("digite a taxa de juros"))
periodo = float (input ("digite o periodo que levara para quitar a divida"))
valor_total =  valor * (1 + juros) ** periodo
print ("o valor total fica em", valor_total)
