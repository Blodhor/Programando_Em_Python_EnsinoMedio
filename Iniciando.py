#Baseado nos tutoriais de https://docs.python.org/3.11/tutorial/index.html
#
##########
#Opcional#
##########
# Abra em um terminal o modo interativo ou utilize o jupyter notebook

##########
# NÚMEROS#
##########

#Podemos utilizar o python como uma calculadora simples
# Fora do notebook/ou modo interativo, precisamos imprimir na tela
#  os resultados, para isso o comando 'print'
print(5+5)  #soma
print(5-2)  #subtração
print(5*6)  #multiplicação
print(8/2)  #divisão #sempre devolve não inteiro
print(2**3) #potencia

# Divisão inteira # a vírgula no print indica
#  separação por espaço
print(int(5/2), 5//2)
# resto de divisão inteira
print(5%2)

#podemos associar nomes a qualquer valor,
#  usando o sinal =
#  e trabalhar com os nomes
largura= 20
altura= 45
print(largura*altura)

########
#FRASES#
########

# Podemos definir uma frase usando aspas
e1='ovos mexidos'
e2='vai descer'
print(e1, e2)
# o símbolo \n numa frase força a mudança de linha
print(e1, '\n', e2)
# o uso de \ força símbolos especiais para dentro da frase
# sem erros
print('para \'bc\'...')

''' para escrever frases ou comentarios no codigo
 com mais de uma linha, usamos 3 aspas 
'''
print(""" aspas dupla 
também é aceita""")

#Podemos usar operações para repetir padrões em uma frase
# e também podemos juntar 2 frases distintas
f1= 2*"vai descer, "
f2= "...música maldita"
print(f1+f2)
#podemos selecionar um símbolo específico de
#  uma frase a partir da contagem de caracteres
#  lembrando que toda contagem em python começa
#  em 0, 1, 2 ...
print(f2[3])
#utilizando contadores negativos, é feito 
# a procura da direita(último) para esquerda(primeiro)
print(f2[-2]) # não faz sentido -0, então começa de -1

#podemos também selecionar frases menores
print(f2[3:])#posição 4 até o fim
print(f2[3:10])#posição 4 até antes da 10 (de 4 a 9)
print(f2[3:-2])#posição 4 até antes da penultima

#não podemos alterar frases diretamente, 
# mas usando operações podemos gerar novas
# frases a partir da original
print('uia '+f2[3:6])
# ao invés de contar, podemos pedir o tamanho
#  das frases diretamente
print(len('caneta azul'))

########
#LISTAS#
########

quadrados= [0,1,4,9,16]
#de forma parecida com frases, podemos
#  selecionar elementos de listas, juntar listas
#  e pedir seu tamanho
print(quadrados[2], len(quadrados))
print(quadrados[1:3] + [25])
#porém, diferente de frases, podemos mudar valores 
# das listas diretamente
quadrados[1]=0
print(quadrados)
#não precisamos manter elementos de mesmo tipo
#  em uma mesma lista
quadrados[2]="erro"
print(quadrados)
#podemos adicionar elementos na última 
# posição da lista (diferente de juntar listas)
l1=[0,1,2]
l2=[3,4,5]
l3=l1+l2
print(l3)
l1.append(3//2) # modificou a lista l1
l1.append(4*3)
l1.append(5**2)
print(l1)

#podemos, se necessário, dar vários nomes 
# para uma mesma coisa
l5=l1
# o simbolo == verifica se dois objetos
# são iguais
#  'id' devolve o endereço de memoria
#   que o objeto foi guardado
print(l5 == l1, id(l5)==id(l1))