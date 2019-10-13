import random
from helpers import summarize

class cromossomos:

    genes = None
    path= None

    def __init__(self,genes=None, path=None):
        self.genes= genes
        self.path= path

    def gerar(self):
        """Gera-se um cromossomo, do tipo lista, equivalente a um conjunto  de posições aleatórias do labirinto"""
        self.path=[]
        condition= True
        cont=0
        while condition:
            if cont<99:
                teste = (random.randint(0,21),random.randint(0,41))
                self.path.append(teste)
                cont+=1
            else:
                condition=False

    def getFitness(self, target):
        self.fitness=0
        for i in range(len(self.path)):
            if self.path[i]==target[i]:
                self.fitness+=1

    def crossover(self, parceiro):
        aux = random.randint(0,99)
        filho = cromossomos()
        filho.gerar()
        """choice = random.choice([True, False])

        if choice==True:
            filho.path[0:aux]= self.path[0:aux]
            if aux<98:
                filho.path[aux+1:98] = parceiro.path[aux+1:98]
        else:
            filho.path[0:aux]= parceiro.path[0:aux]
            if aux<98:
                filho.path[aux+1:98] = self.path[aux+1:98]"""
        for i in range(len(self.path)):
            choice = random.choice([True, False])

            if choice==True:
                filho.path[i]= self.path[i]
            else:
                filho.path[i]= parceiro.path[i]
        return filho

    def mutacionar(self, cont: int):
        for i in range(len(self.path)):
            if random.random() < 0.01 * (cont/100):
                self.path[i]= (random.randint(0,21),random.randint(0,41))
def main():
    # Caminho que desejamos encontrar
    target= [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (2, 15), (1, 15), (1, 16), (1, 17), (2, 17), (3, 17), (3, 18), (3, 19), (2, 19), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (2, 23), (3, 23), (3, 24), (3, 25), (3, 26), (3, 27), (2, 27), (1, 27), (1, 28), (1, 29), (2, 29), (3, 29), (3, 30), (3, 31), (4, 31), (5, 31), (6, 31), (7, 31), (7, 30), (7, 29), (6, 29), (5, 29), (5, 28), (5, 27), (6, 27), (7, 27), (8, 27), (9, 27), (9, 28), (9, 29), (9, 30), (9, 31), (10, 31), (11, 31), (12, 31), (13, 31), (13, 32), (13, 33), (14, 33), (15, 33), (15, 34), (15, 35), (14, 35), (13, 35), (13, 36), (13, 37), (12, 37), (11, 37), (11, 38), (11, 39), (12, 39), (13, 39), (14, 39), (15, 39), (15, 38), (15, 37), (16, 37), (17, 37), (17, 38), (17, 39), (18, 39), (19, 39), (20, 39)]

    # Definição da população
    populacao = []
    tam = 10000
    melhorScore = 0
    geracao = 1

    """
        A variável cont será responsável
        por armazenar a quantidade de vezes
        em que uma geração não encontrou uma
        solução com o melhor score. Esse parametro
        será necessário para definir o limite na
        mutação do cromossomo. Enquanto isso, a
        Flag será responsável por sinalizar se a
        houve uma mudança de melhorScore ou não
    """
    cont = 0
    flag = melhorScore

    # Gerar membros da população
    for i in range(tam):
        populacao.append(cromossomos())
        populacao[i].gerar()

    # Enquanto o melhor Score for menor que o tamanho da populacão, gera-se uma nova
    while melhorScore < len(target):
        if flag==melhorScore:
            cont+=1
        else:
            cont=0
            flag=melhorScore

        # Armazena todas  as solucoes candidatas a se reproduzir
        mattingPool = []

        # copia todos os individuos da geracao atual
        pais = populacao[:]
        populacao = []

        """ Método de roleta:
            Armazenará-se na lista de soluções candidatas
            de acordo com a aptidão. Isto é, se o fitness
            do cromossomo for igual a zero, então ignoraremos
            a sua existência. Caso for igual a n, armazenaremos
            na lista este cromossomo na lista n vezes
        """
        for i in range(tam):
            pais[i].getFitness(target)
            for j in range(pais[i].fitness):
                mattingPool.append(pais[i])

        for i in range(tam):
            if pais[i].fitness > melhorScore:
                melhorScore = pais[i].fitness
                summarize(geracao, pais[i].path, melhorScore)

        """
            Se não há candidatos, gera-se uma nova população
        """
        if len(mattingPool)== 0:
            populacao.append(cromossomos())
            populacao[i].gerar()

        for i in range(tam):
            x = random.choice(range(len(mattingPool)))
            y = random.choice(range(len(mattingPool)))



            filho = mattingPool[x].crossover(mattingPool[y])
            if cont > random.randint(0,tam):
                filho.mutacionar(cont)

            populacao.append(filho)
        geracao += 1
        print(geracao)

if __name__=="__main__":
    main()
