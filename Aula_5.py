'''Para mostrar graficamente o vetor precisamos
do matplotlib'''
import numpy as np
import matplotlib.pyplot as plt

'''Vamos focar em vetores em no plano XY para facilitar.Abaixo utilizamos o método de "classe", que é uma forma de criar objetos com vários parâmetros e métodos específicos a ele, que é perfeito para vetores.'''
class Vetor2D:
    '''Nomes definidos fora do método construtor "__init__" são da classe que cria todos os objetos ou seja, são compartilhados entre todos os objetos existentes e que ainda não foram criados'''
    sempre_origem = True
    def __init__(self, ponta=(0,1), pe=(0,0),nome='v'):
        '''Método que constrói o vetor. A notação que usaremos nos vetores será pe ---> ponta. Com a 'ponta' sendo o primeiro valor pedido podemos definir vetores na origem apenas com Vetor2D((posição_X, posição_Y)), se necessário usaremos o 'pe' para tira-lo da origem. Os nomes definidos no método __init__ são exclusivos do objeto que foi criado, i.e., se alterar no vetor 1, não influencia em nenhum outro vetor'''
        self.pe = pe 
        self.ponta = ponta
        self.nome = nome
    
    def __str__(self):
        '''Faz com que, se é pedido o vetor diretamente (ex: print(vetor) ), o nome que foi dado ao vetor aparece ao invés do seu endereço ou a classe'''
        return self.nome
    
    def __add__(self, vetor):
        '''Permite a adição de dois vetores. Para garantir que some apenas vetores, precisamos de uma verificação.'''
        if type(vetor) == type(self):
            '''Para realizar a soma vetorial, a forma mais fácil é mover o segundo vetor de forma que a 'ponta' do primeiro conecta com o 'pe' do segundo'''
            po1x, po1y = self.ponta
            pe2x, pe2y = vetor.pe
            '''como vamos mudar a posição do vetor 2 para somar, vamos guardar a configuração inicial dele e usa-la depois'''
            po2x, po2y = vetor.ponta 

            '''para saber o quanto mover o vetor 2 precisamos da diferença de coordenadas'''
            delta_x = pe2x - po1x
            delta_y = pe2y - po1y
            if delta_x>0:
                '''pe do vetor 2 está a direita da ponta do vetor 1'''
                vetor.esquerda(delta_x)
            elif delta_x<0:
                '''pe do vetor 2 está a esquerda da ponta do vetor 1'''
                vetor.direita(delta_x)

            if delta_y>0:
                '''pe do vetor 2 está acima da ponta do vetor 1'''
                vetor.baixo(delta_y)
            elif delta_y<0:
                '''pe do vetor 2 está abaixo da ponta do vetor 1'''
                vetor.cima(delta_y)
            
            '''As coordenadas do vetor 2 foram alteradas (sem modificar o vetor 2), agora o vetor soma será definido pelo 'pe' do vetor 1 ligado a 'ponta' do vetor 2'''
            self.sempre_origem = False
            novopex, novopey = self.pe
            novapontax, novapontay = vetor.ponta
            novonome="%s+%s"%(self.nome,vetor.nome)
            novo = Vetor2D(pe=(novopex,novopey),ponta=(novapontax,novapontay),nome=novonome)
            #podemos ajustar o vetor 2 para a posição inicial
            vetor.pe = (pe2x,pe2y)
            vetor.ponta = (po2x,po2y)
            return novo
        else:
            print(vetor, "Não pertence a classe Vetor2D!")
    
    def direita(self,val=1):
        '''Move o vetor para direita. Como as coordenadas do tipo (0,0) são de um tipo constante, não é possível alterar seu valor diretamente'''
        ix, iy = self.pe
        fx, fy = self.ponta
        '''mover a direita significa aumentar as coordenadas X do vetor'''
        self.pe = (ix+abs(val),iy)
        '''O comando 'abs' usa o valor absoluto. Isso é a nossa garantia que moveremos o vetor apenas na direção desejada'''
        self.ponta = (fx+abs(val),fy)

    def esquerda(self,val=1):
        '''Move o vetor para esquerda'''
        ix, iy = self.pe
        fx, fy = self.ponta
        '''mover a esquerda significa diminuir as coordenadas X do vetor'''
        self.pe = (ix-abs(val),iy)
        self.ponta = (fx-abs(val),fy)

    def cima(self,val=1):
        '''Move o vetor para cima'''
        ix, iy = self.pe
        fx, fy = self.ponta
        '''mover para cima significa aumentar as coordenadas Y do vetor'''
        self.pe = (ix,iy+abs(val))
        self.ponta = (fx,fy+abs(val))
    
    def baixo(self,val=1):
        '''Move o vetor para baixo'''
        ix, iy = self.pe
        fx, fy = self.ponta
        '''mover para baixo significa diminuir as coordenadas Y do vetor'''
        self.pe = (ix,iy-abs(val))
        self.ponta = (fx,fy-abs(val))
    
    def tamanho(self):
        '''Caso o vetor não seja paralelo a nenhuma eixo, pode ser útil saber seu tamanho. Para isso, basta considerar linhas que ligam os pontos (pe e ponta) diretamente aos eixos X e Y; escolher um dos triângulos formados com a hipotenusa entre o 'pe' e a 'ponta' e aplicar o teorema de Pitágoras'''
        pex, pey = self.pe
        pox, poy = self.ponta
        hipotenusa = ( (pox-pex)**2 +(poy-pey)**2)**0.5
        return hipotenusa
    
    def origem(self):
        '''Caso o vetor não comece na origem e você quer que ele comece, precisamos dos valores do pe para saber o quanto devemos move-lo'''
        ix, iy = self.pe
        #se uma das coordenadas já for zero não precisamos altera-la       
        #Corrijindo eixo X
        if ix>0:
            # o vetor está a direita da origem
            self.esquerda(ix)
        elif ix<0:
            # o vetor está a esquerda da origem
            self.direita(ix)
        
        #Corrijindo eixo Y
        if iy>0:
            # o vetor está acima da origem
            self.baixo(iy)
        elif iy<0:
            # o vetor está abaixo da origem
            self.cima(iy)
        
# Para mostrar graficamente os vetores
def Mostre_vetor(vetores=[], referencia = Vetor2D((0,0))):
    fig = plt.figure(dpi=100)
    if type(vetores) == type(referencia):
        '''O método recebeu só um vetor. Pela definição do método 'quiver' precisamos deixar no formato a seguir'''
        x, y = vetores.pe
        xp,yp = vetores.ponta
        o = [x], [y] #pe do vetor
        p = [xp-x], [yp-y] # quantas unidades na direção da ponta do vetor
        plt.quiver(*o,*p,angles='xy', scale_units='xy',scale=1)
        '''Por algum motivo o 'quiver' não encaixa corretamente no zoom inicial do gráfico. Então ajustamos os limites dos eixos para o tamanho do vetor e adicionamos um espaço extra de margem'''
        #margem
        mx, my = ((xp - x)/10.0, (yp - y)/10.0)
        #limites do eixo x
        plt.xlim(x-mx, xp+mx)
        #limites do eixo y
        plt.ylim(y-my, yp+my)
    elif type(vetores) == type([]):
        '''O método recebeu uma lista, então, serão mais de um vetor no mesmo gráfico. Aqui faremos o mesmo que no caso acima, porém devemos verificar cada membro da lista para garantir que todos são vetores. Quanto aos limites do gráfico teremos que procurar os vetores com as maiores coordenadas e os vetores com as menores. Para diferenciar cada vetor estamos trocando suas cores e adicionando uma legenda.'''
        '''limites do gráfico XY: assumimos valores de troca fácil - valores que devem ser pequenos ou negativos recebem inicialmente valores grandes, e valores que devem ser grandes recebem valores muito negativos. Assim quando verificarmos cada vetor, usaremos como mínimo do gráfico o menor valor entre um grande daqui e um pequeno do vetor (o do vetor será escolhido), com essa mesma ideia comparamos os valores de cada vetor. Ideia analoga pra os limites maiores do gráfico.'''
        xini, xfim = 1000, -1000
        yini, yfim = 1000, -1000
        '''Sequência de cores nos vetores: blue(b), green(g), red(r), cyan(c), magenta(m), yellow(y), black(k)'''
        cores =['b','g','r','c','m','y','k']
        indice_cor=0
        for i in vetores:
            if type(i)!= type(referencia):
                print(i, "Não é do tipo Vetor2D!")
                return 404
            x, y = i.pe
            xp,yp = i.ponta
            #modificando os limites dos eixos
            xini = min(x,xp,xini)
            xfim = max(x,xp,xfim)
            yini = min(y,yp,yini)
            yfim = max(y,yp,yfim)

            o = [x], [y]
            p = [xp-x], [yp-y] 
            plt.quiver(*o,*p,angles='xy', scale_units='xy',scale=1,color=cores[indice_cor],label=i)
            indice_cor +=1
            if indice_cor == len(cores):
                indice_cor = 0
        #para a legenda aparecer no topo esquerdo
        plt.legend(loc="upper left") 
        #margem
        margemx, margemy = ((xfim - xini)/10.0, (yfim - yini)/10.0)
        plt.xlim(xini-margemx, xfim+margemx)
        plt.ylim(yini-margemy, yfim+margemy)
    else:
        #não é um vetor ou uma lista de vetores
        print(vetores, "Não é do tipo Vetor2D ou uma lista de Vetor2D!")
        return 404
          
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show() 

if __name__ == "__main__":
    a = Vetor2D((1,2),nome='a')
    b = Vetor2D((1,-2),nome='b')
    c = a+b
    Mostre_vetor([a,b,c])
    '''
Atividade 6: Implemente o produto por escalar e mostre com gráfico.
Ex:  inicio: -> ; após produto por 3: --->

Atividade 7: Em uma brincadeira de caça ao tesouro, o mapa diz que para chegar
 ao local onde a arca de ouro está enterrada, deve-se, primeiramente, dar 10
 passos na direção norte, depois 12 passos para o leste, em seguida, 7 passos
 para o sul, e finalmente 8 passos para oeste.
A partir dessas informações:
    (a) Desenhe em um gráfico a trajetória descrita no mapa usando vetores
    (b) Se um caçador caminhasse em linha reta, desde o ponto de partida
    até o ponto de chegada, quantos passos ele daria?
'''
