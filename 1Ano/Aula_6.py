# Baseado no tuotrial de https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html
import sympy as sp

'''O sympy foi criado para resolver cálculos matemáticos exatos, sem aproximações. Exemplo: a raiz de 8'''
# o método padrão por potencia aproxima
print(8**0.5)
# o sympy apenas simplifica
print(sp.sqrt(8))

'''Podemos também escrever expressões matemáticas definindo as variáveis x e y, não precisamos mais associar valores específicos a x e y'''
x, y = sp.symbols('x y')
f = x + 2*y
print(f)
# podemos alterar as expressões
print(f +1 -x)

'''Algumas operações não são feitas automaticamente, pois a função heurística do sympy pode determinar que a expressão como está, já é sua formar simplificada. Exemplo: x*(x+2*y) = x**2 + 2*x*y'''
f2 = x* f
print(f2)
print("Expandindo", sp.expand(f2))
'''De modo inverso podemos ter originalmente uma expressão como x**2 + 2*x*y, e  fatora-la para obter a nossa f2'''
print("Fatorando", sp.factor(x**2 + 2*x*y))

#Resolvendo equações
eq1 = x**2 -2
sol1 = sp.solve(eq1, x) #O solve iguala eq1 a zero e isola o 'x'
''' x**2 -2 = 0  -> x? '''
sol2 = sp.solve(f2,y) # resolva em 'y'
print("Eq:", eq1, "= 0, solução em x:",sol1)
print("Eq:", f2, "= 0, solução em y:",sol2)

# podemos substituir uma variavel da equação por um valor específico
f2s= f2.subs(y, -8/x) # faça y= -8/x
print("Eq:", f2s, "= 0, solução:",sp.solve(f2s,x))

'''Não precisamos resolver as equações sempre igualando-as a zero. Também conseguimos resolver com outra igualdade. Por exemplo, pedir a eq: x**2 -16= 9, e resolver em x. Para isso usamos o comando Eq que iguala duas expressões.'''
f2s9 = sp.Eq(f2s, 9) # faz f2s = 9
print("Eq:", sp.expand(f2s9), "solução:",sp.solve(f2s9,x))

'''Finalmente, podemos determinar a solução de um sistema de equações. Por exemplo {x-2*y=0, x+y=18}'''
se1 = x-2*y
se2 = sp.Eq(x+y, 18)
print("Resolvendo o sistema:\n(1)", se1,"= 0")
print("(2)",se2)
'''Usando o comando linsolve, passamos uma lista de equações e enseguida a lista de variáveis que queremos encontrar como (x,y), A solução será entregue na ordem pedida, nesse caso, primeiro x e depois y'''
solsis=sp.linsolve([se1,se2], (x,y))
print("(x , y) =",solsis)
'''Se tivermos alguma equação não linear no sistema (potência maior que 1), ex: x**2 = 10, precisamos usar o método sp.nonlinsolve()'''
solsis2 = sp.nonlinsolve([x**2-2*y, sp.Eq(6*x+y,-18)], (x,y))
print("Solução do sistema não linear:", solsis2)

'''
Atividade 8:Um pequeno motor a pilha é utilizado para
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

Atividade 9: Um bloco escorrega, livre de resistência do
ar, sobre um plano inclinado de 30° conforme a figura
(sem escala) a seguir.

No trecho AB não existe atrito e no trecho BC o coefi-
ciente de atrito vale mu = sqrt(3)/2. O bloco é abandonado,
do repouso em relação ao plano inclinado, no ponto A e chega
ao ponto C com velocidade nula. A altura do ponto A, em 
relação ao ponto B, é h1, e a altura do ponto B, em relação
ao ponto C, é h2. Quanto vale a razão h1/h2?
'''
