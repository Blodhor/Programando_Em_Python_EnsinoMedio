'''Atividade 5: A partir das definições da Aula 4 e dada a onda o=Onda(1.2,0.25,np.pi/2), qual é o comprimento de onda
 e a velocidade de propagação?
 
Solução:
A velocidade de propagação obtemos ao multiplicar a frequência pelo comprimento de onda
 vel = freq * comp
O comprimento de onda conseguimos direto do gráfico de o
'''
from Aula_4 import*

o = Onda(amplitude=1.2,frequencia=0.25,fase=np.pi/2)
Grafico(o,pontos=101,delta=0.08,linha=True)

'''Vemos assim que comp = 4 m ; portanto vel = 4m * 0.25Hz = 1 m/s'''
