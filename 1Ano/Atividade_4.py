'''
Atividade: Um trem de 150 m de comprimento se desloca com velocidade escalar
 constante de 16 m/s. Esse trem atravessa 3 túneis em dias diferentes e leva 
 desde a entrada até a saída completa de cada túnel 50 s, 20 s e 90 s. Quanto 
 é o comprimento de cada túnel?

Solução: 
 Considerando o momento que a frente do trem alcança a abertura do túnel com t=0s;
 para que o trem atravesse completamente o túnel, a parte traseira do trem deve percorrer
 o comprimento do trem (150 m) para alcançar o túnel e todo comprimento do túnel (d metros)
 para atravessa-lo totalmente, logo
    delta_s = d + 150            (1)
    delta_s = v*delta_t, v=16m/s (2)
    Substituindo (1) em (2)
    d + 150 = 16*delta_t, isolando o comprimento do túnel
    d = 16*delta_t -150
'''
def Comprimento_tunel(v=16,trem=150):
    return lambda t: v*t -150

d = Comprimento_tunel() # assim aceito os valores predefinidos de 'v' e 'trem'
print("Os túneis possuem respectivamente:")
for i in [50,20,90]:
    print("%.1f metros de comprimento"%d(i))
