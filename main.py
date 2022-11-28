ERRO_SEM_PEÇA_LOCAL = "Não há peça da sua cor no local indicado.\n"
PRETAS = "pretas"
BRANCAS = "brancas"
TAMANHO_TABULEIRO = 8
MSG_TURNO = "          TURNO DAS {}"
ESPACO = u'\u2001'
SEPARADOR_VAZIO = ''
SEPARADOR_VERTICAL1 = '| '
SEPARADOR_VERTICAL = ' | '
SEPARADOR_VERTICAL0 = ' |'
SEPARADOR_HORIZ = '_'*38
RAINHA_B = '\u2655'
REI_B = '\u2654'
TORRE_B = '\u2656'
BISPO_B = '\u2657'
CAVALO_B = '\u2658'
PEAO_B = '\u2659'
RAINHA_P = '\033[30m\u265b\033[m'
REI_P = '\033[30m\u265a\033[m'
TORRE_P = '\033[30m\u265c\033[m'
BISPO_P = '\033[30m\u265d\033[m'
CAVALO_P = '\033[30m\u265e\033[m'
PEAO_P = '\033[30m\u2659\033[m'


def montando_tabuleiro():
    global tabuleiro
    pecas_brancas = [TORRE_B, CAVALO_B, BISPO_B, RAINHA_B, REI_B, BISPO_B, CAVALO_B, TORRE_B]
    pecas_pretas = [TORRE_P, CAVALO_P, BISPO_P, RAINHA_P, REI_P, BISPO_P, CAVALO_P, TORRE_P]

    for i in range(TAMANHO_TABULEIRO):
        tabuleiro.append([])
        for j in range(TAMANHO_TABULEIRO):
            if i <= 1 or i >= 6:
                if i == 1:
                    tabuleiro[i].append(PEAO_P)
                elif i == 0:
                    for h in range(TAMANHO_TABULEIRO):
                        tabuleiro[i].append(pecas_pretas[h])
                elif i == 6:
                    tabuleiro[i].append(PEAO_B)
                elif i == 7:
                    for h in range(TAMANHO_TABULEIRO):
                        tabuleiro[i].append(pecas_brancas[h])
            else:
                tabuleiro[i].append(ESPACO)


def criar_referencia_cor():
    global tabuleiro_cores
    for i in range(TAMANHO_TABULEIRO):
        linha = []
        for j in range(TAMANHO_TABULEIRO):
            if i == 0 or i == 1:
                linha.append(PRETAS)
            elif i == 6 or i == 7:
                linha.append(BRANCAS)
            else:
                linha.append(ESPACO)
        tabuleiro_cores.append(linha)


def imprime_tabuleiro():
    for i in range(TAMANHO_TABULEIRO):
        if i == 0:
            for h in range(TAMANHO_TABULEIRO+1):
                print(ESPACO, end=coluna_tabuleiro[h])
            print()
        print(' ', SEPARADOR_HORIZ)
        for j in range(TAMANHO_TABULEIRO):

            if j == TAMANHO_TABULEIRO-1:
                print(SEPARADOR_VERTICAL+tabuleiro[i][j], end=SEPARADOR_VERTICAL0)
            else:
                if j == 0:
                    print(i+1, SEPARADOR_VERTICAL1, end=tabuleiro[i][j])
                else:
                    print(SEPARADOR_VERTICAL, end=tabuleiro[i][j])
        print()
        if i == TAMANHO_TABULEIRO-1:
            print(' ', SEPARADOR_HORIZ)


def trocar_turno():
    global turno
    if turno == BRANCAS:
        turno = PRETAS
    else:
        turno = BRANCAS


def validar_jogada(coordenada):
    global posi_atual_p
    global movimento_p

    if len(coordenada) == 5 and coordenada[2 == " "]:
        posi_atual_p = coordenada[:2]
        movimento_p = coordenada[3:]
    elif len(coordenada) == 4:
        posi_atual_p = coordenada[:2]
        movimento_p = coordenada[2:]
    else:
        return False

    if posi_atual_p[0].isnumeric() and movimento_p[0].isnumeric():
        if int(movimento_p[0])-1 >= 0 and int(movimento_p[0])-1 <= 7:
            for i in range(len(coluna_referencia)):
                if movimento_p[1] == coluna_referencia[i]:
                    if tabuleiro_cores[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] == turno:
                        return True


def jogar():
    if tabuleiro[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] == PEAO_B or \
            tabuleiro[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] == PEAO_P:

        mover_peao()

    elif tabuleiro[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] == CAVALO_B or \
            tabuleiro[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] == CAVALO_P:

        mover_cavalo()


def mover_peao():
    global posi_atual_p
    global movimento_p
    valido = False

    if movimento_p[1] == posi_atual_p[1]:
        if int(movimento_p[0]) == int(posi_atual_p[0])-1:
            if tabuleiro_cores[int(movimento_p[0])-1][coluna_referencia.index(movimento_p[1])] == ESPACO:
                valido = True

        elif int(movimento_p[0]) == int(posi_atual_p[0])-2 and int(posi_atual_p[0]) == 7:
            if tabuleiro_cores[int(movimento_p[0])][coluna_referencia.index(movimento_p[1])] == ESPACO:
                valido = True

    elif coluna_referencia.index(posi_atual_p[1]) == coluna_referencia.index(movimento_p[1])+1 or \
            coluna_referencia.index(posi_atual_p[1]) == coluna_referencia.index(movimento_p[1])-1:
        if int(movimento_p[0]) == int(posi_atual_p[0])-1 and tabuleiro_cores[int(movimento_p[0])-1]\
                [coluna_referencia.index(movimento_p[1])] == PRETAS:
            valido = True

    if movimento_p[1] == posi_atual_p[1]:
        if int(movimento_p[0]) == int(posi_atual_p[0]) + 1:
            if tabuleiro_cores[int(movimento_p[0]) - 1][coluna_referencia.index(movimento_p[1])] == ESPACO:
                valido = True

        elif int(movimento_p[0]) == int(posi_atual_p[0]) + 2 and int(posi_atual_p[0]) == 2:
            if tabuleiro_cores[int(movimento_p[0]) - 2][coluna_referencia.index(movimento_p[1])] == ESPACO:
                valido = True

    elif coluna_referencia.index(posi_atual_p[1]) == coluna_referencia.index(movimento_p[1])+1 or \
            coluna_referencia.index(posi_atual_p[1]) == coluna_referencia.index(movimento_p[1])-1:
        if int(movimento_p[0]) == int(posi_atual_p[0])+1 and tabuleiro_cores[int(movimento_p[0])-1]\
                [coluna_referencia.index(movimento_p[1])] == BRANCAS:
            valido = True

    if valido:
        tabuleiro[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] = ESPACO

        tabuleiro_cores[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] = ESPACO
        tabuleiro_cores[int(movimento_p[0]) - 1][coluna_referencia.index(movimento_p[1])] = turno

        if turno == BRANCAS:
            tabuleiro[int(movimento_p[0]) - 1][coluna_referencia.index(movimento_p[1])] = PEAO_B
        else:
            tabuleiro[int(movimento_p[0]) - 1][coluna_referencia.index(movimento_p[1])] = PEAO_P


def mover_cavalo():
    if tabuleiro_cores[int(movimento_p[0])-1][coluna_referencia.index(movimento_p[1])] != turno:
        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                if (int(movimento_p[0]) == int(posi_atual_p[0])+i and coluna_referencia.index(movimento_p[1]) == coluna_referencia.index(posi_atual_p[1])+j) or\
                        (int(movimento_p[0]) == int(posi_atual_p[0])+j and coluna_referencia.index(movimento_p[1]) == coluna_referencia.index(posi_atual_p[1])+i):

                    tabuleiro[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] = ESPACO

                    tabuleiro_cores[int(posi_atual_p[0]) - 1][coluna_referencia.index(posi_atual_p[1])] = ESPACO
                    tabuleiro_cores[int(movimento_p[0]) - 1][coluna_referencia.index(movimento_p[1])] = turno

                    if turno == BRANCAS:
                        tabuleiro[int(movimento_p[0]) - 1][coluna_referencia.index(movimento_p[1])] = CAVALO_B
                    else:
                        tabuleiro[int(movimento_p[0]) - 1][coluna_referencia.index(movimento_p[1])] = CAVALO_P


posi_atual_p: str
movimento_p: str
turno = BRANCAS
tabuleiro = []
tabuleiro_cores = []
coluna_tabuleiro = [' ', 'a ', ' b', '  c',  '  d', '  e', '  f ', ' g', '  h']
coluna_referencia = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

montando_tabuleiro()
criar_referencia_cor()

while True:
    imprime_tabuleiro()
    print(MSG_TURNO.format(turno.upper()))
    coordenada_jogada = input()
    if validar_jogada(coordenada_jogada):
        jogar()
    else:
        print(0)
    trocar_turno()
