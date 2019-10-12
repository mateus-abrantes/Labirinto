# DEPENDENCIAS: p5py -> https://github.com/p5py/p5
from p5 import *
import numpy as np
from astar import *


# DEFINIÇÕES DO NUMERO DE COLUNAS E LINHAS, TAMANHO DOS QUADROS(AREA DOS QUADRADOS) DO LABIRINTO E UMA VARIAVEL DE DESCONTO
# DE TAMANHO PARA O TAMANHO DO PERSONAGEM EM RELACAO AO LABIRINTO
colunas = 41
linhas = 21
tam_quadro = 30
vdesconto = 5
x = 0
y = 0
analise = Node
path = []
i = 0
inicial = True
demonstracaoa = True

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

# POSIÇÕES INICIAIS DO JOGADOR (QUADRO DE INICIO)
posicao_x_jogador = 45
posicao_y_jogador = 15
linha = -1
coluna = 1


def setup():
    global  path, i, analise
    size(colunas * tam_quadro, linhas * tam_quadro)
    no_stroke()
    start = (0, 1)
    end = (20, 39)
    path, analise = astar(M, start, end)

# FUNCAO QUE CONTA A CADA 5 QUADROS DE EXECUCAO


def timeIt():
    if (frame_count % 5 == 0):
        return 1
    else:
        return 0

# FUNCAO QUE FAZ A AUTOMATIZACAO DO PERSONAGEM E DA ITERACAO DO ALGORITMO A*


def increment():
    global i, posicao_y_jogador, posicao_x_jogador, analise, demonstracaoa
    # DEMOSTRACAO DA ITERACAO DO A*
    if(demonstracaoa):
        if (i < (len(analise)) and timeIt()):
            fill(100, 255, analise[i].f % 255)
            rect((analise[i].position[1]*tam_quadro,
                  analise[i].position[0]*tam_quadro), tam_quadro, tam_quadro)
            i += 1
        elif(i == len(analise)):
            i = 0
            demonstracaoa = False
    # AUTOMATIZACAO DO PERSONAGEM PELO MELHOR CAMINHO RETORNADO PELO A*
    elif(~demonstracaoa):
        # FAZ COM QUE O RASTRO DO PERCURSO DO PERSONAGEM SEJA PREENCHIDO COM UM QUADRADO AZUL CLARO
        if(i > 0):
            fill(52, 222, 235)
            rect((path[i-1][1]*tam_quadro, path[i-1][0]
                  * tam_quadro), tam_quadro, tam_quadro)
        # AUTOMATIZA O MOVIMENTO DO PERSOAGEM A 5 QUADROS POR INTERACAO E DEPOIS DE FECHA A JANELA
        if (i < len(path) and timeIt()):
            posicao_x_jogador = path[i][1]*tam_quadro+15
            posicao_y_jogador = path[i][0]*tam_quadro+15
            i += 1
        elif (i == (len(path))):
            exit()


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
    increment()
    fill(255, 255, 255)
    ellipse((posicao_x_jogador, posicao_y_jogador),
            tam_quadro-vdesconto, tam_quadro-vdesconto)


run()
