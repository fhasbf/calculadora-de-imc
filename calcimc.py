print ("bem vindo")
print ("vamos calcular o imc")
peso = float (input ("digite seu peso"))
altura = float (input("digite sua altura"))
imc = peso / (altura ** 2 )
if imc <18.5:
    print ("voce esta abaixo do peso, seu imc é" , imc)
elif 18.5 <= imc < 24.9:
    print  ("parabéns, você está no peso ideal, seu imc é de" , imc)
elif 25 <= imc <30:
    print ("cuidado, voê está um pouco acima do peso" , imc)
elif 30.1 <= imc <35:
    print ('CUIDADO você está em obesidade nível I' , imc)
elif 35.1 <= imc <40:
    print ('PROCURE UM MÉDICO URGENTE, VOCÊ ESTÁ EM OBESIDADE NÍVEL II', imc)

