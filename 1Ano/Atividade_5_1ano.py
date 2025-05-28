'''
Atividade: Um trabalhador mora a 2,4 km de distância do 
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

Solução:
Precisamos construir o gráfico deslocamento vs tempo.
Como fala em velocidade média no problema, assumimos MU
A equação que utilizamos é 
    v= delta_s / delta_t
Como sabemos a distância, isolamos o tempo
    delta_t = delta_s/v
Contruiremos assim as listas
    tempo1, dist 300 m
    tempo2, dist 600 m
    ....

'''
import matplotlib.pyplot as plt

#Primeiro precisamos usar a mesma unidade para comparar 
# as velocidades, usaremos as unidades do SI
def v_kmh2ms(v):
    #transforma km/h em m/s
    return v/3.6

def tempo(v):
    return lambda s: s/v

#Faremos um único gráfico para comparar os dois 
# veículos
def graf(f1=tempo(8),f2=tempo(v_kmh2ms(18)),
         legenda1="Bicicleta", legenda2="Ônibus",
         pontos=101,delta=24,eixox='Deslocamento (m)',
         eixoy='Tempo (s)'):
    #f1 -> bicicleta
    #f2 -> onibus
    # distância = (pontos-1)*delta 
    fig = plt.figure(dpi=150) 
    
    x=[delta*i for i in range(pontos)]
    y1, y2 = [], []
    for i in x:
        y1.append(f1(i))
        y2.append(f2(i))

    plt.ylabel(eixoy, fontsize=12)
    plt.xlabel(eixox, fontsize=12) 
    
    # Para usar o mesmo gráfico, basta repetir
    #  o comando 'plot'
    plt.plot(x,y1,label=legenda1,color='red')
    plt.plot(x,y2,label=legenda2,color='blue')
    # para mostrar o ponto máximo de cada veículo
    # usamos o comando 'text(posição x do texto, posição y do texto, texto)'
    plt.text(x[-25],y1[-1],"%.1f s, %d m"%(y1[-1],x[-1]),color='red')
    plt.text(x[-25],y2[-1],"%.1f s, %d m"%(y2[-1],x[-1]),color='blue')
    plt.legend(loc="upper left") #para a legenda aparecer no topo esquerdo
    plt.grid(True)
    plt.show()

graf()