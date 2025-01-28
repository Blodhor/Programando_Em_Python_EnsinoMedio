#Baseado nos tutoriais de https://docs.python.org/3.11/tutorial/index.html

########
#CICLOS#
########

#Ao invés de repetir comandos
#  podemos criar ciclos de execução

a=[0]
print(a)
a.append(1)
a.append(2)
a.append(3)
print(a)

# com ciclo
b = [] # lista vazia
i=0
while i<4:
    # enquanto i for menor que 4 o ciclo executa
    b.append(i)
    print(b)
    # alterando o valor de i
    #  pois o ciclo depende de i 
    #  para acabar
    i= i +1 # novo 'i' recebe o 'i' antigo mais 1 

#com os ciclos, podemos fazer operações
#  mais complicadas automaticamente
#exemplo: para criar uma lista com
#  os 10 primeiros fatoriais
# 0!=1, 1!=1, 2!= 2*1, 3!= 3*2*1, ...

l, j =[1], 1 # dessa forma não precisamos de várias linhas
             #'l' recebe o primeiro valor '[1]'; 'j' o segundo '1';
             #  e assim por diante se tiverem mais valores 

while j <10:
    # de 0 a 9 temos 10 fatoriais
    #l[-1] é o fatorial do anterior
    l.append(j*l[-1])
    #se não alterar j, o ciclo continua para sempre
    j += 1 # abreviação de j=j+1
print(l)

# temos outro formato de ciclo que não precisa se preocupar
# em sempre mudar a variavel do ciclo

for i in ['maçã','uva','banana','melão']:
    # 'i' nesse ciclo recebe os valores da lista 
    # em sequência, o ciclo acaba após todos os valores serem usados
    print(i)

for i in [0,1,2,3,4]:
    print(i)
    
# para sequencia de numeros inteiros podemos usar 'range()'
for i in range(10):
    print(i)

print("Podemos modificar a sequência do range")
for i in range(1,10,2):
    # começa a sequência em 1, termina em 10 ou antes de 10 (respeitando o passo)
    # com passo de 2 em 2
    print(i)

###################################
#PEDINDO VALORES ANTES DE EXECUTAR#
###################################

# o comando 'input' pede uma informação de quem executa o codigo
# essa informação é recebida como um tipo frase
# se queremos um tipo número, teremos que modificar o tipo
x= input("Escolha um número inteiro: ")
print(type(x), type(5)) # comando type indica o tipo do objeto
# x terá tipo de frase ('str') e 5 de inteiro ('int')

#se uma frase for composta de apenas um numero inteiro
# podemos fazer a conversão
x=int(x) # de forma semelhante, se for um número real usamos 'float' 
print("Após a conversão ", type(x))

#############
# SE e SENÃO#
#############

# criação de blocos de código que só são acessados 
# 'se' uma regra a ser definida for obedecida
if x<0:
    print("Número negativo")
elif x>0:
    # elif pede um nova verificação, nesse caso 
    # se não for negativo, mas for positivo
    print("Número positivo")
else:
    #caso nenhuma verificação deu certo
    print("Valor nulo")

'''Atividade 1:
Faça um código que peça uma sequência de valores
e calcule a média deles.

Atividade 2:
Faça uma código que peça um número inteiro e
nos diz se o número é par ou ímpar.
'''
