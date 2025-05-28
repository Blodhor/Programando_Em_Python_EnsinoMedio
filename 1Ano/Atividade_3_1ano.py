'''Atividade: Uma ave marinha costuma mergulharde uma altura de 20 m
 para buscar alimento no mar. Suponha que um desses mergulhos tenha sido
 feito em sentido vertical, a partir do repouso. Desprezando-se as forças
 de atrito, a ave chegará à superfície do mar em qual velocidade em km/h?
'''
#Os métodos que precisamos definir são:
#Equação de Torricelli e um conversor m/s -> km/h
def V_Torricelli(v0,a,delta_s):
    return (v0**2 +2*a*delta_s)**0.5

def V_kmhora(v):
    return v*3.6

print("A velocidade da ave ao atingir o mar será:%.1f km/h"%V_kmhora(V_Torricelli(0,9.8,20)))
