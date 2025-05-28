'''Atividade: Implemente o produto por escalar e mostre com gráfico.
Ex:  inicio: -> ; após produto por 3: --->'''
# Podemos reaproveitar o código de "Vetores.py"
# Lembre de deixar os arquivos na mesma pasta
from Aula_5_1ano import Vetor2D, Mostre_vetor

# Para implementar o produto por escalar, basta adicionar o metódo em Vetor2D
# Utilizaremos Herença para isso

class Vetor2Dprod(Vetor2D):
    def __rmul__(self,escalar):
        ''' Caso esteja por exemplo escalar*vetor, colocamos para repetir o método de
         vetor * escalar '''
        return self * escalar
    def __mul__(self,escalar):
        '''Entende como vetor * escalar'''
        # Primeiro verificamos se escalar é de fato um número
        if type(escalar) not in [int,float]:
            print("Só aceitamos produto de vetor com números reais")
            return 404
        else:
            # para fazer esse produto, basta multiplicar as coordenadas da ponta
            px, py = self.ponta
            ix, iy = self.pe
            novo = Vetor2Dprod(ponta=(px*escalar, py*escalar),pe=(ix,iy),nome="%.2f*%s"%(escalar,self.nome))
            return novo

#Lembre que o método de mostrar no gráfico faz comparação com um vetor referência
#  esse vetor também deve ser da nova classe
a = Vetor2Dprod((1,0))
b = 2*a
Mostre_vetor(vetores=[a,b], referencia=Vetor2Dprod(0,0))