("bem vindo vamos calcular o seu desconto")
preco= float (input ("insira o preço que deseja calcular o desconto"))
desconto = float   (input ("insira o desconto que recebeu"))
# vd = valor do desconto
vd = (preco * desconto / 100)
#pf = preco final
pf = ( preco - vd )

print ("seu preço com desconto ficou por", pf)