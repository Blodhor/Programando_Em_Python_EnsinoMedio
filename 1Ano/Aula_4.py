
'''Para gerar gráficos precisamos de uma biblioteca específica. Caso você esteja usando aplicativos como o Google Colab Notebook, todas as bibliotecas já estão instaladas. Se estiver programando localmente (sem internet), precisara instalar as bibliotecas necessárias.

Recomendo instalar o Pip (https://pypi.org/). No Visual Studio Code da Microsoft ele é instalado como extensão; no Pydroid de aparelhos Android ele já vem preparado.

Com o pip ou algum gerenciador do seu aplicativo instale as bibliotecas:  matplotlib e numpy.
'''

'''Para utilizar as bibliotecas precisamos chama-las. Abaixo uso o comando que chama a biblioteca numpy, e usaremos ela aqui com o nome 'np’. De modo similar chamamos de ‘plt’ a biblioteca genérica de gráficos'''
import numpy as np
import matplotlib.pyplot as plt

#Métodos para MUV
def Posicao_MUV(s0,v0,a):
    return lambda t: s0 + v0*t + (a/2)* t**2

def Grafico(f=Posicao_MUV(0,1,1), pontos=5, eixox='Tempo (s)', eixoy='Altura (m)', delta=0.5, linha=False):
    '''
    f:        função que utilizaremos
    pontos: quantidade de pontos no gráfico
    eixox:  nome no eixo x
    eixoy:  nome no eixo y
    delta:  espaçamento entre pontos consecutivos no eixo x
    linha:
     +se True, constrói o gráfico com uma linha ligando os pontos (fica incorreto com poucos pontos)
     +se False, constrói o gráfico com pontos apenas'''
    #Precisamos criar a interface com os eixos
    # para isso chamamos o método figure
    fig = plt.figure(dpi=150)
    '''O dpi é a qualidade desejada onde 100 é razoavel e 300 é muito alta. Para colocar nossa função no gráfico, basta gerar uma lista de pontos. Caso f = x**2, precisa-se de alguns valores como:
       se x=-2, f= 4
        se x=-1, f= 1
        se x=0, f= 0
        se x=1, f= 1
        se x=2, f= 4
Assim teremos as listas: x=[-2,-1,0,1,2] e y=[4,1,0,1,4];
A nossa função será a dada como 'f'. Aqui assumimos por conveniência que só importa os valores positivos do eixo x (tempo). Podemos criar uma lista com o seguinte comando'''
    x=[delta*i for i in range(pontos)]
    '''Se usar '0.5*i for i in range(4)' i assumiria os valores de 0,1,2,3 então ficariamos com a lista [0, 0.5, 1.0, 1.5]'''
    y=[]
    for i in x:
       #para todos os valores de x, queremos os valores de y
        y.append(f(i))

    #Para deixar o gráfico mais fácil de ler, daremos nomes aos eixos
    plt.ylabel(eixoy, fontsize=12) # fontzise é o tamanho da letra nas legendas
    plt.xlabel(eixox, fontsize=12) 
    plt.grid(True)
    # grid pede para desenhar a grade nos eixos, mas não é necessário de ter
    # com as listas de x e y pasta coloca-las no gráfico
    if linha:
        plt.plot(x,y)
    else:
        plt.plot(x,y,'o') #'o' indica que é para mostrar pontos no gráfico
    plt.show() 
    ''' Sem o comando show, dependendo de onde você programa, não mostrará o gráfico. Lembre que acima apenas definimos os métodos e não pedimos para o código fazer de fato o gráfico. Dica: Quando queremos que os comandos abaixo executem apenas quando executamos esse arquivo usamos o bloco __main__'''

'''Métodos para MCU: ds = R*theta; x=R*cos theta; y=R*sin theta'''
def xy_MCU(R):
    x = lambda theta: R*np.cos(theta)
    y = lambda theta: R*np.sin(theta)
    return (x, y)

def radiano(x):
    return x*2*np.pi/360

def graus(x):
    return x*360/(2*np.pi)

def Grafico_circulo(raio=1,mostre_theta=np.pi/4, pontos=360, eixox='X (m)', eixoy='Y (m)', delta=1,grade=False):
    #funções de X e Y
    f=xy_MCU(raio)
    if pontos<100:
        pontos+=100
    fig = plt.figure(dpi=100)
    X, Y =[], []
    for i in range(pontos):
        X.append(f[0]( radiano(i) ))
        Y.append(f[1]( radiano(i) ))
    plt.ylabel(eixoy, fontsize=12)
    plt.xlabel(eixox, fontsize=12)
    plt.grid(grade)
    plt.plot(X,Y)
    #mostranto o raio no ângulo escolhido
    o = [0], [0]
    p = [raio*np.cos(mostre_theta)], [raio*np.sin(mostre_theta)] 
    plt.quiver(*o,*p,angles='xy', scale_units='xy',scale=1,color='k',label='Raio=%.1f\nÂngulo=%.1f'%(raio,graus(mostre_theta)))
    plt.legend(loc="upper left")        
    plt.show()

if __name__ == "__main__":
    # MUV
    #s = Posicao_MUV(0,15,-10)
    #Grafico(f=s,pontos=300,delta=0.01,linha=True)
    #MCU
    Grafico_circulo(raio=2,grade=True)    
    
    '''Atividade 5-MUV: Um trabalhador mora a 2,4 km de distância do 
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

Atividade 5-MCU: Considere uma polia girando em torno de
seu eixo central, conforme figura abaixo. A velocidade
dos pontos A e B são, respectivamente, 60 cm/s e 0,3 m/s.
A distância AB vale 10 cm. O diâmetro e a velocidade
angular da polia, respectivamente, valem:
'''
