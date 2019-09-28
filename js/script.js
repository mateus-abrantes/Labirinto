//DEFINIÇÕES DO NUMERO DE COLUNAS E LINHAS, TAMANHO DOS QUADROS(AREA DOS QUADRADOS) DO LABIRINTO E UMA VARIAVEL DE DESCONTO 
//DE TAMANHO PARA O TAMANHO DO PERSONAGEM EM RELACAO AO LABIRINTO
var colunas = 41, linhas = 21, tam_quadro = 30, vdesconto = 5;
//MATRIZ SO TABULEIRO
var M = [];
//POSIÇÕES INICIAIS DO JOGADOR (QUADRO DE INICIO)
var posicao_x_jogador = 45, posicao_y_jogador = 15;
var x, y;
function setup() {
    //CRIAÇÃO DO CANVAS (TELA DO JOGO)
    createCanvas(colunas * tam_quadro, linhas * tam_quadro);

    //MATRIZ DO LABIRINTO (0 -> PAREDE, 1-> ESPAÇO LIVRE, 2->SAIDA, 3-ENTRADA)
    M = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]];
}

function draw() {
    //COR DE FUNDO DO LABIRINTO (SERVE PARA DESTACAR A COR DO ESPAÇO LIVRE)
    background(161, 161, 161);
    //CRIAÇÃO DO DESENHO TO LABIRINTO
    for (var i = 0; i < colunas; i++) {
        for (var j = 0; j < linhas; j++) {
            var x = i * tam_quadro;
            var y = j * tam_quadro;
            stroke(0);

            if (M[j][i] == 3) {
                //DESENHA A POSIÇÃO DE ENTRADA "E";
                fill(216, 227, 0);
                rect(x, y, tam_quadro, tam_quadro);
            }
            if (M[j][i] == 2) {
                //DESENHA A POSIÇÃO DE SAIDA "S"
                fill(30, 207, 6);
                rect(x, y, tam_quadro, tam_quadro);
            }
            if (M[j][i] == 0) {
                //DESENHA AS PAREDES DO LABIRINTO
                fill(25);
                rect(x, y, tam_quadro, tam_quadro);
            }

        }
    }
    //COR DO PERSONAGEM E CRIAÇÃO DA ELIPSE COMO PERNSONAGEM
    fill(255, 255, 255);
    ellipse(posicao_x_jogador, posicao_y_jogador, tam_quadro-vdesconto, tam_quadro-vdesconto);
}
//FUNCAO QUE FERIFICA QUANDO AS TECLAS SE SETA SAO SOLTAS E MOVE O PERSONAGEM POR UM QUADRADO
function keyReleased() {
    if ((keyCode === UP_ARROW) && barreiras(0,-30)) {
        posicao_y_jogador -= 30;
        y = -30;
        x = 0;
    }
    if ((keyCode === RIGHT_ARROW)&& barreiras(30,0)) {
        posicao_x_jogador += 30;
        x = 30;
        y = 0;
    }
    if ((keyCode === LEFT_ARROW) && barreiras(-30,0)) {
        posicao_x_jogador -= 30;
        x = -30;
        y = 0;
    }
    if ((keyCode === DOWN_ARROW) && barreiras(0,30)) {
        posicao_y_jogador += 30;
        y = 30;
        x = 0;
    }
    //DEBUG POSICAO DO PERSONAGEM
    //print(int(0.5)); // -10.5
    print("X:" + (posicao_y_jogador/30) + " Y:" + (posicao_x_jogador/30));
    print("M[" + int((posicao_y_jogador)/30) + "][" + int((posicao_x_jogador)/30) + "]=" + M[int((posicao_y_jogador) / 30)][int((posicao_x_jogador) / 30)]);
}
//PROIBIR O PERSONAGEM DE ATRAVESSAR AS PAREDES
function barreiras(x, y) {
    if(((((posicao_x_jogador+x)/30) >=0 && int((posicao_x_jogador+x)/30)<=40) && (((posicao_y_jogador+y)/30) >=0 && int((posicao_y_jogador+y)/30)<=20))){
        if (M[int((posicao_y_jogador + y) / 30)][int((posicao_x_jogador + x) / 30)] != 0 )
        return true;
    }
    else return false;
}


