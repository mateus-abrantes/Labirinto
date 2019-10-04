#DEPENDENCIAS: p5py -> https://github.com/p5py/p5
from p5 import *
import numpy as np

#DEFINIÇÕES DO NUMERO DE COLUNAS E LINHAS, TAMANHO DOS QUADROS(AREA DOS QUADRADOS) DO LABIRINTO E UMA VARIAVEL DE DESCONTO
#DE TAMANHO PARA O TAMANHO DO PERSONAGEM EM RELACAO AO LABIRINTO
colunas = 41
linhas =21
tam_quadro =30
vdesconto =5
x=0
y=0

#MATRIZ DO LABIRINTO (0 -> PAREDE, 1-> ESPAÇO LIVRE, 2->SAIDA, 3-ENTRADA)
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]])

#POSIÇÕES INICIAIS DO JOGADOR (QUADRO DE INICIO)
posicao_x_jogador = 45
posicao_y_jogador = 15
linha=-1;
coluna=1
cont=0

def setup():
    size(colunas * tam_quadro, linhas * tam_quadro)
    no_stroke()
    background(161, 161, 161)

def drawMaze():
    #CRIAÇÃO DO DESENHO TO LABIRINTO
    if posicao_x_jogador==45 and posicao_y_jogador==15:
        for i in range (0,colunas):
            for  j in range (0,linhas):
                x = i * tam_quadro
                y = j * tam_quadro
                if (M[j][i] == 3):
                    #DESENHA A POSIÇÃO DE ENTRADA "E";
                    fill(216, 227, 0)
                    rect((x, y), tam_quadro, tam_quadro)
                elif (M[j][i] == 2):
                    #DESENHA A POSIÇÃO DE SAIDA "S"
                    fill(30, 207, 6)
                    rect((x, y), tam_quadro, tam_quadro)
                elif (M[j][i] == 0):
                    #DESENHA AS PAREDES DO LABIRINTO
                    fill(25)
                    rect((x, y), tam_quadro, tam_quadro)
    else:
        x = coluna * tam_quadro
        y = linha * tam_quadro
        if (M[linha][coluna] == 3):
            #DESENHA A POSIÇÃO ANTERIOR DE ENTRADA "E";
            fill(216, 227, 0)
            rect((x, y), tam_quadro, tam_quadro)
        elif (M[linha][coluna] == 2):
            #DESENHA A POSIÇÃO ANTERIOR DE SAIDA "S"
            fill(30, 207, 6)
            rect((x, y), tam_quadro, tam_quadro)
        elif (M[linha][coluna] == 1):
            #DESENHA A POSIÇÃO ANTERIOR DE ESPAÇO LIVRE
            fill(161,161,161)
            rect((x, y), tam_quadro, tam_quadro)

def draw():
    stroke(0)
    drawMaze()
    #       print(M[posicao_x_anterior][posicao_y_anterior])
    #COR DO PERSONAGEM E CRIAÇÃO DA ELIPSE COMO PERNSONAGEM

    fill(255, 255, 255)
    ellipse((posicao_x_jogador, posicao_y_jogador), tam_quadro-vdesconto, tam_quadro-vdesconto)

def barreiras(x, y):
    if(((((posicao_x_jogador+x)/30) >=0 and int((posicao_x_jogador+x)/30)<=40) and (((posicao_y_jogador+y)/30) >=0 and int((posicao_y_jogador+y)/30)<=20))):
        if (M[int((posicao_y_jogador + y) / 30)][int((posicao_x_jogador + x) / 30)] != 0 ):
            return 1
    else:
        return 0

def key_pressed(event):
    global x,y
    global posicao_x_jogador,posicao_y_jogador, linha, coluna
    linha=int(posicao_y_jogador/tam_quadro)
    coluna=int(posicao_x_jogador/tam_quadro)
    if  key == 'UP' and barreiras(0,-30):
        posicao_y_jogador -= 30
        y = -30
        x = 0
    elif key == 'DOWN' and barreiras(0,30):
        posicao_y_jogador += 30
        y = 30
        x = 0
    elif key == 'RIGHT' and barreiras(30,0):
        posicao_x_jogador += 30
        x = 30
        y = 0
    elif key == 'LEFT' and barreiras(-30,0):
        posicao_x_jogador -= 30
        x = -30
        y = 0


    #print(posicao_x_anterior,"OIII",posicao_y_anterior)

run()
