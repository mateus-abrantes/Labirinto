import random
from cromossomos import *
from p5 import *
import numpy as np
from ga import *

# DEFINIÇÕES DO NUMERO DE COLUNAS E LINHAS, TAMANHO DOS QUADROS(AREA DOS QUADRADOS) DO LABIRINTO E UMA VARIAVEL DE DESCONTO
# DE TAMANHO PARA O TAMANHO DO PERSONAGEM EM RELACAO AO LABIRINTO
colunas = 41
linhas = 21
tam_quadro = 30
vdesconto = 5
x = 0
y = 0
path = []
analise = []
i = 0
inicial = True
demonstracao = True


# MATRIZ DO LABIRINTO (0 -> PAREDE, 1-> ESPAÇO LIVRE, 2->SAIDA, 3-ENTRADA)
M = np.array([
    [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
])

# Caminho que desejamos encontrar
target= [(0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (2, 11), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (2, 15), (1, 15), (1, 16), (1, 17), (2, 17), (3, 17), (3, 18), (3, 19), (2, 19), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (2, 23), (3, 23), (3, 24), (3, 25), (3, 26), (3, 27), (2, 27), (1, 27), (1, 28), (1, 29), (2, 29), (3, 29), (3, 30), (3, 31), (4, 31), (5, 31), (6, 31), (7, 31), (7, 30), (7, 29), (6, 29), (5, 29), (5, 28), (5, 27), (6, 27), (7, 27), (8, 27), (9, 27), (9, 28), (9, 29), (9, 30), (9, 31), (10, 31), (11, 31), (12, 31), (13, 31), (13, 32), (13, 33), (14, 33), (15, 33), (15, 34), (15, 35), (14, 35), (13, 35), (13, 36), (13, 37), (12, 37), (11, 37), (11, 38), (11, 39), (12, 39), (13, 39), (14, 39), (15, 39), (15, 38), (15, 37), (16, 37), (17, 37), (17, 38), (17, 39), (18, 39), (19, 39), (20, 39)]

# POSIÇÕES INICIAIS DO JOGADOR (QUADRO DE INICIO)
posicao_x_jogador = 45
posicao_y_jogador = 15
linha = -1
coluna = 1

def setup():
    global  path, analise
    size(colunas * tam_quadro, linhas * tam_quadro)
    no_stroke()
    path, analise = ga(target,10000)

# FUNCAO QUE CONTA A CADA 5 QUADROS DE EXECUCAO
def timeIt():
    if (frame_count % 5 == 0):
        return 1
    else:
        return 0

# FUNCAO QUE FAZ A AUTOMATIZACAO DO PERSONAGEM E DA ITERACAO DO ALGORITMO A*
def increment():
    global posicao_y_jogador, posicao_x_jogador,target, analise,demonstracao
    x,y=(0,0)
    # DEMOSTRACAO DA ITERACAO DO A*
    if(demonstracao and timeIt()):
        for i in range(0,len(analise)):
            for j in range(0,99):
                if(timeIt()):
                    fill(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    x,y = analise[i][j]
                    rect((y*tam_quadro,x*tam_quadro), tam_quadro, tam_quadro)
        demonstracao=False
    else:
        for i in range(0,99):
            if(timeIt()):
                fill(52, 222, 235)
                x,y = path[i]
                rect((y*tam_quadro, x
                      * tam_quadro), tam_quadro, tam_quadro)
    # AUTOMATIZACAO DO PERSONAGEM PELO MELHOR CAMINHO RETORNADO PELO A*

def drawMaze():
    global inicial
    if(inicial):
        # CRIAÇÃO DO DESENHO TO LABIRINTO
        background(161, 161, 161)
        for i in range(0, colunas):
            for j in range(0, linhas):
                x = i * tam_quadro
                y = j * tam_quadro
                if (M[j][i] == 3):
                    # DESENHA A POSIÇÃO DE ENTRADA "E";
                    fill(216, 227, 0)
                    rect((x, y), tam_quadro, tam_quadro)
                elif (M[j][i] == 2):
                    # DESENHA A POSIÇÃO DE SAIDA "S"
                    fill(30, 207, 6)
                    rect((x, y), tam_quadro, tam_quadro)
                elif (M[j][i] == 0):
                    # DESENHA AS PAREDES DO LABIRINTO
                    fill(25)
                    rect((x, y), tam_quadro, tam_quadro)
                elif (M[j][i] == 1):
                    # DESENHA OS ESPACOS LIVRES
                    fill(161, 161, 161)
                    rect((x, y), tam_quadro, tam_quadro)
                inicial = False
    else:
        x = coluna * tam_quadro
        y = linha * tam_quadro
        if (M[linha][coluna] == 3):
            # DESENHA A POSIÇÃO ANTERIOR DE ENTRADA "E";
            fill(216, 227, 0)
            rect((x, y), tam_quadro, tam_quadro)
        elif (M[linha][coluna] == 2):
            # DESENHA A POSIÇÃO ANTERIOR DE SAIDA "S"
            fill(30, 207, 6)
            rect((x, y), tam_quadro, tam_quadro)
        elif (M[linha][coluna] == 1):
            # DESENHA A POSIÇÃO ANTERIOR DE ESPAÇO LIVRE
            stroke(0)
            fill(52, 222, 235)
            rect((x, y), tam_quadro, tam_quadro)


def draw():
    stroke(0)
    drawMaze()
    #       print(M[posicao_x_anterior][posicao_y_anterior])
    # COR DO PERSONAGEM E CRIAÇÃO DA ELIPSE COMO PERNSONAGEM
    stroke(0)
    ellipse((posicao_x_jogador, posicao_y_jogador),
            tam_quadro-vdesconto, tam_quadro-vdesconto)
    increment()
    fill(255, 255, 255)


run()
