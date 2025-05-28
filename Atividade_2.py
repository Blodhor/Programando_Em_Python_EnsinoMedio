'''Atividade:
Faça uma código que peça um número inteiro e
nos diz se o número é par ou ímpar.
'''
n=int(input("Informe um número inteiro: "))

if n % 2 ==0:
    #se o resto da divisão por 2 for zero é par
    print("%d é par"%n) # com %d podemos colocar números inteiros em frases
else:
    # se não é par, é ímpar
    print("%d é impar"%n)