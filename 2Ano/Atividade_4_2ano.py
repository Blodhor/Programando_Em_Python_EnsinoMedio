'''Atividade_4_2ano: Um barbeiro B segura um espelho plano E2,
de espessura desprezível, paralelamente a outro espelho plano E1,
também de espessura desprezível, permitindo que seu cliente A observer, no espelho E1,
o seu corte de cabelo na parte posterior da cabeça.

Esquema:
B|--|E2|--|A|--|E1 
Distância E2_A: 0.6 m | Distância A_E1: 1 m

Determine a menor distância entre o cliente e a imagem
que ele observa da sua nuca no espelho E1, considerando
que a cabeça do cliente também possui dimensões desprezíveis.
'''

def Dist_objeto_imagem(distancia_espelho):
    return 2*distancia_espelho

#A imagem da nuca de A em E2
d_A_E2 = Dist_objeto_imagem(0.6) #A'|--|A
#objeto A' (imagem da nuca) está a d_A_E2 de A

#Imagem do A' em E1 terá a distância d_A_E2 somado a distância de A ao E1 (de 1m) 
d_e2_e1 = Dist_objeto_imagem(d_A_E2+1)
#d_e2_e1 é a distância A'|----|A''
#queremos a distância A|--|A''
# Como A esta a d_A_E2 a frente de A', basta subtrair 
d_ai= d_e2_e1 - d_A_E2
print(d_ai, "m")