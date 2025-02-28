#Baseado nos tutoriais de https://docs.python.org/3.11/tutorial/index.html
'''As vezes não temos muita certeza de quando um ciclo deveria terminar, para esses casos dois comandos são úteis: 'break' e 'while True' '''

while True:
    '''O 'while' mantém um ciclo enquanto a sentença dada for verdade. Porém, ‘True’ sempre assume o valor 'verdade', logo o ciclo continua indefinidamente'''
    x=int(input("Informe um número inteiro: "))

    '''Em ciclos indefinidos, usamos uma verificação dentro do ciclo para decidir se paramos ele'''
    if x%3==0:
        #ao fazer uma divisão inteira por 3, se não tiver resto, então x é múltiplo de 3
        print("Múltiplo de 3!")
        #o comando 'break' para o ciclo mais interno
        break

#####################
#DEFININDO MÉTODOS#
#####################

'''Muitas vezes existe alguma sequência de comandos que se repete várias vezes no nosso código. Para evitar o trabalho tedioso de repetir tudo, podemos definir métodos com o comando def'''

fib=[0,1] # primeiros números da sequência de Fibonacci
    
def Fibonacci(n):
   #nomes definidos dentro de um método são apagados quando o método termina
    i=len(fib) # comece do topo da lista 
    while i<=n:
        #enquanto 'i' for menor ou igual a 'n'
        if i==len(fib): #se ‘i’ for igual ao tamanho da lista fib
            '''a posição 'i' não existe na lista. Posição começa de 0, então uma lista tamanho 2 só terá as posições 0 e 1'''
            novo=fib[-1]+fib[-2] # regra base da sequência
            fib.append(novo)
        i+=1
    # o ciclo acima, preenche a lista fib com todos os elementos anteriores a 'n'

# toda vez agora que quisermos um número da sequência, precisamos apenas chamar o método
print("Informe 3 posições da sequência de Fibonacci")
for j in range(3):
    #lembre que primeira posição tem indice 0
    p=int(input(">>"))-1
    if p>= len(fib): # a posição não existe ainda e devemos criar
        Fibonacci(p)
    print(fib[p])

'''Uma forma de definir funções matemáticas é utilizando o método 'lambda'. Abaixo definiremos a equação horária do movimento uniformemente acelerado (ex: queda livre)'''
def Posicao_MUV(s0,v0,a):
    ''' s = s0 + v0*t + (a/2)* t**2
    Esse método devolve a função 's' que depende do tempo'''
    return lambda t: s0 + v0*t + (a/2)* t**2

# Exemplo: s = 50 -(g/2)* t**2, g=10 m/s**2
s = Posicao_MUV(50,0,-10)
for i in range(4):
    '''De forma similar ao ‘%d’ para inteiros (usado nas aulas passadas), o ‘%f’ pede números reais na frase, e ‘%.1f’ significa que queremos apenas 1 casa decimal'''
    print("%.1f metros"%s(i))

'''
Atividade 3: Uma ave marinha costuma mergulharde uma altura de 20 m
 para buscar alimento no mar. Suponha que um desses mergulhos tenha sido
 feito em sentido vertical, a partir do repouso. Desprezando-se as forças
 de atrito, a ave chegará à superfície do mar em qual velocidade em km/h? 

Atividade 4:Um trem de 150 m de comprimento se desloca com velocidade escalar
 constante de 16 m/s. Esse trem atravessa 3 túneis em dias diferentes e leva 
 desde a entrada até a saída completa de cada túnel 50 s, 20 s e 90 s. Quanto 
 é o comprimento de cada túnel?

'''
