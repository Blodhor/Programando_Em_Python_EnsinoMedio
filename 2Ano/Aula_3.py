#Baseado nos tutoriais de https://docs.python.org/3.11/tutorial/index.html
# Continuando de Aula_3_base

'''Uma forma de definir funções matemáticas é utilizando o método 'lambda'. Abaixo definiremos a velocidade de propagação de um pulso transversal em uma corda homogênea'''
def Velocidade_prop_corda(den):
    ''' v = (T/den)**0.5
    T == Tração na corda | den == desnsidade linear da corda
    Devolve a função da velocidade em relação a Tração.'''
    return lambda T: (T/den)**0.5
def Densidade_linear(massa,comprimento):
    return massa/comprimento

'''Para ondas periódicas, a velocidade de propagação é constante e podemos determinar a frequência e período da onda'''
def Periodo(velocidade):
    '''Devolve o Período em função do comprimento de onda (chamaremos de cp)'''
    return lambda cp: (cp/velocidade)
def Frequencia(periodo):
    return 1/periodo

if __name__=="__main__":
    #Exemplo:
    '''A velocidade de propagação v de um pulso transversal numa corda depende da força de tração T com que a corda é esticada e de sua densidade linear d (v==(T/d)**0.5). Um cabo de aço, com 2,0 m de comprimento e 200 g de massa, é esticado com força de tração de 40 N. A velocidade de propagação de um pulso nesse cabo é, em m/s,'''
    d = Densidade_linear(0.2, 2) # 0.2kg; 2m
    vel = Velocidade_prop_corda(d)
    #Para uma tração de 40N temos
    print(vel(40), "m/s")

    '''
Atividade_3_2ano: Quando jogamos uma pedra em um lago de
águas calmas, são produzidas ondas periódicas que per-
correm 5 m em 10 s.
Sendo a distância entre duas cristas sucessivas igual a
40 cm, teremos que a frequência e a velocidade de pro-
pagação dessas ondas são, respectivamente, iguais a?

Considerando que ao usar espelhos planos, a distância da imagem ao espelho é igual a distância do espelho ao objeto.
Atividade_4_2ano: Um barbeiro B segura um espelho plano E2,
de espessura desprezível, paralelamente a outro espelho plano E1,
também de espessura desprezível, permitindo que seu cliente A observer, no espelho E1,
o seu corte de cabelo na parte posterior da cabeça.

Esquema:
B|--|E2|--|A|--|E1 
Distância E2_A: 0.6 m | Distância A_E1: 1 m

Determine a menor distância entre o cliente e a imagem
que ele observa da sua nuca no espelho E1, considerando
que a cabeça do cliente também possui dimensões desprezíveis.
'''
