
'''Para gerar gráficos precisamos de uma biblioteca específica. Caso você esteja usando aplicativos como o Google Colab Notebook, todas as bibliotecas já estão instaladas. Se estiver programando localmente (sem internet), precisara instalar as bibliotecas necessárias.

Recomendo instalar o Pip (https://pypi.org/). No Visual Studio Code da Microsoft ele é instalado como extensão; no Pydroid de aparelhos Android ele já vem preparado.

Com o pip ou algum gerenciador do seu aplicativo instale as bibliotecas:  matplotlib e numpy.
'''

'''Para utilizar as bibliotecas precisamos chama-las. Abaixo uso o comando que chama a biblioteca numpy, e usaremos ela aqui com o nome 'np’. De modo similar chamamos de ‘plt’ a biblioteca genérica de gráficos'''
import numpy as np
import matplotlib.pyplot as plt

#Montaremos aqui o gráfico de uma onda periodica
def Onda(amplitude,frequencia,fase):
    return lambda x: amplitude * np.sin(2*np.pi * frequencia*x +fase)
'''Lembrete: Frequência = velocidade/cp ; cp=comprimento de onda | fase apenas indica de onde "começa" a onda'''

def Grafico(f=Onda(1,1,0), pontos=5, eixox='X (m)', eixoy='Y (m)', delta=0.5, linha=False):
    '''Parâmetros: (f) função que utilizaremos; (pontos) quantidade de pontos no gráfico; (eixox) nome no eixo x; (eixoy) nome no eixo y; (delta) espaçamento entre pontos consecutivos no eixo x; (linha) se 'True', constrói o gráfico com uma linha ligando os pontos (fica incorreto com poucos pontos)| se 'False', constrói o gráfico com pontos apenas'''
    '''Precisamos criar a interface com os eixos, para isso chamamos o método figure'''
    fig = plt.figure(dpi=150)
    '''O 'dpi' é a qualidade desejada onde 100 é razoavel e 300 é muito alta. Para colocar nossa função no gráfico, basta gerar uma lista de pontos. Caso f = x**2, precisa-se de alguns valores como: se x=-2, f= 4| se x=-1, f= 1| se x=0, f= 0| se x=1, f= 1; Assim teremos as listas: x=[-2,-1,0,1] e y=[4,1,0,1]. A nossa função aqui será a dada por 'f'. Aqui assumimos por conveniência que só importa os valores positivos do eixo x (tempo). Podemos, então, criar uma lista com o seguinte comando'''
    x=[delta*i for i in range(pontos)]
    '''Se usar '0.5*i for i in range(4)' i assumiria os valores de 0,1,2,3 então ficariamos com a lista [0, 0.5, 1.0, 1.5]'''
    y=[]
    for i in x:
       #para todos os valores de x, queremos os valores de y
        y.append(f(i))

    #Para deixar o gráfico mais fácil de ler, daremos nomes aos eixos
    plt.ylabel(eixoy, fontsize=12) 
    # fontzise é o tamanho da letra nas legendas
    plt.xlabel(eixox, fontsize=12) 
    plt.grid(True)
    #O grid pede para desenhar a grade nos eixos
    if linha:
        plt.plot(x,y)
    else:
        plt.plot(x,y,'o')
        #'o' indica que é para mostrar pontos no gráfico
    plt.show() 
    ''' Sem o comando show, dependendo de onde você programa, não mostrará o gráfico. Lembre que acima apenas definimos os métodos e não pedimos para o código fazer de fato o gráfico. Dica: Quando queremos que os comandos abaixo executem apenas quando executamos esse arquivo usamos o bloco __main__'''

def Grafico_multionda(ondas=[], referencia = Onda(1,1,0),  pontos=5, eixox='X (m)', eixoy='Y (m)', delta=0.5, linha=False):
    '''Generalização do método Grafico para aceitar várias condas no mesmo gráfico'''
    if type(ondas) == type(referencia):
        '''O método recebeu só uma onda. Repetição do código Grafico'''
        Grafico(f=ondas, pontos=pontos, eixox=eixox, eixoy=eixoy,delta=delta,linha=linha)
    else:
        fig = plt.figure(dpi=150)
        if type(ondas) == type([]):
            '''O método recebeu uma lista, então, serão mais de uma função de onda no mesmo gráfico. Aqui faremos o mesmo que no caso acima, porém devemos verificar cada membro da lista para garantir que todos são funções.'''
            
            '''Sequência de cores para diferenciar as ondas: blue(b), green(g), red(r), cyan(c), magenta(m), yellow(y), black(k)'''
            cores =['b','r','g','c','m','y','k']
            indice_cor=0
            nomes_ondas = ['uva','maçã','pera','melão','manga','abacaxi','banana']
            for i in ondas:
                if type(i)!= type(referencia):
                    print(i, "Não é do tipo Onda!")
                    return 404
                
                x=[delta*p for p in range(pontos)]
                y=[]
                for j in x:
                    #para todos os valores de x, queremos os valores y da onda 'i'
                    y.append(i(j)) 
                if linha:
                    plt.plot(x,y,color=cores[indice_cor],label="onda %s"%nomes_ondas[indice_cor])
                else:
                    plt.plot(x,y,'o',color=cores[indice_cor],label="onda %s"%nomes_ondas[indice_cor])
                indice_cor +=1
                if indice_cor == len(cores):
                    indice_cor = 0
            #para a legenda aparecer no topo esquerdo #é opcional nomear as ondas
            plt.legend(loc="upper left") 
            plt.grid(True)
        else:
            #não é uma função de onda ou uma lista de ondas
            print(ondas, "Não é do tipo Onda ou uma lista de Ondas!")
            return 404
          
    plt.xlabel(eixox, fontsize=12)
    plt.ylabel(eixoy, fontsize=12)
    plt.show()

if __name__ == "__main__":
    # Definindo a função como: sen(2*pi*x)
    o1 = Onda(1,1,0)
    # Chamamos a criação do gráfico com 11 pontos a cada 0.3 m
    #Grafico(f=o1,pontos=11,delta=0.3)
    '''Com poucos pontos fica ilegível, então aumentamos os pontos e diminuimos o espaçamento'''
    #Grafico(f=o1,pontos=300,delta=0.01,linha=True)
    o2 = Onda(1,0.5,0)
    Grafico_multionda(ondas=[o1,o2],pontos=400,delta=0.01,linha=True)
    '''Atividade 5: A partir das definições da Aula 4 e dada a onda o=Onda(1.2,0.25,np.pi/2), qual é o comprimento de onda
 e sua velocidade de propagação?'''
