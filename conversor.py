print('Bem-vindo')
valor = float(input("Digite o número que deseja converter: "))
sist = int(input("Digite sua medida (1 para milhas, 2 para polegadas, 3 para pés, 4 para centímetros, 5 para metros, 6 para quilômetros): "))

if sist == 1:
    milhas = (valor)
    pes = (valor * 5280)
    polegadas =  (valor * 63360)
    centimetros = (valor * 160934.4)
    metros = (valor * 1609.34)
    quilometros = (valor * 1.60934)
    print(milhas, "milhas são equivalente a", pes, "pés,", polegadas, "polegadas,", centimetros, "centímetros,", metros, "metros e", quilometros, "quilômetros.")
    
elif sist == 2:
    polegadas = (valor)
    milhas = (valor / 63360)
    pes = (valor / 12)
    centimetros = (valor * 2.54)
    metros = (valor * 0.0254)
    quilometros = (metros / 1000)
    print( polegadas, "polegadas são equivalente a ", "milhas", milhas,  "pés,", pes,  "centímetros,", centimetros,  "metros,",metros,   "e", quilometros, "quilômetros.")

elif sist == 3:
    pes = (valor)
    milhas = (valor / 5280)
    polegadas = (valor * 12)
    centimetros = ( valor * 30.48)
    metros = (valor * 0.3048)
    quilometros = (valor * 0.3048 / 1000)
    print (pes, "pés são equivalente a", milhas, "milhas,", polegadas, "polegadas,", centimetros, "centímetros,", metros, "metros e,", quilometros, "quilometros." )

elif sist == 4:
    centimetros = (valor)
    milhas = (valor / 100 / 1000 )
    polegadas =(valor / 2.54)
    pes = (valor / 30.48)
    metros =( valor / 100)
    quilometros = ( valor  / 100000)
    print (centimetros, "centímetros são equivalente a", milhas, "milhas,", polegadas, "polegadas,", pes, "pés,", metros, "metros,", quilometros, "quilometros.")

elif sist == 5:
    metros = ( valor )
    milhas = ( valor / 1609.34)
    polegadas = (valor * 39.3701)
    pes = ( valor * 3.28084)
    centimetros = ( valor * 100)
    quilometros =( valor * 1000)
    print (metros, "metros são equivalente a", milhas, "milhas,", polegadas, "polegadas,", pes, "pés,", quilometros, "quilometros." )

elif sist == 6:
    
    quilometros = (valor)
    milhas =( valor / 1.60934)
    polegadas = (valor * 1000 * 39.3701) 
    pes = ( valor * 3280.84)
    centimetros = ( valor * 1000)
    metros = ( valor * 100)
    print (  quilometros, "quilometros é equivalentes a" , milhas, "milhas,", polegadas, "polegadas,", pes, "pes,", centimetros, "centimetros e", metros, "metros." )