idade = int(input("Digite sua idade: "))
if idade > 60: 
    print("Idoso")
elif idade > 18: 
    print("Adulto")
elif idade > 12: 
    print("Adolescente")
elif idade < 12: 
    print("Criança")
else:
    print ("erro")