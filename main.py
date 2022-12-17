from constantes import *


def montando_tabuleiro():
    global tabuleiro
    pecas_brancas = [TORRE_V, CAVALO_V, BISPO_V, RAINHA_V, REI_V, BISPO_V, CAVALO_V, TORRE_V]
    pecas_pretas = [TORRE_A, CAVALO_A, BISPO_A, RAINHA_A, REI_A, BISPO_A, CAVALO_A, TORRE_A]

    for i in range(TAMANHO_TABULEIRO):
        tabuleiro.append([])
        for j in range(TAMANHO_TABULEIRO):
            if i <= 1 or i >= 6:
                if i == 1:
                    tabuleiro[i].append(PEAO_A)
                elif i == 0:
                    for h in range(TAMANHO_TABULEIRO):
                        tabuleiro[i].append(pecas_pretas[h])
                elif i == 6:
                    tabuleiro[i].append(PEAO_V)
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
                linha.append(AZUIS)
            elif i == 6 or i == 7:
                linha.append(VERDES)
            else:
                linha.append(ESPACO)
        tabuleiro_cores.append(linha)


def imprime_tabuleiro():
    for i in range(TAMANHO_TABULEIRO):
        if i == 0:
            for h in range(TAMANHO_TABULEIRO+1):
                print(ESPACO, end=COLUNA_TABULEIRO[h])
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
    if turno == VERDES:
        turno = AZUIS
    else:
        turno = VERDES


def validar_jogada():
    global posi_atual_p
    global movimento_p

    if posi_atual_p[0].isnumeric() and movimento_p[0].isnumeric():
        if int(movimento_p[0])-1 >= 0 and int(movimento_p[0])-1 <= 7:
            for i in range(len(COLUNA_REFERENCIA)):
                if movimento_p[1] == COLUNA_REFERENCIA[i]:
                    return True


def verificar_peao():
    global posi_atual_p
    global movimento_p

    valido = False

    if movimento_p[1] == posi_atual_p[1]:
        if int(movimento_p[0]) == int(posi_atual_p[0]) - 1:
            if tabuleiro_cores[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == ESPACO:
                valido = True

        elif int(movimento_p[0]) == int(posi_atual_p[0]) - 2 and int(posi_atual_p[0]) == 7:
            if tabuleiro_cores[int(movimento_p[0])][COLUNA_REFERENCIA.index(movimento_p[1])] == ESPACO:
                valido = True

    elif COLUNA_REFERENCIA.index(posi_atual_p[1]) == COLUNA_REFERENCIA.index(movimento_p[1]) + 1 or \
            COLUNA_REFERENCIA.index(posi_atual_p[1]) == COLUNA_REFERENCIA.index(movimento_p[1]) - 1:
        if int(movimento_p[0]) == int(posi_atual_p[0]) - 1 and tabuleiro_cores[int(movimento_p[0]) - 1] \
                [COLUNA_REFERENCIA.index(movimento_p[1])] == AZUIS:
            valido = True

    if movimento_p[1] == posi_atual_p[1]:
        if int(movimento_p[0]) == int(posi_atual_p[0]) + 1:
            if tabuleiro_cores[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == ESPACO:
                valido = True

        elif int(movimento_p[0]) == int(posi_atual_p[0]) + 2 and int(posi_atual_p[0]) == 2:
            if tabuleiro_cores[int(movimento_p[0]) - 2][COLUNA_REFERENCIA.index(movimento_p[1])] == ESPACO:
                valido = True

    elif COLUNA_REFERENCIA.index(posi_atual_p[1]) == COLUNA_REFERENCIA.index(movimento_p[1]) + 1 or \
            COLUNA_REFERENCIA.index(posi_atual_p[1]) == COLUNA_REFERENCIA.index(movimento_p[1]) - 1:
        if int(movimento_p[0]) == int(posi_atual_p[0]) + 1 and tabuleiro_cores[int(movimento_p[0]) - 1] \
                [COLUNA_REFERENCIA.index(movimento_p[1])] == VERDES:
            valido = True

    if valido:
        return True


def verificar_cavalo():
    valido = False
    if tabuleiro_cores[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] != turno:
        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                if (int(movimento_p[0]) == int(posi_atual_p[0]) + i and COLUNA_REFERENCIA.index(
                        movimento_p[1]) == COLUNA_REFERENCIA.index(posi_atual_p[1]) + j) or \
                        (int(movimento_p[0]) == int(posi_atual_p[0]) + j and COLUNA_REFERENCIA.index(
                            movimento_p[1]) == COLUNA_REFERENCIA.index(posi_atual_p[1]) + i):
                    valido = True

    if valido:
        return True


def verificar_torre():
    global posi_atual_p
    global movimento_p
    valido = False
    cont = 0

    if tabuleiro_cores[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == turno and \
            tabuleiro_cores[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] != turno:
        if posi_atual_p[0] == movimento_p[0]:
            if COLUNA_REFERENCIA.index(posi_atual_p[1]) > COLUNA_REFERENCIA.index(movimento_p[1]):
                for i in range(COLUNA_REFERENCIA.index(movimento_p[1]) + 1, COLUNA_REFERENCIA.index(posi_atual_p[1])):
                    if tabuleiro_cores[int(posi_atual_p[0]) - 1][i] == ESPACO:
                        cont += 1
            else:
                for i in range(COLUNA_REFERENCIA.index(posi_atual_p[1]) + 1, COLUNA_REFERENCIA.index(movimento_p[1])):
                    if tabuleiro_cores[int(posi_atual_p[0]) - 1][i] == ESPACO:
                        cont += 1

            if cont == abs(COLUNA_REFERENCIA.index(posi_atual_p[1]) - COLUNA_REFERENCIA.index(movimento_p[1])) - 1:
                valido = True

        elif posi_atual_p[1] == movimento_p[1]:
            if int(posi_atual_p[0]) > int(movimento_p[0]):
                for i in range(int(movimento_p[0]), int(posi_atual_p[0]) - 1):
                    if tabuleiro_cores[i][COLUNA_REFERENCIA.index(posi_atual_p[1])] == ESPACO:
                        cont += 1
            else:
                for i in range(int(posi_atual_p[0]), int(movimento_p[0]) - 1):
                    if tabuleiro_cores[i][COLUNA_REFERENCIA.index(posi_atual_p[1])] == ESPACO:
                        cont += 1

            if cont == abs(int(posi_atual_p[0]) - int(movimento_p[0])) - 1:
                valido = True

    if valido:
        return True


def verificar_rei():
    valido = False

    if tabuleiro_cores[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] != turno:
        if tabuleiro_cores[int(posi_atual_p[0]) - 1] == tabuleiro_cores[int(movimento_p[0]) - 1] or (
                tabuleiro_cores[int(posi_atual_p[0]) - 1] == tabuleiro_cores[int(movimento_p[0])]) or \
                tabuleiro_cores[int(posi_atual_p[0]) - 1] == tabuleiro_cores[int(movimento_p[0]) - 2]:
            if COLUNA_REFERENCIA.index(posi_atual_p[1]) == COLUNA_REFERENCIA.index(movimento_p[1]):
                valido = True

            elif COLUNA_REFERENCIA.index(posi_atual_p[1]) == COLUNA_REFERENCIA.index(movimento_p[1]) + 1:
                valido = True

            elif COLUNA_REFERENCIA.index(posi_atual_p[1]) == COLUNA_REFERENCIA.index(movimento_p[1]) - 1:
                valido = True

    if valido:
        return True


def verificar_bispo():
    valido = False
    cont = 0
    if tabuleiro_cores[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] != turno:
        if int(posi_atual_p[0]) - 1 > int(movimento_p[0]) - 1:
            if COLUNA_REFERENCIA.index(posi_atual_p[1]) > COLUNA_REFERENCIA.index(movimento_p[1]):
                x = (int(posi_atual_p[0]) - 1) - (int(movimento_p[0]) - 1)
                v = int(movimento_p[0])
                for i in range(COLUNA_REFERENCIA.index(movimento_p[1]) + 1, COLUNA_REFERENCIA.index(posi_atual_p[1])):
                    if tabuleiro_cores[v][i] != ESPACO:
                        cont += 1
                    v += 1
                if cont == 0:
                    if COLUNA_REFERENCIA.index(posi_atual_p[1]) - x == COLUNA_REFERENCIA.index(movimento_p[1]):
                        valido = True

            elif COLUNA_REFERENCIA.index(posi_atual_p[1]) < COLUNA_REFERENCIA.index(movimento_p[1]):
                x = (int(posi_atual_p[0]) - 1) - (int(movimento_p[0]) - 1)
                v = int(movimento_p[0])
                for i in range(COLUNA_REFERENCIA.index(movimento_p[1]) - 1, COLUNA_REFERENCIA.index(posi_atual_p[1]),
                               -1):
                    if tabuleiro_cores[v][i] != ESPACO:
                        cont += 1
                    v += 1
                if cont == 0:
                    if COLUNA_REFERENCIA.index(posi_atual_p[1]) + x == COLUNA_REFERENCIA.index(movimento_p[1]):
                        valido = True

        elif int(posi_atual_p[0]) - 1 < int(movimento_p[0]) - 1:
            if COLUNA_REFERENCIA.index(posi_atual_p[1]) > COLUNA_REFERENCIA.index(movimento_p[1]):
                x = (int(movimento_p[0]) - 1) - (int(posi_atual_p[0]) - 1)
                v = int(posi_atual_p[0])
                for i in range(COLUNA_REFERENCIA.index(posi_atual_p[1]) - 1, COLUNA_REFERENCIA.index(movimento_p[1]),
                               -1):
                    if tabuleiro_cores[v][i] != ESPACO:
                        cont += 1
                    v += 1
                if cont == 0:
                    if COLUNA_REFERENCIA.index(posi_atual_p[1]) - x == COLUNA_REFERENCIA.index(movimento_p[1]):
                        valido = True

            elif COLUNA_REFERENCIA.index(posi_atual_p[1]) < COLUNA_REFERENCIA.index(movimento_p[1]):
                x = (int(movimento_p[0]) - 1) - (int(posi_atual_p[0]) - 1)
                v = int(posi_atual_p[0])
                for i in range(COLUNA_REFERENCIA.index(posi_atual_p[1]) + 1, COLUNA_REFERENCIA.index(movimento_p[1])):
                    if tabuleiro_cores[v][i] != ESPACO:
                        cont += 1
                    v += 1
                if cont == 0:
                    if COLUNA_REFERENCIA.index(posi_atual_p[1]) + x == COLUNA_REFERENCIA.index(movimento_p[1]):
                        valido = True

    if valido:
        return True


def mover_peça(peça):
    tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] = ESPACO
    tabuleiro_cores[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] = ESPACO
    tabuleiro_cores[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = turno

    if peça == "peão":
        if turno == VERDES:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = PEAO_V
        else:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = PEAO_A

    elif peça == "cavalo":
        if turno == VERDES:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = CAVALO_V
        else:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = CAVALO_A

    elif peça == "torre":
        if turno == VERDES:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = TORRE_V
        else:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = TORRE_A

    elif peça == "rei":
        if turno == VERDES:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = REI_V
        else:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = REI_A

    elif peça == "bispo":
        if turno == VERDES:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = BISPO_V
        else:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = BISPO_A

    elif peça == "rainha":
        if turno == VERDES:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = RAINHA_V
        else:
            tabuleiro[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] = RAINHA_A


def jogar():
    global valido
    valido = False
    if tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_A and turno == AZUIS:

        if verificar_peao():
            mover_peça("peão")
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O peão"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_A and turno == AZUIS:

        if verificar_cavalo():
            mover_peça("cavalo")
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O cavalo"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_A and turno == AZUIS:

        if verificar_torre():
            mover_peça("torre")
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("A torre"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_A and turno == AZUIS:

        if verificar_rei():
            mover_peça("rei")
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O rei"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_A and turno == AZUIS:

        if verificar_bispo():
            mover_peça("bispo")
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O bispo"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_A and turno == AZUIS:

        if verificar_bispo() or verificar_torre():
            mover_peça("rainha")
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("A rainha"))

    else:
        print(MSG_ESPAÇO_VAZIO)


def criar_posis(coordenada):
    global posi_atual_p
    global movimento_p

    if len(coordenada) == 5 and coordenada[2 == " "]:
        posi_atual_p = coordenada[:2].lower()
        movimento_p = coordenada[3:].lower()
    elif len(coordenada) == 4:
        posi_atual_p = coordenada[:2].lower()
        movimento_p = coordenada[2:].lower()
    else:
        return False


posi_atual_p: str
movimento_p: str
turno = VERDES
valido = False
tabuleiro = []
tabuleiro_cores = []

montando_tabuleiro()
criar_referencia_cor()

while True:
    imprime_tabuleiro()
    print(MSG_TURNO.format(turno.upper()))
    coordenada_jogada = input()

    if criar_posis(coordenada_jogada) != False:

        if validar_jogada():
            jogar()
            if valido:
                trocar_turno()
        else:
            print(MSG_COMANDO_INVALIDO)
    else:
        print(MSG_COMANDO_INVALIDO)
