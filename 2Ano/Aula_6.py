from sympy import*

'''Atividade em sala (com professor): Uma barra delgada está em uma temperatura na qual o seu comprimento é igual L0=100 cm. A barra, de coeficiente de dilatação linear 8,0*10**(-5) °C**(-1) é, então, colocada a uma distância d=0,8 m do vértice de um espelho curvo (o objeto está do lado da superfície convexa do espelho "obj C imagem"). O espelho possui um raio de curvatura de 160 cm. Para se fazer a imagem crescer 0,5 cm, pode-se: (a) aproximar a barra 10 cm; (b) afastar a barra 5 cm; ou (c) aquecer a barra em 125 °C'''

def Problema1_mudanca_temperatura(L0,alfa,d_obj,raio):
    '''Nessa situação: | obj ( imagem | A imagem é virtual, logo pl<0 e a imagem é direita. Tanto o foco quanto o raio são negativos'''
    f, p, pl, i, o, dL, dT = symbols('f p pl i o dL dT')
    gauss = Eq(1/f, 1/p + 1/pl)
    aumento = Eq(i/o, -pl/p)
    dilatacao = Eq(dL, L0*alfa*dT)
    '''Para espelhos esféricos de Gauss, a distância focal f é a metade do raio de curvatura CV'''
    g1 = gauss.subs(f,-abs(raio/2))
    g2 = g1.subs(p, d_obj)
    '''O 'solve' devolve uma lista de soluções para cada variável pedida. Como só pedi 'pl' ele devolve uma lista de 1 elemento, assim, usando [0] eu retiro o elemento.'''
    distancia_imagem = solve(g2,pl)[0]
    #devolve -40 cm no problema exemplo
    a1 = aumento.subs(p, d_obj)
    a2= a1.subs(pl,distancia_imagem)
    # modificar 'o' por último nos permite reutilizar a2 posteriormente
    a3= a2.subs(o,L0)
    altura_imagem = solve(a3, i)[0]
    #imagem cresce 0.5cm
    nova_altura = altura_imagem+0.5
    '''Se for o caso das distâncias p e pl permanecerem iguais então quanto L0 precisa aumentar? Teremos a equação: novo_o = (i+0.5)*(-p/pl)'''
    a4 = a2.subs(i,nova_altura)
    novo_o = solve(a4,o)[0]
    # dL = novo_o -L0 = L0*alfa*dT  
    eq_dil = dilatacao.subs(dL,novo_o-L0)
    variacao_temp = solve(eq_dil, dT)[0]
    return "A temperatura da barra precisou variar em %.2f °C"%variacao_temp

resp = Problema1_mudanca_temperatura(100,8*10**(-5),80,160)
print(resp)

'''Atividade 7: Resolva o problema feito em sala,
 porém, considerando que a temperatura não mude,
 quanto que a posição da barra vai mudar?
'''
