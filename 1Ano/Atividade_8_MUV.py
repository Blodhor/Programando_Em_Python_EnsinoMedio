'''
Atividade: Sobre um rio, há uma ponte de 20 metros de altura de onde um
 pescador deixa cair um anzol ligado a um peso de chumbo. Esse anzol, que cai
 a partir do repouso e em linha reta, atinge uma lancha que se deslocava com 
 velocidade constante de 20 m/s por esse rio. Nessas condições, desprezando a 
 resistência do ar e admitindo que a aceleração gravitacional seja g=10 m/s**2,
 pode-se afirmar que no exato momento do início da queda do anzol a lancha 
 estava a uma distência do vertical da queda, em metros, de:

Solução:
Basta determinar o tempo de queda do anzol com a
Equação horária do MUV
eq1: 0 = 20 -(10/2)* (t**2)
A lancha está no regime MU, então seu deslocamente foi
eq2: d = 20*t
'''
from sympy import *
d, t = symbols('d t')
eq1 = 20 -(10/2)* (t**2)
eq2 = Eq(d, 20*t)
print("(tempo de queda, distância inicial da lancha) =")
# como o termo t**2 não é linear, usamos nonlinsolve
print(nonlinsolve([eq1,eq2], (t,d)))
# como tempo nunca é negativo, apenas uma das soluções é válida
# mas o método devolve todas as soluções matematicamente possíveis
