'''Atividade feita em sala com professor:
Uma barra delgada está em uma temperatura 
na qual o seu comprimento é igual L0=100 cm. 
A barra, de coeficiente de dilatação linear 
8,0*10**(-5) °C**(-1) é, então, colocada a 
uma distância d=0,8 m do vértice de um espelho 
curvo (o objeto esta do lado da superfície convexa do espelho "obj C imagem").
O espelho possui um raio de curvatura de 
160 cm. Para se fazer a imagem crescer 0,5 cm, 
pode-se:
(a) aproximar a barra 10 cm
(b) afastar a barra 5 cm
(c) aquecer a barrra em 125 °C (afirmativa correta)

Atividade 7: Resolva o problema feito em sala,
 porém, considerando que a temperatura não mude,
 quanto que a posição da barra vai mudar?
'''
from sympy import*

def Problema2_mudanca_p(L0,alfa,d_obj,raio):
    '''Nessa situação: obj ( imagem ; a imagem é virtual, logo pl<0 e a imagem é direita
     Tanto o foco quanto o raio são negativos'''
    f, p, pl, i, o, dL, dT = symbols('f p pl i o dL dT')
    gauss = Eq(1/f, 1/p + 1/pl)
    aumento = Eq(i/o, -pl/p)
    dilatacao = Eq(dL, L0*alfa*dT)
    '''Para espelhos esféricos de Gauss, a distância focal f é a metade do raio de curvatura CV'''
    g1 = gauss.subs(f,-abs(raio/2))
    g2 = g1.subs(p, d_obj)

    distancia_imagem = solve(g2,pl)[0]
    # encontra pl=-40cm
    # diferente do problema1, vamos substituir o tamanho primeiro
    a1 = aumento.subs(o,L0)
    a2= a1.subs(pl,distancia_imagem)
    a3= a2.subs(p, d_obj)
    altura_imagem = solve(a3, i)[0]
    #imagem cresce 0.5cm
    nova_altura = altura_imagem+0.5
    '''Se for o caso da temperatura ficar constante, o quanto as distâncias p e pl mudarão?'''
    # o/(i+0.5)= (-p/pl)  - eq1
    a4 = a1.subs(i,nova_altura)
    # 1/f = 1/p + 1/pl - eq2 (g1) incognitas p, pl
    ppl_novo = nonlinsolve([g1,a4],(p,pl))
    return ppl_novo

resp = Problema2_mudanca_p(100,8*10**(-5),80,160)
#resp recebe duas respostas, vou usar a segunda
data = str(resp)[10:-2].split(',')
for i in range(len(data)):
    data[i]= round(float(data[i]),2)
print("As novas distâncias serão:\n p=%.2f cm; p\'=%.2f cm"%(data[0],data[1]))