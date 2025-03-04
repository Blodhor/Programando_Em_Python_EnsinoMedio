# Baseado no tuotrial de https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html
import sympy as sp

'''O sympy foi criado para resolver cálculos matemáticos exatos, sem aproximações. Exemplo: a raiz de 8; O método padrão por potencia aproxima o valor'''
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
sol1 = sp.solve(eq1, x)
'''O solve iguala eq1 a zero e isola o 'x'. Nesse caso: x**2 -2 = 0  -> quanto é x? '''
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
Considerando a Equação de Gauss(Espelhos Esféricos):
1/f = 1/p + 1/p' ;
f é a distância focal
p é a distância entre o objeto e o vértice
p' é a distância entre a imagem e o vértice

E a relação de aumento linear:
A = i/o  ;  i/o = -p'/p
i é o tamanho da imagem
o é o tamanho do objeto

Atividade 6: Considere um objeto luminoso colocado
sobre o eixo principal de um espelho esférico côncavo.
Sabendo que a distância focal do espelho é 30 cm, que
a distância do objeto ao espelho é 90 cm e que a altura
do objeto é 6,0 cm, calcule a distância da imagem ao
espelho e a altura da imagem, ambas em centímetros.
'''
