#Baseado nos tutoriais de https://docs.python.org/3.11/tutorial/index.html
# Continuando de Aula_3_base

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
