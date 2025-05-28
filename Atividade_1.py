'''Atividade:
Faça um código que peça uma sequência de valores
e calcule a média deles.
'''
print("Calculadora de média")
entrada=input("Informe os números separados por espaço: ")

#split() procura um padrão na frase e quebra ela em uma lista
'''exemplo:
"eu curto programar".split(" ") == ["eu", "curto", "programar"]'''
l=entrada.split() # quando não damos nenhum padrão, assumesse que separaremos por espaço

soma=0
for i in l:
    soma += float(i) # float transforma em número real

print("Média =", soma/len(l))