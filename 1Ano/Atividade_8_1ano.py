'''Atividade:Um pequeno motor a pilha é utilizado para
movimentar um carrinho de brinquedo. Um sistema de
engrenagens transforma a velocidade de rotação des-
se motor na velocidade de rotação adequada às rodas
do carrinho. Esse sistema é formado por quatro engre-
nagens, A, B, C e D, sendo que A está presa ao eixo
do motor, B e C estão presas a um segundo eixo e D a
um terceiro eixo, no qual também estão presas duas das
quatro rodas do carrinho.

Nessas condições, quando o motor girar com frequência
fM, as duas rodas do carrinho girarão com frequência fR.
Sabendo que as engrenagens A e C possuem 8 dentes,
que as engrenagens B e D possuem 24 dentes, que não
há escorregamento entre elas e que fM=13.5Hz é correto 
afirmar que fR, em Hz, é igual a

Solução:
Lembrete: r*w=v; w=2*pi*f
No caso de engrenagens ligando os dentes
va=vb, assim
ra*wa=rb*wb; ra*fa=rb*fb

fa = fm= 13.5Hz
Precisamos determinar fb, para isso precisamos das relações
de ra e rb com os dentes das engrenagens
'''
from sympy import *
def raio(dentes):
    '''n dentes no comprimento da circunferência 2*pi*r'''
    return dentes/(2*pi)

def Engrenagens(fa=13.5,ra=raio(8), rb=raio(24), rc=raio(8), rd=raio(24)):
    '''A e B ligam os dentes'''
    fb, fd = symbols('fb fd')
    f_ab = Eq(ra*fa, rb*fb)
    '''B e C estão ligados no mesmo eixo, então possuem nos mesmos parâmetros angulares'''
    #fc = fb
    '''C e D ligam os dentes, como fc=fb'''
    f_cd = Eq(rc*fb, rd*fd)
    sis = solve([f_ab,f_cd], (fb,fd))
    print(sis)

Engrenagens()