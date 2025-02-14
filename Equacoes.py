# Baseado no tutorial de https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html
import sympy as sp

# sympy foi feito para cálculos matemáticos exatos, sem aproximações
# Exemplo: a raiz de 8
print(8**0.5) # mostra uma aproximação
print(sp.sqrt(8)) # a raiz é simplificada e não aproximada

# Podemos também escrever expressões matemáticas
# definindo as variáveis x e y, não precisamos mais
#  associar valores a x e y
x, y = sp.symbols('x y')
f = x + 2*y
print(f)
# podemos alterar as expressões
print(f +1 -x)
# algumas operações não são feitas automaticamente
#  pois o sympy acha que a expressão como está, é sua
#  formar simplificada
'''Exemplo: 
x*(x+2*y) = x**2 + 2*x*y'''
f2 = x* f
print(f2)
print("Expandindo", sp.expand(f2))
# de modo inverso podemos ter originalmente uma expressão 
# como a f2, e podemos fatora-la
print("Fatorando", sp.factor(x**2 + 2*x*y))

#Resolvendo equações
eq1 = x**2 -2
sol1 = sp.solve(eq1, x) # Iguala eq1 a zero e isole o 'x'
''' x**2 -2 = 0  -> x? '''
sol2 = sp.solve(f2,y) # resolva em 'y'
print("Eq:", eq1, "= 0, solução em x:",sol1)
print("Eq:", f2, "= 0, solução em y:",sol2)
# podemos substituir uma variavel da equação por um valor específico
f2s= f2.subs(y, -8/x) # faça y= -8/x
print("Eq:", f2s, "= 0, solução:",sp.solve(f2s,x))

# não precisamos resolver sempre igualando a zero
''' podemos fazer por ex.
x**2 -16= 9, e resolver em x'''
f2s9 = sp.Eq(f2s, 9) # faz f2s = 9
print("Eq:", sp.expand(f2s9), "solução:",sp.solve(f2s9,x))

# Finalmente, podemos determinar a solução de um sistema
#  de equações
'''
x-2*y=0
x+y=18
'''
se1 = x-2*y
se2 = sp.Eq(x+y, 18)
print("Resolvendo o sistema:\n(1)", se1,"= 0")
print("(2)",se2)
solsis=sp.linsolve([se1,se2], (x,y)) # o (x,y) indica tanto as variáveis que queremos solução quanto sua ordem
print("(x , y) =",solsis)
'''se tiver alguma equação não linear no sistema
ex: x**2 = 10,
use o método sp.nonlinsolve()'''

'''
Atividade: Sobre um rio, há uma ponte de 20 metros de altura de onde um
 pescador deixa cair um anzol ligado a um peso de chumbo. Esse anzol, que cai
 a partir do repouso e em linha reta, atinge uma lancha que se deslocava com 
 velocidade constante de 20 m/s por esse rio. Nessas condições, desprezando a 
 resistência do ar e admitindo que a aceleração gravitacional seja g=10 m/s**2,
 pode-se afirmar que no exato momento do início da queda do anzol a lancha 
 estava a uma distência do vertical da queda, em metros, de:
'''
