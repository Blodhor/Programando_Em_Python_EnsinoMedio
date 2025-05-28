'''Atividade 6: Considere um objeto luminoso colocado
sobre o eixo principal de um espelho esférico côncavo.
Sabendo que a distância focal do espelho é 30 cm, que
a distância do objeto ao espelho é 90 cm e que a altura
do objeto é 6,0 cm, calcule a distância da imagem ao
espelho e a altura da imagem, ambas em centímetros.

Solução:
Do enunciado temos:
f= 30 cm; p= 90 cm; o= 6cm
Aplicando a equação de Gauss obtemos a distância da imagem
que chamaremos de pl. Com pl, poderemos então utilizar a 
relação de aumento. Lembrando que o sinal negativo significa
imagem invertida.'''
from sympy import*

def Metodo(foco,d_obj,tam_o):
    f, p, pl, i, o = symbols('f p pl i o')
    gauss = Eq(1/f, 1/p + 1/pl)
    aumento = Eq(i/o, -pl/p)
    g1 = gauss.subs(f,foco)
    g2 = g1.subs(p, d_obj)
    '''O 'solve' devolve uma lista de soluções para cada
variável pedida. Como só pedi 'pl' ele devolve uma lista 
de 1 elemento, assim, usando [0] eu retiro o elemento.'''
    distancia_imagem = solve(g2,pl)[0]

    a1 = aumento.subs(o,tam_o)
    a2= a1.subs(p, d_obj)
    a3= a2.subs(pl,distancia_imagem)
    altura_imagem = solve(a3, i)[0]
    return "Distância %d cm; Altura %d cm"%(distancia_imagem,altura_imagem)

print(Metodo(30,90,6))
