print ("bem vindo")
a= float (input("diga o tamanho do primeiro lado"))
b= float (input (" diga o segundo lado"))
c= float (input ("diga o terceiro lado"))
if (a+b<c) or (a+b<c) or (b+ c <a):
 print (" não é um triangulo")
elif(a==b) and (a==c):
 print ("equilatero")
elif (a==b) or (a==c) or (b==c):
 print ("isósceles")
elif (a!=b) and (a!=c) and (b!=c):
    print ("escaleno")
else:
    print ("erro")