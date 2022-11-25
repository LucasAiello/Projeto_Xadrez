PRETAS = "pretas"
BRANCAS = "brancas"
TAMANHO_TABULEIRO = 8
ESPACO= u'\u2001'
SEPARADOR_VAZIO= ''
SEPARADOR_VERTICAL1='| '
SEPARADOR_VERTICAL=' | '
SEPARADOR_VERTICAL0=' |'
SEPARADOR_HORIZ= '_'*38

turno = BRANCAS

""" Sugestão - As peças serem armazenadas em constantes (uma pra cada), para uma melhor visualização e ficar mais facil
na hora de movimentar as peças """

pecasbrancas = ['\u2656','\u2657','\u2658','\u2654','\u2655','\u2658', '\u2657','\u2656']

pecaspretas = ['\033[30m\u265c\033[m',  '\033[30m\u265d\033[m','\033[30m\u265e\033[m',
             '\033[30m\u265a\033[m',  '\033[30m\u265b\033[m', '\033[30m\u265e\033[m',
             '\033[30m\u265d\033[m', '\033[30m\u265c\033[m', '\033[30m\u2659\033[m']
tabuleiro = []


def montando_tabuleiro():
    for i in range(TAMANHO_TABULEIRO):
        tabuleiro.append([])
        for j in range(TAMANHO_TABULEIRO):
            if i <= 1 or i >= 6:
                if i == 1:
                    tabuleiro[i].append("\u2659")
                elif i == 0:
                    for h in range(TAMANHO_TABULEIRO):
                        tabuleiro[i].append(pecasbrancas[h])
                elif i == 6:
                    tabuleiro[i].append(pecaspretas[-1])
                elif i == 7:
                    for h in range(TAMANHO_TABULEIRO):
                        tabuleiro[i].append(pecaspretas[h])
            else:
                tabuleiro[i].append(ESPACO)


def imprime_tabuleiro():
    for i in range(TAMANHO_TABULEIRO):
        print(SEPARADOR_HORIZ)
        for j in range(TAMANHO_TABULEIRO):
            if j == TAMANHO_TABULEIRO-1:
                print(SEPARADOR_VERTICAL+tabuleiro[i][j], end= SEPARADOR_VERTICAL0)
            else:
                if j == 0:
                    print(SEPARADOR_VERTICAL1, end=tabuleiro[i][j])
                else:
                    print(SEPARADOR_VERTICAL, end=tabuleiro[i][j])
        print()
        if i == TAMANHO_TABULEIRO-1:
            print(SEPARADOR_HORIZ)


def trocar_turno():
    global turno
    if turno == BRANCAS:
        turno = PRETAS
    else:
        turno = BRANCAS


montando_tabuleiro()
imprime_tabuleiro()
