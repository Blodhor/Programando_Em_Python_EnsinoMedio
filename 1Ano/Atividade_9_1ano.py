'''Atividade 9: Um bloco escorrega, livre de resistência do
ar, sobre um plano inclinado de 30° conforme a figura
(sem escala) a seguir.

No trecho AB não existe atrito e no trecho BC o coefi-
ciente de atrito vale mu = sqrt(3)/2. O bloco é abandonado,
do repouso em relação ao plano inclinado, no ponto A e chega
ao ponto C com velocidade nula. A altura do ponto A, em 
relação ao ponto B, é h1, e a altura do ponto B, em relação
ao ponto C, é h2. Quanto vale a razão h1/h2?

Solução: 30° = pi/6 rad
h1 = AB sin(pi/6), h1+h2 = AC sin(pi/6), ou
h1/AB = (h1+h2)/AC
h1*(1/AB-1/AC)=h2/AC
h1/h2= 1/(AC*(1/AB-1/AC)) , AC= AB+BC
h1/h2 = 1/((AB+BC)*(1/AB-1/(AB+BC)))(eq1)

Com Torricelli temos
vB**2=va**2+2*a*AB, va=0 e a=g*sin(pi/6), pois não tem atrito
vB**2=2*g*sin(pi/6)*AB;

vC**2 = vB**2+ 2*a_bc*BC, vc=0
0=2*g*sin(pi/6)*AB + 2*a_bc*BC (eq2)

Encontramos a_bc com a 2 lei de Newton
Fr= P*sin(pi/6) -Fat, Fat=N*mu=P*cos(pi/6)*mu 
m*a_bc = m*g*sin(pi/6) - m*g*cos(pi/6)*sqrt(3)/2
a_bc = g*sin(pi/6) - g*cos(pi/6)*sqrt(3)/2 (eq3)
'''
from sympy import*
def a_bc(g):
    #eq3
    return g*sin(pi/6) - g*cos(pi/6)*sqrt(3)/2

def razaoh1_h2():
    AB, BC, g , r= symbols('AB BC g r')
    #r = h1/h2
    h1_h2 = Eq(r,1/((AB+BC)*(1/AB-1/(AB+BC)))) 
    eq2 = 2*g*sin(pi/6)*AB + 2*a_bc(g)*BC
    
    sol = nonlinsolve([h1_h2, eq2],(AB,r))
    # como só terá 1 solução possível, posso arrumar o print
    #str() força o argumento a virar texto
    #split() separa o texto em um lista, baseado no padrão dado
    dados= str(sol)[2:-2].split(',')
    print("AB=%s e h1/h2=%s"%(dados[0],dados[1]))

razaoh1_h2()