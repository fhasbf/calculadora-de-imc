nota = float (input ("digite sua  nota"))

#9-1 0: A (Excelente)
#7-8: B (Bom)
# 5-6 : R (Regular)
#Abaixo de 5: F (Reprovado)

if nota < 4.9 : 
    print ("F (REPROVADO)")
elif 5 <= nota < 6.9 :
    print ("R (regular)")
elif 7 <= nota < 8.9 :
    print ("B (bom)")
elif 9 <= nota <= 10:
    print ("A (excelente)")
else:
    print ("erro")