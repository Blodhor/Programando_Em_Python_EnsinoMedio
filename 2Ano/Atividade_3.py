'''Atividade_3_2ano: Quando jogamos uma pedra em um lago de
águas calmas, são produzidas ondas periódicas que per-
correm 5 m em 10 s.
Sendo a distância entre duas cristas sucessivas igual a
40 cm, teremos que a frequência e a velocidade de pro-
pagação dessas ondas são, respectivamente, iguais a?
'''
from Aula_3 import Periodo, Frequencia

# A velocidade de propagação foi dada como 5m/10s
v = 5/10 #m/s
# A distância de duas cristas sucessivas é o comprimento de onda
cp = 0.4 #m
p = Periodo(v)
freq = Frequencia(p(cp))

print("%.2f Hz e %.2f m/s"%(freq,v))
