from tabuleiro import *
from time import sleep


def atualizar_referencia_captura(cor):
    global tabuleiro
    global tabuleiro_captura_verdes
    global tabuleiro_captura_azuis

    def verificar_horizontal_vertical():
        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i + l][j] != 2) or (cor == AZUIS and tabuleiro_captura_azuis[i + l][j] != 2):
                    if tabuleiro_cores[i + l][j] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j] = 1
                        else:
                            tabuleiro_captura_azuis[i + l][j] = 1
                    elif tabuleiro_cores[i + l][j] == cor:
                        if cor == VERDES:
                            if tabuleiro[i + l][j] != REI_V:
                                tabuleiro_captura_verdes[i + l][j] = 1
                                break
                        else:
                            if tabuleiro[i + l][j] != REI_A:
                                tabuleiro_captura_azuis[i + l][j] = 1
                                break
                    elif (cor == VERDES and tabuleiro[i + l][j] == REI_A) or (
                            cor == AZUIS and tabuleiro[i + l][j] == REI_V):
                        for k in range(0, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i + k][j] = 2
                            else:
                                tabuleiro_captura_azuis[i + k][j] = 2
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j] = 1
                            break
                        else:
                            tabuleiro_captura_azuis[i + l][j] = 1
                            break

        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i - l][j] != 2) or (cor == AZUIS and tabuleiro_captura_azuis[i - l][j] != 2):
                    if tabuleiro_cores[i - l][j] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j] = 1
                        else:
                            tabuleiro_captura_azuis[i - l][j] = 1
                    elif tabuleiro_cores[i - l][j] == cor:
                        if cor == VERDES:
                            if tabuleiro[i - l][j] != REI_V:
                                tabuleiro_captura_verdes[i - l][j] = 1
                                break
                        else:
                            if tabuleiro[i - l][j] != REI_A:
                                tabuleiro_captura_azuis[i - l][j] = 1
                                break
                    elif (cor == VERDES and tabuleiro[i - l][j] == REI_A) or (
                            cor == AZUIS and tabuleiro[i - l][j] == REI_V):
                        for k in range(0, l + 1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i - k][j] = 2
                            else:
                                tabuleiro_captura_azuis[i - k][j] = 2
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j] = 1
                            break
                        else:
                            tabuleiro_captura_azuis[i - l][j] = 1
                            break

        for l in range(1, TAMANHO_TABULEIRO):
            if j + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i][j + l] != 2) or (cor == AZUIS and tabuleiro_captura_azuis[i][j + l] != 2):
                    if tabuleiro_cores[i][j + l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j + l] = 1
                        else:
                            tabuleiro_captura_azuis[i][j + l] = 1
                    elif tabuleiro_cores[i][j + l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i][j + l] != REI_V:
                                tabuleiro_captura_verdes[i][j + l] = 1
                                break
                        else:
                            if tabuleiro[i][j + l] != REI_A:
                                tabuleiro_captura_azuis[i][j + l] = 1
                                break
                    elif (cor == VERDES and tabuleiro[i][j + l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i][j + l] == REI_V):
                        for k in range(0, l + 1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i][j + k] = 2
                            else:
                                tabuleiro_captura_azuis[i][j + k] = 2
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j + l] = 1
                            break
                        else:
                            tabuleiro_captura_azuis[i][j + l] = 1
                            break

        for l in range(1, TAMANHO_TABULEIRO):
            if j - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i][j - l] != 2) or (cor == AZUIS and tabuleiro_captura_azuis[i][j - l] != 2):
                    if tabuleiro_cores[i][j - l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j - l] = 1
                        else:
                            tabuleiro_captura_azuis[i][j - l] = 1
                    elif tabuleiro_cores[i][j - l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i][j - l] != REI_V:
                                tabuleiro_captura_verdes[i][j - l] = 1
                                break
                        else:
                            if tabuleiro[i][j - l] != REI_A:
                                tabuleiro_captura_azuis[i][j - l] = 1
                                break
                    elif (cor == VERDES and tabuleiro[i][j - l] == REI_A) or (
                                    cor == AZUIS and tabuleiro[i][j - l] == REI_V):
                        for k in range(0, l + 1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i][j - k] = 2
                            else:
                                tabuleiro_captura_azuis[i][j - k] = 2
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j - l] = 1
                            break
                        else:
                            tabuleiro_captura_azuis[i][j - l] = 1
                            break

    def verificar_diagonal():
        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO and j + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i + l][j + l] != 2) or (cor == AZUIS and tabuleiro_captura_azuis[i + l][j + l] != 2):
                    if tabuleiro_cores[i + l][j + l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j + l] = 1
                        else:

                            tabuleiro_captura_azuis[i + l][j + l] = 1
                    elif tabuleiro_cores[i + l][j + l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i + l][j + l] != REI_V:
                                tabuleiro_captura_verdes[i + l][j + l] = 1
                            break
                        else:
                            if tabuleiro[i + l][j + l] != REI_A:
                                tabuleiro_captura_azuis[i + l][j + l] = 1
                            break

                    elif (cor == VERDES and tabuleiro[i + l][j + l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i + l][j + l] == REI_V):
                        for k in range(0, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i+k][j + k] = 2
                            else:
                                tabuleiro_captura_azuis[i+k][j + k] = 2
                        break
                    else:
                        break

        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO and j - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i + l][j - l] != 2) or (
                        cor == AZUIS and tabuleiro_captura_azuis[i + l][j - l] != 2):
                    if tabuleiro_cores[i + l][j - l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j - l] = 1
                        else:
                            tabuleiro_captura_azuis[i + l][j - l] = 1
                    elif tabuleiro_cores[i + l][j - l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i + l][j - l] != REI_V:
                                tabuleiro_captura_verdes[i + l][j - l] = 1
                            break
                        else:
                            if tabuleiro[i + l][j - l] != REI_A:
                                tabuleiro_captura_azuis[i + l][j - l] = 1
                            break
                    elif (cor == VERDES and tabuleiro[i + l][j - l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i + l][j - l] == REI_V):
                        for k in range(0, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i+k][j - k] = 2
                            else:
                                tabuleiro_captura_azuis[i+k][j - k] = 2
                        break
                    else:
                        break


        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0 and j + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i - l][j + l] != 2) or (cor == AZUIS and tabuleiro_captura_azuis[i - l][j + l] != 2):
                    if tabuleiro_cores[i - l][j + l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j + l] = 1
                        else:
                            tabuleiro_captura_azuis[i - l][j + l] = 1
                    elif tabuleiro_cores[i - l][j + l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i - l][j + l] != REI_V:
                                tabuleiro_captura_verdes[i - l][j + l] = 1
                            break
                        else:
                            if tabuleiro[i - l][j + l] != REI_A:
                                tabuleiro_captura_azuis[i - l][j + l] = 1
                            break
                    elif (cor == VERDES and tabuleiro[i - l][j + l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i - l][j + l] == REI_V):
                        for k in range(0, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i - k][j + k] = 2
                            else:
                                tabuleiro_captura_azuis[i - k][j + k] = 2
                        break
                    else:
                        break

        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0 and j - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i - l][j - l] != 2) or (cor == AZUIS and tabuleiro_captura_azuis[i - l][j - l] != 2):
                    if tabuleiro_cores[i - l][j - l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j - l] = 1
                        else:
                            tabuleiro_captura_azuis[i - l][j - l] = 1
                    elif tabuleiro_cores[i - l][j - l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i - l][j - l] != REI_V:
                                tabuleiro_captura_verdes[i - l][j - l] = 1
                            break
                        else:
                            if tabuleiro[i - l][j - l] != REI_V:
                                tabuleiro_captura_azuis[i - l][j - l] = 1
                            break
                    elif (cor == VERDES and tabuleiro[i - l][j - l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i - l][j - l] == REI_V):
                        for k in range(0, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i - k][j - k] = 2
                            else:
                                tabuleiro_captura_azuis[i - k][j - k] = 2
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
                            if tabuleiro_captura_verdes[i - 1][j + 1] != 2:
                                if tabuleiro_cores[i-1][j+1] == cor or tabuleiro_cores[i-1][j+1] == ESPACO:
                                    if tabuleiro_captura_verdes[i - 1][j + 1] == 4:
                                        tabuleiro_captura_verdes[i - 1][j + 1] = 7
                                    elif tabuleiro_captura_verdes[i - 1][j + 1] == 0:
                                        tabuleiro_captura_verdes[i - 1][j + 1] = 3
                                elif tabuleiro_cores[i-1][j+1] == AZUIS:
                                    tabuleiro_captura_verdes[i - 1][j + 1] = 1
                        if i == 6:
                            if tabuleiro_cores[i - 1][j] == ESPACO:
                                if tabuleiro_captura_verdes[i - 1][j] != 2:
                                    if tabuleiro_cores[i - 1][j] == 3:
                                        tabuleiro_captura_verdes[i - 1][j] = 7
                                    elif tabuleiro_captura_verdes[i - 1][j] == 0:
                                        tabuleiro_captura_verdes[i - 1][j] = 4

                            if tabuleiro_cores[i - 2][j] == ESPACO:
                                if tabuleiro_captura_verdes[i - 2][j] != 2:
                                    if tabuleiro_cores[i - 2][j] == 3:
                                        tabuleiro_captura_verdes[i - 2][j] = 7
                                    elif tabuleiro_captura_verdes[i - 2][j] == 0:
                                        tabuleiro_captura_verdes[i - 2][j] = 4
                        else:
                            if tabuleiro_captura_verdes[i - 1][j] != 2:
                                if tabuleiro_cores[i - 1][j] == ESPACO:
                                    if tabuleiro_captura_verdes[i - 1][j] == 3:
                                        tabuleiro_captura_verdes[i - 1][j] = 7
                                    elif tabuleiro_captura_verdes[i - 1][j] == 0:
                                        tabuleiro_captura_verdes[i - 1][j] = 4

                        if i - 1 >= 0 and j - 1 >= 0:
                            if tabuleiro_captura_verdes[i - 1][j - 1] != 2:
                                if tabuleiro_cores[i - 1][j - 1] == cor or tabuleiro_cores[i - 1][j - 1] == ESPACO:
                                    if tabuleiro_captura_verdes[i - 1][j - 1] == 4:
                                        tabuleiro_captura_verdes[i - 1][j - 1] = 7
                                    elif tabuleiro_captura_verdes[i - 1][j - 1] == 0:
                                        tabuleiro_captura_verdes[i - 1][j - 1] = 3
                                elif tabuleiro_cores[i - 1][j - 1] == AZUIS:
                                    tabuleiro_captura_verdes[i - 1][j - 1] = 1

                    # Peões Azuis

                    else:
                        if i + 1 < TAMANHO_TABULEIRO and j + 1 < TAMANHO_TABULEIRO:
                            if tabuleiro_cores[i + 1][j + 1] == cor or tabuleiro_cores[i + 1][j + 1] == ESPACO:
                                if tabuleiro_captura_azuis[i + 1][j + 1] == 4:
                                    tabuleiro_captura_azuis[i + 1][j + 1] = 7
                                elif tabuleiro_captura_azuis[i + 1][j + 1] == 7:
                                    pass
                                else:
                                    tabuleiro_captura_azuis[i + 1][j + 1] = 3
                            elif tabuleiro_cores[i + 1][j + 1] == VERDES:
                                tabuleiro_captura_azuis[i + 1][j + 1] = 1

                        if i == 1:
                            if tabuleiro_cores[i + 1][j] == ESPACO:
                                if tabuleiro_captura_azuis[i + 1][j] == 3:
                                    tabuleiro_captura_azuis[i + 1][j] = 7
                                elif tabuleiro_captura_azuis[i + 1][j] == 7:
                                    pass
                                else:
                                    tabuleiro_captura_azuis[i + 1][j] = 4
                        if tabuleiro_captura_azuis[i + 2][j] != 2:
                            if tabuleiro_cores[i + 2][j] == ESPACO:
                                if tabuleiro_captura_azuis[i + 2][j] == 3:
                                    tabuleiro_captura_azuis[i + 2][j] = 7
                                elif tabuleiro_captura_azuis[i + 2][j] == 7:
                                    pass
                                else:
                                    tabuleiro_captura_azuis[i + 2][j] = 4
                        else:
                            if tabuleiro_captura_azuis[i + 1][j] != 2:
                                if tabuleiro_cores[i + 1][j] == ESPACO:
                                    if tabuleiro_captura_azuis[i + 1][j] == 3:
                                        tabuleiro_captura_azuis[i + 1][j] = 7
                                    elif tabuleiro_captura_azuis[i + 1][j] == 7:
                                        pass
                                    else:
                                        tabuleiro_captura_azuis[i + 1][j] = 4

                        if i + 1 < TAMANHO_TABULEIRO and j - 1 >= 0:
                            if tabuleiro_cores[i + 1][j - 1] == cor or tabuleiro_cores[i + 1][j - 1] == ESPACO:
                                if tabuleiro_captura_azuis[i + 1][j - 1] == 4:
                                    tabuleiro_captura_azuis[i + 1][j - 1] = 7
                                elif tabuleiro_captura_azuis[i + 1][j - 1] == 7:
                                    pass
                                else:
                                    tabuleiro_captura_azuis[i + 1][j - 1] = 3
                            elif tabuleiro_cores[i + 1][j - 1] == VERDES:
                                tabuleiro_captura_azuis[i + 1][j - 1] = 1

                elif tabuleiro[i][j] == CAVALO_V or tabuleiro[i][j] == CAVALO_A:
                    for l in range(-2, 3, 1):
                        if l != 0:
                            for c in range(-2, 3, 1):
                                if c != 0 and l + c != 0 and l != c:
                                    if (j+c >= 0 and j+c < TAMANHO_TABULEIRO) and (i+l >= 0 and i+l < TAMANHO_TABULEIRO):
                                        if (cor == VERDES and tabuleiro_captura_verdes[i + l][j + c] != 2) or (
                                                cor == AZUIS and tabuleiro_captura_azuis[i + l][j + c] != 2):
                                            if tabuleiro_cores[i+l][j+c] == ESPACO or (cor == VERDES and tabuleiro[i+l][j+c] == REI_A) or \
                                                    (cor == AZUIS and tabuleiro[i+l][j+c] == REI_V):
                                                if cor == VERDES:
                                                    tabuleiro_captura_verdes[i+l][j+c] = 1
                                                else:
                                                    tabuleiro_captura_azuis[i + l][j + c] = 1

                                            if tabuleiro_cores[i+l][j+c] == cor:
                                                if cor == VERDES and tabuleiro[i+l][j+c] != REI_V:
                                                    tabuleiro_captura_verdes[i+l][j+c] = 1
                                                else:
                                                    if cor == AZUIS and tabuleiro[i+l][j+c] != REI_A:
                                                        tabuleiro_captura_azuis[i + l][j + c] = 1

                elif tabuleiro[i][j] == TORRE_V or tabuleiro[i][j] == TORRE_A:
                    verificar_horizontal_vertical()

                elif tabuleiro[i][j] == BISPO_V or tabuleiro[i][j] == BISPO_A:
                    verificar_diagonal()

                elif tabuleiro[i][j] == RAINHA_V or tabuleiro[i][j] == RAINHA_A:
                    verificar_horizontal_vertical()
                    verificar_diagonal()

                """elif tabuleiro[i][j] == REI_V or tabuleiro[i][j] == REI_A:
                    for l in range(-1, 2):
                        for c in range(-1, 2):
                            if (i + l >= 0 and i+l < TAMANHO_TABULEIRO) and (j + c >= 0 and j+c < TAMANHO_TABULEIRO):
                                if tabuleiro_cores[i + l][j + c] == ESPACO or tabuleiro_cores[i + l][j + c] == cor:
                                    if cor == VERDES:
                                        tabuleiro_captura_verdes[i + l][j + c] = 5
                                    else:
                                        tabuleiro_captura_azuis[i + l][j + c] = 5
                                    pass"""


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
    global xeque
    global valido
    global peça_erro
    valido = False
    peça_erro = "nenhum"

    if (xeque and turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0])-1][COLUNA_REFERENCIA.index(movimento_p[1])] == 2) or \
        (xeque and turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == 2) or \
        xeque == False:
        if tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_V and turno == VERDES or \
                tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_A and turno == AZUIS:

            if verificar_peao(posi_atual_p, movimento_p):
                mover_peça("peão", posi_atual_p, movimento_p, turno)
                valido = True

            else:
                peça_erro = "O peão"

        elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_V and turno == VERDES or \
                tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_A and turno == AZUIS:

            if verificar_cavalo(posi_atual_p, movimento_p, turno):
                mover_peça("cavalo", posi_atual_p, movimento_p, turno)
                valido = True

            else:
                peça_erro = "O cavalo"

        elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_V and turno == VERDES or \
                tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_A and turno == AZUIS:

            if verificar_torre(posi_atual_p, movimento_p, turno):
                mover_peça("torre", posi_atual_p, movimento_p, turno)
                valido = True

            else:
                peça_erro = "A torre"

        elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_V and turno == VERDES or \
                tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_A and turno == AZUIS:

            if verificar_bispo(posi_atual_p, movimento_p, turno):
                mover_peça("bispo", posi_atual_p, movimento_p, turno)
                valido = True

            else:
                peça_erro = "O bispo"

        elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_V and turno == VERDES or \
                tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_A and turno == AZUIS:

            if verificar_bispo(posi_atual_p, movimento_p, turno) or verificar_torre(posi_atual_p, movimento_p, turno):
                mover_peça("rainha", posi_atual_p, movimento_p, turno)
                valido = True

            else:
                peça_erro = "A rainha"

    else:
        print("Você não pode mover a peça nessa posição, pois seu rei está em XEQUE.")

    if tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_A and turno == AZUIS:
        if (turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0])-1][COLUNA_REFERENCIA.index(movimento_p[1])] == 0 or \
                turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == 4):
            if verificar_rei(posi_atual_p, movimento_p, turno):
                mover_peça("rei", posi_atual_p, movimento_p, turno)
                valido = True
            else:
                peça_erro = "O rei"
        elif (turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == 0 or \
            turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == 4):
            if verificar_rei(posi_atual_p, movimento_p, turno):
                mover_peça("rei", posi_atual_p, movimento_p, turno)
                valido = True
            else:
                peça_erro = "O rei"

        else:
            print("O rei não pode ir para essa posição, pois entrará em XEQUE.")


def criar_posis(coordenada):
    global posi_atual_p
    global movimento_p

    if len(coordenada) == 5 and coordenada[2] == " ":
        posi_atual_p = coordenada[:2].lower()
        movimento_p = coordenada[3:].lower()

        return True
    elif len(coordenada) == 4:
        posi_atual_p = coordenada[:2].lower()
        movimento_p = coordenada[2:].lower()
        return True
    else:
        return False


def imprimir_tutorial():
    print("\nPara jogar entre com comandos na seguinte ordem:\n")
    sleep(2.5)
    print("Informe o número da linha com a letra da coluna da peça a ser movida;\n")
    sleep(2.5)
    print("Em seguida coloque o númera da linha com a letra da coluna do movimento desejado.\n")
    sleep(2.5)
    print("EX: 7e 6e, 7E5E, 7E 5E ou 7e5e\n")
    sleep(2.5)
    input("Presione ENTER para começar.")


def verificar_xeque():
    global xeque
    xeque = False
    if tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == 1 or tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == 2 or \
            tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == 3 or tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == 7:
        xeque = True
    if tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == 1 or tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == 2 or \
            tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == 3 or tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == 7:
        xeque = True


def verificar_xeque_mate():
    cont = 0
    if turno == VERDES:
        for i in range(TAMANHO_TABULEIRO):
            for j in range(TAMANHO_TABULEIRO):
                if tabuleiro_captura_verdes[i][j] == 1 and tabuleiro_captura_azuis[i][j] == 2:
                    return False
                elif tabuleiro_captura_verdes[i][j] == 4 and tabuleiro_captura_azuis[i][j] == 2:
                    return False
                elif tabuleiro_captura_verdes[i][j] == 7 and tabuleiro_captura_azuis[i][j] == 2:
                    return False

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and i == j):
                    if ((posis_reis[0][0]) + i >= 0 and (posis_reis[0][0]) + i < TAMANHO_TABULEIRO) and \
                            ((posis_reis[0][1]) + j >= 0 and (posis_reis[0][1]) + j < TAMANHO_TABULEIRO):
                        if tabuleiro_captura_azuis[(posis_reis[0][0])+i][(posis_reis[0][1])+j] == 0:
                            if tabuleiro_cores[(posis_reis[0][0])+i][(posis_reis[0][1])+j] != VERDES:
                                cont += 1

        if cont != 0:
            return False

        return True

    else:
        for i in range(TAMANHO_TABULEIRO):
            for j in range(TAMANHO_TABULEIRO):
                if tabuleiro_captura_azuis[i][j] == 1 and tabuleiro_captura_verdes[i][j] == 2:
                    return False
                elif tabuleiro_captura_azuis[i][j] == 4 and tabuleiro_captura_verdes[i][j] == 2:
                    return False
                elif tabuleiro_captura_azuis[i][j] == 7 and tabuleiro_captura_verdes[i][j] == 2:
                    return False

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and i == j):
                    if ((posis_reis[1][0]) + i >= 0 and (posis_reis[1][0]) + i < TAMANHO_TABULEIRO) and \
                            ((posis_reis[1][1]) + j >= 0 and (posis_reis[1][1]) + j < TAMANHO_TABULEIRO):
                        if tabuleiro_captura_verdes[(posis_reis[1][0]) + i][(posis_reis[1][1]) + j] == 0:
                            if tabuleiro_cores[(posis_reis[1][0]) + i][(posis_reis[1][1]) + j] != AZUIS:
                                cont += 1

        if cont != 0:
            return False

        return True


valido = False
posi_atual_p: str
movimento_p: str
turno = VERDES
xeque = False
peça_erro = "nenhum"
tabuleiro_captura_verdes = []
tabuleiro_captura_azuis = []

montando_tabuleiro()
criar_referencia_cor()
#imprimir_tutorial()

while True:
    atualizar_referencia_captura(AZUIS)
    atualizar_referencia_captura(VERDES)
    verificar_xeque()
    imprime_tabuleiro()

    print(MSG_TURNO.format(turno.upper()))

    """for i in range(TAMANHO_TABULEIRO):
        print(*tabuleiro_captura_verdes[i])

    print()
    for i in range(TAMANHO_TABULEIRO):
        print(*tabuleiro_captura_azuis[i])"""

    if xeque:
        if verificar_xeque_mate():
            print("XEQUE-MATE")
            if turno == VERDES:
                print("As azuis ganharam")
            else:
                print("As verdes ganharam")
            break
        else:
            print(MSG_XEQUE)


    coordenada_jogada = input()

    if criar_posis(coordenada_jogada):

        if validar_jogada():
            jogar()
            if valido:
                trocar_turno()
            elif peça_erro != "nenhum":
                print(MSG_MOVIMENTO_INVALIDO.format(peça_erro))
            else:
                if not xeque:
                    print(MSG_ESPAÇO_VAZIO)
        else:
            print(MSG_COMANDO_INVALIDO)
    else:
        print(MSG_COMANDO_INVALIDO)
