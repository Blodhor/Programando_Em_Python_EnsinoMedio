'''Para gerar gráficos precisamos de uma biblioteca
específica. Caso você esteja usando aplicativos como o
Google Colab Notebook, todas as bibliotecas já estão instaladas.

Se estiver programando localmente (sem internet), precisara instalar.
Recomendo instalar o Pip (https://pypi.org/). No Visual Studio Code
da Microsoft ele é instalado como extensão; no Pydroid de aparelhos
Android ele já vem preparado.

Com o pip ou algum gerenciador do seu aplicativo instale as bibliotecas:
    matplotlib
    numpy
'''

#Para utilizar as bibliotecas precisamos chama-las
# abaixo uso "chame a biblioteca numpy, e usaremos ela aqui com o nome 'np'"
import numpy as np
import matplotlib.pyplot as plt

#Utilizaremos o exemplo de "Fundamentos2" como função
def Posicao_MUV(s0,v0,a):
    return lambda t: s0 + v0*t + (a/2)* t**2

def Grafico(f=Posicao_MUV(0,1,1),pontos=5,eixox='Tempo (s)',eixoy='Altura (m)',delta=0.5,linha=False):
    '''
    f:      função que utilizaremos
    pontos: quantidade de pontos que queremos no gráfico
    eixox:  nome no eixo x
    eixoy:  nome no eixo y
    delta:  diferença de pontos consecutivos no eixo x
    linha:
        se True, constrói o gráfico com uma linha ligando os pontos (fica incorreto com poucos pontos)
        se False, constrói o gráfico com pontos apenas
    '''
    #Precisamos criar a interface com os eixos, para 
    # isso chamamos o método figure
    fig = plt.figure(dpi=150) #dpi é a qualidade desejada onde 100 é razoavel e 300 é muito alta

    #Para colocar nossa função no gráfico, basta gerar uma lista de pontos
    '''Caso f = x**2, precisa-se de alguns valores como:
        se x=-2, f= 4
        se x=-1, f= 1
        se x=0, f= 0
        se x=1, f= 1
        se x=2, f= 4
        Assim teremos as listas:
        x=[-2,-1,0,1,2] e y=[4,1,0,1,4]
    '''
    #nossa função será a dada como 'f'
    # Aqui assumimos por conveniência que só importa os
    #  valores positivos do eixo x
    #Podemos criar uma lista com o seguinte comando
    x=[delta*i for i in range(pontos)]
    '''se usar '0.5*i for i in range(4)':
    i assumiria os valores de 0, 1,2,3 então ficariamos com
    x=[0, 0.5, 1.0, 1.5]'''
    y=[]
    for i in x:
        #para todos os valores de x, queremos os valores de y
        y.append(f(i))

    #Para deixar o gráfico mais fácil de ler, daremos nomes aos eixos
    plt.ylabel(eixoy, fontsize=12) # fontzise é o tamanho da letra nas legendas
    plt.xlabel(eixox, fontsize=12) 
    plt.grid(True)# isso pede para desenhar a grade nos eixos # não é necessário de ter

    # com as listas de x e y pasta coloca-las no grafico
    if linha:
        plt.plot(x,y)
    else:
        plt.plot(x,y,'o') #'o' indica que é para mostrar pontos no gráfico
    plt.show() # sem esse comando, dependendo de onde você programa, não mostrará o gráfico

# Lembre que acima apenas definimos os métodos, não pedimos
#  para o código fazer nada

#Dica: Quando queremos que os comandos abaixo executem apenas
#      quando executamos esse arquivo usamos o bloco __main__

if __name__ == "__main__":
    # Definindo a função como: s = 50 -(g/2)* t**2, g=10 m/s**2
    s = Posicao_MUV(50,0,-10)
    # Chamamos a criação do gráfico com 11 pontos a cada 0.3 segundos
    Grafico(f=s,pontos=11,delta=0.3)
    # Caso queira ver quando a altura zera: 
    #Grafico(f=s,pontos=317,delta=0.01,linha=True)
    '''
Atividade 1:
Um trabalhador mora a 2,4 km de distância do 
seu emprego. Ele tem que decidir entre duas 
opções de transporte para chegar ao trabalho: 
de ônibus, cuja velocidade média em sua região 
é de 18 km/h, ou de bicicleta, com a qual ele 
é capaz de desenvolver uma velocidade média de 
8 m/s. Considerando que existe um ponto de ônibus
bem em frente à sua casa e outro ponto em frente 
ao seu trabalho, e desconsiderando eventuais perdas 
de tempo na espera do ônibus, qual das opções de
meio de transporte é mais rápido? Indique com gráfico.
'''