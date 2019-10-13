import random
from helpers import summarize
from cromossomos import *

def ga(target, tam):
    # Definição da população
    populacao = []
    melhorScore = 0
    geracao = 1
    aux = []

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
                aux.append(pais[i].path)

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
        caminho= populacao.path
        return caminho, aux
