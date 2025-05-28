#MCU
'''Atividade:
Considere uma polia girando em torno de
seu eixo central, conforme figura abaixo. A velocidade
dos pontos A e B são, respectivamente, 60 cm/s e 0,3 m/s.
A distância AB vale 10 cm. O diâmetro e a velocidade
angular da polia, respectivamente, valem:


Solução:Nesse caso a velocidade angular de A e B são iguais.
wa=wb, r*w=v
Logo, va/r= vb/(r-10)
r/va = r/vb - 10/vb
10/vb = r*(1/vb -1/va)
r = 10/(vb*(1/vb -1/va)) 
diametro = 2*r
'''
def diametro(va,vb):
    r= 10/(vb*(1/vb -1/va))
    return 2*r
def vel_angular(v,r):
    return v/r

d=diametro(60,30)
omega=vel_angular(60,d/2)
print("%d cm e %.1f rad/s"%(d,omega)) 
