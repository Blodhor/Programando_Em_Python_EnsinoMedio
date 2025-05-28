'''Atividade: Em uma brincadeira de caça ao tesouro, o mapa diz que para chegar
 ao local onde a arca de ouro está enterrada, deve-se, primeiramente, dar 10
 passos na direção norte, depois 12 passos para o leste, em seguida, 7 passos
 para o sul, e finalmente 8 passos para oeste.
A partir dessas informações:
    (a) Desenhe em um gráfico a trajetória descrita no mapa usando vetores
    (b) Se um caçador caminhasse em linha reta, desde o ponto de partida
    até o ponto de chegada, quantos passos ele daria?'''

#Para isso usaremos os métodos já prontos de Vetores.py
from Aula_5 import Vetor2D, Mostre_vetor

# Para conectar a trajetória
# o 'pe' do próximo vetor será a 'ponta' do anterior
# a 'ponta' do novo vetor será seu mais o novo deslocamento
#começo = (0,0)
# norte = somando em Y;  sul = subtraindo em Y
# leste = somando em X; oeste= subtraindo em X
norte = (0,10) # 10 passos ao norte
leste= (12,10) # 12 passos a leste
sul = (12,3)# 7 passos ao sul
oeste=(4,3) # 8 passos a oeste

a=Vetor2D(norte,nome='10 passos N')
b=Vetor2D(pe=norte,ponta=leste,nome="12 passos L")
c=Vetor2D(pe=leste,ponta=sul,nome='7 passos S')
d=Vetor2D(pe=sul,ponta=oeste,nome='8 passos O')

# resposta do item (a)
#Mostre_vetor(vetores=[a,b,c,d])

# Para responder (b) basta somar
e = a+b+c+d
#nomearemos e com seu tamanho
tam = e.tamanho()
e.nome=str(tam)+" passos"
Mostre_vetor(vetores=[a,b,c,d,e])
