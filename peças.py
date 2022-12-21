from constantes import *


def verificar_peao(inicial, movimento, turno):
    v = False

    if turno == VERDES:
        if COLUNA_REFERENCIA.index(inicial[1]) == COLUNA_REFERENCIA.index(movimento[1]):
            if tabuleiro[int(movimento[0])-1][COLUNA_REFERENCIA.index(movimento[1])] == ESPACO:
                if int(inicial[0])-1 == 6 and int(inicial[0])-2 == int(movimento[0]):
                        v = True
                elif int(inicial[0])-1 == int(movimento[0]):
                        v = True
        else:
            if COLUNA_REFERENCIA.index(movimento[1]) == COLUNA_REFERENCIA.index(inicial[1])-1:
                if tabuleiro_cores[int(movimento[0])-1][COLUNA_REFERENCIA.index(movimento[1])] == AZUIS:
                    v = True
            elif COLUNA_REFERENCIA.index(movimento[1]) == COLUNA_REFERENCIA.index(inicial[1])+1:
                if tabuleiro_cores[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] == AZUIS:
                    v = True
    else:
        if COLUNA_REFERENCIA.index(inicial[1]) == COLUNA_REFERENCIA.index(movimento[1]):
            if tabuleiro[int(movimento[0])-1][COLUNA_REFERENCIA.index(movimento[1])] == ESPACO:
                if int(inicial[0])-1 == 1 and int(inicial[0])+2 == int(movimento[0]):
                        v = True
                elif int(inicial[0]) == int(movimento[0])-1:
                        v = True
        else:
            if COLUNA_REFERENCIA.index(movimento[1]) == COLUNA_REFERENCIA.index(inicial[1])-1:
                if tabuleiro_cores[int(movimento[0])-1][COLUNA_REFERENCIA.index(movimento[1])] == VERDES:
                    v = True
            elif COLUNA_REFERENCIA.index(movimento[1]) == COLUNA_REFERENCIA.index(inicial[1])+1:
                if tabuleiro_cores[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] == VERDES:
                    v = True

    if v:
        return True


def verificar_cavalo(inicial, movimento, turno):
    v = False
    if tabuleiro_cores[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] != turno:
        for i in range(-2, 3, 4):
            for j in range(-1, 2, 2):
                if (int(movimento[0]) == int(inicial[0]) + i and COLUNA_REFERENCIA.index(
                        movimento[1]) == COLUNA_REFERENCIA.index(inicial[1]) + j) or \
                        (int(movimento[0]) == int(inicial[0]) + j and COLUNA_REFERENCIA.index(
                            movimento[1]) == COLUNA_REFERENCIA.index(inicial[1]) + i):
                    v = True

    if v:
        return True


def verificar_torre(inicial, movimento, turno):
    v = False
    cont = 0

    if tabuleiro_cores[int(inicial[0]) - 1][COLUNA_REFERENCIA.index(inicial[1])] == turno and \
            tabuleiro_cores[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] != turno:
        if inicial[0] == movimento[0]:
            if COLUNA_REFERENCIA.index(inicial[1]) > COLUNA_REFERENCIA.index(movimento[1]):
                for i in range(COLUNA_REFERENCIA.index(movimento[1]) + 1, COLUNA_REFERENCIA.index(inicial[1])):
                    if tabuleiro_cores[int(inicial[0]) - 1][i] == ESPACO:
                        cont += 1
            else:
                for i in range(COLUNA_REFERENCIA.index(inicial[1]) + 1, COLUNA_REFERENCIA.index(movimento[1])):
                    if tabuleiro_cores[int(inicial[0]) - 1][i] == ESPACO:
                        cont += 1

            if cont == abs(COLUNA_REFERENCIA.index(inicial[1]) - COLUNA_REFERENCIA.index(movimento[1])) - 1:
                v = True

        elif inicial[1] == movimento[1]:
            if int(inicial[0]) > int(movimento[0]):
                for i in range(int(movimento[0]), int(inicial[0]) - 1):
                    if tabuleiro_cores[i][COLUNA_REFERENCIA.index(inicial[1])] == ESPACO:
                        cont += 1
            else:
                for i in range(int(inicial[0]), int(movimento[0]) - 1):
                    if tabuleiro_cores[i][COLUNA_REFERENCIA.index(inicial[1])] == ESPACO:
                        cont += 1

            if cont == abs(int(inicial[0]) - int(movimento[0])) - 1:
                v = True

    if v:
        return True


def verificar_rei(inicial, movimento, turno):
    v = False

    if tabuleiro_cores[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] != turno:
        if tabuleiro_cores[int(inicial[0]) - 1] == tabuleiro_cores[int(movimento[0]) - 1] or (
                tabuleiro_cores[int(inicial[0]) - 1] == tabuleiro_cores[int(movimento[0])]) or \
                tabuleiro_cores[int(inicial[0]) - 1] == tabuleiro_cores[int(movimento[0]) - 2]:
            if COLUNA_REFERENCIA.index(inicial[1]) == COLUNA_REFERENCIA.index(movimento[1]):
                v = True

            elif COLUNA_REFERENCIA.index(inicial[1]) == COLUNA_REFERENCIA.index(movimento[1]) + 1:
                v = True

            elif COLUNA_REFERENCIA.index(inicial[1]) == COLUNA_REFERENCIA.index(movimento[1]) - 1:
                v = True

    if v:
        return True


def verificar_bispo(inicial, movimento, turno):
    cont = 0
    val = False

    if int(inicial[0]) - 1 > int(movimento[0]) - 1:
        if COLUNA_REFERENCIA.index(inicial[1]) > COLUNA_REFERENCIA.index(movimento[1]):
            x = (int(inicial[0]) - 1) - (int(movimento[0]) - 1)
            v = int(movimento[0])
            for i in range(COLUNA_REFERENCIA.index(movimento[1]) + 1, COLUNA_REFERENCIA.index(inicial[1])):
                if tabuleiro_cores[v][i] != ESPACO:
                    cont += 1
                v += 1
            if cont == 0:
                if COLUNA_REFERENCIA.index(inicial[1]) - x == COLUNA_REFERENCIA.index(movimento[1]):
                    val = True

        elif COLUNA_REFERENCIA.index(inicial[1]) < COLUNA_REFERENCIA.index(movimento[1]):
            x = (int(inicial[0]) - 1) - (int(movimento[0]) - 1)
            v = int(movimento[0])
            for i in range(COLUNA_REFERENCIA.index(movimento[1]) - 1, COLUNA_REFERENCIA.index(inicial[1]),
                           -1):
                try:
                    if tabuleiro_cores[v][i] != ESPACO:
                        cont += 1
                    v += 1
                except IndexError:
                    pass
            if cont == 0:
                if COLUNA_REFERENCIA.index(inicial[1]) + x == COLUNA_REFERENCIA.index(movimento[1]):
                    val = True
    elif int(inicial[0]) - 1 < int(movimento[0]) - 1:
        if COLUNA_REFERENCIA.index(inicial[1]) > COLUNA_REFERENCIA.index(movimento[1]):
            x = (int(movimento[0]) - 1) - (int(inicial[0]) - 1)
            v = int(inicial[0])
            for i in range(COLUNA_REFERENCIA.index(inicial[1]) - 1, COLUNA_REFERENCIA.index(movimento[1]),
                           -1):
                if tabuleiro_cores[v][i] != ESPACO:
                    cont += 1
                v += 1
            if cont == 0:
                if COLUNA_REFERENCIA.index(inicial[1]) - x == COLUNA_REFERENCIA.index(movimento[1]):
                    val = True
        elif COLUNA_REFERENCIA.index(inicial[1]) < COLUNA_REFERENCIA.index(movimento[1]):
            x = (int(movimento[0]) - 1) - (int(inicial[0]) - 1)
            v = int(inicial[0])
            for i in range(COLUNA_REFERENCIA.index(inicial[1]) + 1, COLUNA_REFERENCIA.index(movimento[1])):
                if tabuleiro_cores[v][i] != ESPACO:
                    cont += 1
                v += 1
            if cont == 0:
                if COLUNA_REFERENCIA.index(inicial[1]) + x == COLUNA_REFERENCIA.index(movimento[1]):
                    val = True

    if val:
        return True


def mover_peça(peça, inicial, movimento, turno):
    global tabuleiro
    global tabuleiro_cores

    tabuleiro[int(inicial[0]) - 1][COLUNA_REFERENCIA.index(inicial[1])] = ESPACO
    tabuleiro_cores[int(inicial[0]) - 1][COLUNA_REFERENCIA.index(inicial[1])] = ESPACO
    tabuleiro_cores[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = turno

    if peça == P_PEAO:
        if turno == VERDES:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = PEAO_V
        else:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = PEAO_A

    elif peça == P_CAVALO:
        if turno == VERDES:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = CAVALO_V
        else:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = CAVALO_A

    elif peça == P_TORRE:
        if turno == VERDES:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = TORRE_V
        else:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = TORRE_A

    elif peça == P_REI:
        if turno == VERDES:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = REI_V
            posis_reis[0][0] = int(movimento[0]) - 1
            posis_reis[0][1] = COLUNA_REFERENCIA.index(movimento[1])
        else:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = REI_A
            posis_reis[1][0] = int(movimento[0]) - 1
            posis_reis[1][1] = COLUNA_REFERENCIA.index(movimento[1])

    elif peça == P_BISPO:
        if turno == VERDES:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = BISPO_V
        else:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = BISPO_A

    elif peça == P_RAINHA:
        if turno == VERDES:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = RAINHA_V
        else:
            tabuleiro[int(movimento[0]) - 1][COLUNA_REFERENCIA.index(movimento[1])] = RAINHA_A


tabuleiro = []
tabuleiro_cores = []
posis_reis = [[7, 4], [0, 4]]
