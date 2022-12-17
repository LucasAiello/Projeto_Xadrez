from peças import *


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


def atualizar_referencia_captura(cor):
    global tabuleiro
    global tabuleiro_captura_verdes
    global tabuleiro_captura_azuis

    def verificar_horizontal_vertical():
        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO:
                if tabuleiro_cores[i + l][j] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i + l][j] = 1
                    else:
                        tabuleiro_captura_azuis[i + l][j] = 1
                elif tabuleiro_cores[i + l][j] == cor or \
                        (cor == VERDES and tabuleiro[i + l][j] == REI_A) or (
                        cor == AZUIS and tabuleiro[i + l][j] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i + l][j] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i + l][j] = 1
                        break
                else:
                    break

        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0:
                if tabuleiro_cores[i - l][j] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i - l][j] = 1
                    else:
                        tabuleiro_captura_azuis[i - l][j] = 1
                elif tabuleiro_cores[i - l][j] == cor or \
                        (cor == VERDES and tabuleiro[i - l][j] == REI_A) or (
                        cor == AZUIS and tabuleiro[i - l][j] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i - l][j] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i - l][j] = 1
                        break
                else:
                    break

        for l in range(1, TAMANHO_TABULEIRO):
            if j + l < TAMANHO_TABULEIRO:
                if tabuleiro_cores[i][j + l] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i][j + l] = 1
                    else:
                        tabuleiro_captura_azuis[i][j + l] = 1
                elif tabuleiro_cores[i][j + l] == cor or (cor == VERDES and tabuleiro[i][j + j] == REI_A) or (
                        cor == AZUIS and tabuleiro[i][j + j] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i][j + l] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i][j + l] = 1
                        break
                else:
                    break

        for l in range(1, TAMANHO_TABULEIRO):
            if j - l >= 0:
                if tabuleiro_cores[i][j - l] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i][j - l] = 1
                    else:
                        tabuleiro_captura_azuis[i][j - l] = 1
                elif tabuleiro_cores[i][j - l] == cor or (cor == VERDES and tabuleiro[i][j - j] == REI_A) or (
                        cor == AZUIS and tabuleiro[i][j - j] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i][j - l] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i][j - l] = 1
                        break
                else:
                    break

    def verificar_diagonal():
        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO and j + l < TAMANHO_TABULEIRO:
                if tabuleiro_cores[i + l][j + l] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i + l][j + l] = 1
                    else:
                        tabuleiro_captura_azuis[i + l][j + l] = 1
                elif tabuleiro_cores[i + l][j + l] == cor or \
                        (cor == VERDES and tabuleiro[i + l][j + l] == REI_A) or (
                        cor == AZUIS and tabuleiro[i + l][j + l] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i + l][j + l] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i + l][j + l] = 1
                        break
                else:
                    break

        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO and j - l >= 0:
                if tabuleiro_cores[i + l][j - l] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i + l][j - l] = 1
                    else:
                        tabuleiro_captura_azuis[i + l][j - l] = 1
                elif tabuleiro_cores[i + l][j - l] == cor or \
                        (cor == VERDES and tabuleiro[i + l][j - l] == REI_A) or (
                        cor == AZUIS and tabuleiro[i + l][j - l] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i + l][j - l] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i + l][j - l] = 1
                        break
                else:
                    break

        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0 and j + l < TAMANHO_TABULEIRO:
                if tabuleiro_cores[i - l][j + l] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i - l][j + l] = 1
                    else:
                        tabuleiro_captura_azuis[i - l][j + l] = 1
                elif tabuleiro_cores[i - l][j + l] == cor or \
                        (cor == VERDES and tabuleiro[i - l][j + l] == REI_A) or (
                        cor == AZUIS and tabuleiro[i - l][j + l] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i - l][j + l] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i - l][j + l] = 1
                        break
                else:
                    break

        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0 and j - l >= 0:
                if tabuleiro_cores[i - l][j - l] == ESPACO:
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i - l][j - l] = 1
                    else:
                        tabuleiro_captura_azuis[i - l][j - l] = 1
                elif tabuleiro_cores[i - l][j - l] == cor or \
                        (cor == VERDES and tabuleiro[i - l][j - l] == REI_A) or (
                        cor == AZUIS and tabuleiro[i - l][j - l] == REI_V):
                    if cor == VERDES:
                        tabuleiro_captura_verdes[i - l][j - l] = 1
                        break
                    else:
                        tabuleiro_captura_azuis[i - l][j - l] = 1
                        break
                else:
                    break

    if cor == VERDES:
        tabuleiro_captura_verdes = [[0 for x in range(TAMANHO_TABULEIRO)] for y in range(TAMANHO_TABULEIRO)]
    else:
        tabuleiro_captura_azuis = [[0 for x in range(TAMANHO_TABULEIRO)] for y in range(TAMANHO_TABULEIRO)]

    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            if tabuleiro_cores[i][j] == cor:
                if tabuleiro[i][j] == PEAO_V or tabuleiro[i][j] == PEAO_A:
                    if tabuleiro[i][j] == PEAO_V:
                        if i - 1 >= 0 and j + 1 < TAMANHO_TABULEIRO:
                            if tabuleiro_cores[i-1][j+1] == cor or tabuleiro_cores[i-1][j+1] == ESPACO or tabuleiro[i-1][j+1] == REI_A:
                                tabuleiro_captura_verdes[i - 1][j + 1] = 1
                        if i - 1 >= 0 and j - 1 >= 0:
                            if tabuleiro_cores[i - 1][j - 1] == cor or tabuleiro_cores[i - 1][j - 1] == ESPACO or tabuleiro[i - 1][j - 1] == REI_A:
                                tabuleiro_captura_verdes[i - 1][j - 1] = 1

                    else:
                        if i + 1 < TAMANHO_TABULEIRO and j + 1 < TAMANHO_TABULEIRO:
                            if tabuleiro_cores[i + 1][j + 1] == cor or tabuleiro_cores[i + 1][j + 1] == ESPACO or \
                                    tabuleiro[i + 1][j + 1] == REI_V:
                                tabuleiro_captura_azuis[i + 1][j + 1] = 1
                        if i + 1 < TAMANHO_TABULEIRO and j - 1 >= 0:
                            if tabuleiro_cores[i + 1][j - 1] == cor or tabuleiro_cores[i + 1][j - 1] == ESPACO or \
                                    tabuleiro[i + 1][j - 1] == REI_V:
                                tabuleiro_captura_azuis[i + 1][j - 1] = 1

                elif tabuleiro[i][j] == CAVALO_V or tabuleiro[i][j] == CAVALO_A:
                    for l in range(-2, 3, 1):
                        if l != 0:
                            for c in range(-2, 3, 1):
                                if c != 0 and l + c != 0 and l != c:
                                    if (j+c >= 0 and j+c < TAMANHO_TABULEIRO) and (i+l >= 0 and i+l < TAMANHO_TABULEIRO):
                                        if tabuleiro_cores[i+l][j+c] == ESPACO or tabuleiro_cores[i+l][j+c] == cor or \
                                                (cor == VERDES and tabuleiro[i+l][j+c] == REI_A) or (cor == AZUIS and tabuleiro[i+l][j+c] == REI_V):
                                            if cor == VERDES:
                                                tabuleiro_captura_verdes[i+l][j+c] = 1
                                            else:
                                                tabuleiro_captura_azuis[i + l][j + c] = 1

                elif tabuleiro[i][j] == TORRE_V or tabuleiro[i][j] == TORRE_A:
                    verificar_horizontal_vertical()

                elif tabuleiro[i][j] == BISPO_V or tabuleiro[i][j] == BISPO_A:
                    verificar_diagonal()

                elif tabuleiro[i][j] == RAINHA_V or tabuleiro[i][j] == RAINHA_A:
                    verificar_horizontal_vertical()
                    verificar_diagonal()

                elif tabuleiro[i][j] == REI_V or tabuleiro[i][j] == REI_A:
                    for l in range(-1, 2):
                        for c in range(-1, 2):
                            if (i + l >= 0 and i+l < TAMANHO_TABULEIRO) and (j + c >= 0 and j+c < TAMANHO_TABULEIRO):
                                if tabuleiro_cores[i + l][j + c] == ESPACO or tabuleiro_cores[i + l][j + c] == cor:
                                    if cor == VERDES:
                                        tabuleiro_captura_verdes[i + l][j + c] = 1
                                    else:
                                        tabuleiro_captura_azuis[i + l][j + c] = 1


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


def jogar():
    global valido
    valido = False

    if tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_A and turno == AZUIS:

        if verificar_peao(posi_atual_p, movimento_p):
            mover_peça("peão", posi_atual_p, movimento_p, turno)
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O peão"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_A and turno == AZUIS:

        if verificar_cavalo(posi_atual_p, movimento_p, turno):
            mover_peça("cavalo", posi_atual_p, movimento_p, turno)
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O cavalo"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_A and turno == AZUIS:

        if verificar_torre(posi_atual_p, movimento_p, turno):
            mover_peça("torre", posi_atual_p, movimento_p, turno)
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("A torre"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_A and turno == AZUIS:

        if verificar_rei(posi_atual_p, movimento_p, turno):
            mover_peça("rei", posi_atual_p, movimento_p, turno)
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O rei"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_A and turno == AZUIS:

        if verificar_bispo(posi_atual_p, movimento_p, turno):
            mover_peça("bispo", posi_atual_p, movimento_p, turno)
            valido = True

        else:
            print(MSG_MOVIMENTO_INVALIDO.format("O bispo"))

    elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_A and turno == AZUIS:

        if verificar_bispo(posi_atual_p, movimento_p, turno) or verificar_torre(posi_atual_p, movimento_p, turno):
            mover_peça("rainha", posi_atual_p, movimento_p, turno)
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



valido = False
posi_atual_p: str
movimento_p: str
turno = VERDES
tabuleiro_captura_verdes = []
tabuleiro_captura_azuis = []

montando_tabuleiro()
criar_referencia_cor()

while True:
    atualizar_referencia_captura(AZUIS)
    atualizar_referencia_captura(VERDES)
    imprime_tabuleiro()

    for i in range(TAMANHO_TABULEIRO):
        print(*tabuleiro_captura_verdes[i])

    print()

    for i in range(TAMANHO_TABULEIRO):
        print(*tabuleiro_captura_azuis[i])

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
