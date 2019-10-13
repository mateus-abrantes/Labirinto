import random

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
