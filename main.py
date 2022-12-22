from tabuleiro import *
from time import sleep

PEÇA_XEQUE = "X"


def atualizar_referencia_captura(cor):
    global tabuleiro
    global tabuleiro_captura_verdes
    global tabuleiro_captura_azuis

    def verificar_horizontal_vertical():
        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i + l][j] != AREA_XEQUE) or (cor == AZUIS and tabuleiro_captura_azuis[i + l][j] != AREA_XEQUE):
                    if tabuleiro_cores[i + l][j] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j] = CAPTURA
                        else:
                            tabuleiro_captura_azuis[i + l][j] = CAPTURA
                    elif tabuleiro_cores[i + l][j] == cor:
                        if cor == VERDES:
                            if tabuleiro[i + l][j] != REI_V:
                                if tabuleiro_captura_verdes[i + l][j] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i + l][j] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i + l][j] = CAPTURA
                                break
                        else:
                            if tabuleiro[i + l][j] != REI_A:
                                if tabuleiro_captura_azuis[i + l][j] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i + l][j] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i + l][j] = CAPTURA
                                break
                    elif (cor == VERDES and tabuleiro[i + l][j] == REI_A) or (
                            cor == AZUIS and tabuleiro[i + l][j] == REI_V):
                        for k in range(1, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i + k][j] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i + k][j] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j] = CAPTURA
                            break
                        else:
                            tabuleiro_captura_azuis[i + l][j] = CAPTURA
                            break

        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i - l][j] != AREA_XEQUE) or (cor == AZUIS and tabuleiro_captura_azuis[i - l][j] != AREA_XEQUE):
                    if tabuleiro_cores[i - l][j] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j] = CAPTURA
                        else:
                            tabuleiro_captura_azuis[i - l][j] = CAPTURA
                    elif tabuleiro_cores[i - l][j] == cor:
                        if cor == VERDES:
                            if tabuleiro[i - l][j] != REI_V:
                                if tabuleiro_captura_verdes[i - l][j] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i - l][j] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i - l][j] = CAPTURA
                                break
                        else:
                            if tabuleiro[i - l][j] != REI_A:
                                if tabuleiro_captura_azuis[i - l][j] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i - l][j] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i - l][j] = CAPTURA
                                break
                    elif (cor == VERDES and tabuleiro[i - l][j] == REI_A) or (
                            cor == AZUIS and tabuleiro[i - l][j] == REI_V):
                        for k in range(1, l + 1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i - k][j] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i - k][j] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j] = CAPTURA
                            break
                        else:
                            tabuleiro_captura_azuis[i - l][j] = CAPTURA
                            break

        for l in range(1, TAMANHO_TABULEIRO):
            if j + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i][j + l] != AREA_XEQUE) or (cor == AZUIS and tabuleiro_captura_azuis[i][j + l] != AREA_XEQUE):
                    if tabuleiro_cores[i][j + l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j + l] = CAPTURA
                        else:
                            tabuleiro_captura_azuis[i][j + l] = CAPTURA
                    elif tabuleiro_cores[i][j + l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i][j + l] != REI_V:
                                if tabuleiro_captura_verdes[i][j + l] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i][j + l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i][j + l] = CAPTURA
                                break
                        else:
                            if tabuleiro[i][j + l] != REI_A:
                                if tabuleiro_captura_azuis[i][j + l] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i][j + l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i][j + l] = CAPTURA
                                break
                    elif (cor == VERDES and tabuleiro[i][j + l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i][j + l] == REI_V):
                        for k in range(1, l + 1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i][j + k] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i][j + k] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j + l] = CAPTURA
                            break
                        else:
                            tabuleiro_captura_azuis[i][j + l] = CAPTURA
                            break

        for l in range(1, TAMANHO_TABULEIRO):
            if j - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i][j - l] != AREA_XEQUE) or (cor == AZUIS and tabuleiro_captura_azuis[i][j - l] != AREA_XEQUE):
                    if tabuleiro_cores[i][j - l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j - l] = CAPTURA
                        else:
                            tabuleiro_captura_azuis[i][j - l] = CAPTURA
                    elif tabuleiro_cores[i][j - l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i][j - l] != REI_V:
                                if tabuleiro_captura_verdes[i][j - l] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i][j - l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i][j - l] = CAPTURA
                                break
                        else:
                            if tabuleiro[i][j - l] != REI_A:
                                if tabuleiro_captura_azuis[i][j - l] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i][j - l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i][j - l] = CAPTURA
                                break
                    elif (cor == VERDES and tabuleiro[i][j - l] == REI_A) or (
                                    cor == AZUIS and tabuleiro[i][j - l] == REI_V):
                        for k in range(1, l + 1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i][j - k] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i][j - k] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
                        break
                    else:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i][j - l] = CAPTURA
                            break
                        else:
                            tabuleiro_captura_azuis[i][j - l] = CAPTURA
                            break

    def verificar_diagonal():
        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO and j + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i + l][j + l] != AREA_XEQUE) or (cor == AZUIS and tabuleiro_captura_azuis[i + l][j + l] != AREA_XEQUE):
                    if tabuleiro_cores[i + l][j + l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j + l] = CAPTURA
                        else:

                            tabuleiro_captura_azuis[i + l][j + l] = CAPTURA
                    elif tabuleiro_cores[i + l][j + l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i + l][j + l] != REI_V:
                                if tabuleiro_captura_verdes[i + l][j + l] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i + l][j + l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i + l][j + l] = CAPTURA
                            break
                        else:
                            if tabuleiro[i + l][j + l] != REI_A:
                                if tabuleiro_captura_azuis[i + l][j + l] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i + l][j + l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i + l][j + l] = CAPTURA
                            break

                    elif (cor == VERDES and tabuleiro[i + l][j + l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i + l][j + l] == REI_V):
                        for k in range(1, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i+k][j + k] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i+k][j + k] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
                        break
                    else:
                        break

        for l in range(1, TAMANHO_TABULEIRO):
            if i + l < TAMANHO_TABULEIRO and j - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i + l][j - l] != AREA_XEQUE) or (
                        cor == AZUIS and tabuleiro_captura_azuis[i + l][j - l] != AREA_XEQUE):
                    if tabuleiro_cores[i + l][j - l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i + l][j - l] = CAPTURA
                        else:
                            tabuleiro_captura_azuis[i + l][j - l] = CAPTURA
                    elif tabuleiro_cores[i + l][j - l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i + l][j - l] != REI_V:
                                if tabuleiro_captura_verdes[i + l][j - l] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i + l][j - l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i + l][j - l] = CAPTURA
                            break
                        else:
                            if tabuleiro[i + l][j - l] != REI_A:
                                if tabuleiro_captura_azuis[i + l][j - l] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i + l][j - l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i + l][j - l] = CAPTURA
                            break
                    elif (cor == VERDES and tabuleiro[i + l][j - l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i + l][j - l] == REI_V):
                        for k in range(1, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i+k][j - k] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i+k][j - k] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
                        break
                    else:
                        break


        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0 and j + l < TAMANHO_TABULEIRO:
                if (cor == VERDES and tabuleiro_captura_verdes[i - l][j + l] != AREA_XEQUE) or (cor == AZUIS and tabuleiro_captura_azuis[i - l][j + l] != AREA_XEQUE):
                    if tabuleiro_cores[i - l][j + l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j + l] = CAPTURA
                        else:
                            tabuleiro_captura_azuis[i - l][j + l] = CAPTURA
                    elif tabuleiro_cores[i - l][j + l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i - l][j + l] != REI_V:
                                if tabuleiro_captura_verdes[i - l][j + l] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i - l][j + l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i - l][j + l] = CAPTURA
                            break
                        else:
                            if tabuleiro[i - l][j + l] != REI_A:
                                if tabuleiro_captura_azuis[i - l][j + l] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i - l][j + l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i - l][j + l] = CAPTURA
                            break
                    elif (cor == VERDES and tabuleiro[i - l][j + l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i - l][j + l] == REI_V):
                        for k in range(1, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i - k][j + k] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i - k][j + k] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
                        break
                    else:
                        break

        for l in range(1, TAMANHO_TABULEIRO):
            if i - l >= 0 and j - l >= 0:
                if (cor == VERDES and tabuleiro_captura_verdes[i - l][j - l] != AREA_XEQUE) or (cor == AZUIS and tabuleiro_captura_azuis[i - l][j - l] != AREA_XEQUE):
                    if tabuleiro_cores[i - l][j - l] == ESPACO:
                        if cor == VERDES:
                            tabuleiro_captura_verdes[i - l][j - l] = CAPTURA
                        else:
                            tabuleiro_captura_azuis[i - l][j - l] = CAPTURA
                    elif tabuleiro_cores[i - l][j - l] == cor:
                        if cor == VERDES:
                            if tabuleiro[i - l][j - l] != REI_V:
                                if tabuleiro_captura_verdes[i - l][j - l] == PEÇA_XEQUE:
                                    tabuleiro_captura_verdes[i - l][j - l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_verdes[i - l][j - l] = CAPTURA
                            break
                        else:
                            if tabuleiro[i - l][j - l] != REI_A:
                                if tabuleiro_captura_azuis[i - l][j - l] == PEÇA_XEQUE:
                                    tabuleiro_captura_azuis[i - l][j - l] = AREA_XEQUE
                                else:
                                    tabuleiro_captura_azuis[i - l][j - l] = CAPTURA
                            break
                    elif (cor == VERDES and tabuleiro[i - l][j - l] == REI_A) or (
                            cor == AZUIS and tabuleiro[i - l][j - l] == REI_V):
                        for k in range(1, l+1):
                            if cor == VERDES:
                                tabuleiro_captura_verdes[i - k][j - k] = AREA_XEQUE
                                tabuleiro_captura_verdes[i][j] = PEÇA_XEQUE
                            else:
                                tabuleiro_captura_azuis[i - k][j - k] = AREA_XEQUE
                                tabuleiro_captura_azuis[i][j] = PEÇA_XEQUE
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
                            if tabuleiro_captura_verdes[i - 1][j + 1] != AREA_XEQUE:
                                if tabuleiro_cores[i-1][j+1] == cor or tabuleiro_cores[i-1][j+1] == ESPACO:
                                    if tabuleiro_captura_verdes[i - 1][j + 1] == MOVIMENTO_PEAO:
                                        tabuleiro_captura_verdes[i - 1][j + 1] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_verdes[i - 1][j + 1] == 0:
                                        tabuleiro_captura_verdes[i - 1][j + 1] = CAPTURA_PEAO
                                elif tabuleiro_cores[i-1][j+1] == AZUIS:
                                    tabuleiro_captura_verdes[i - 1][j + 1] = CAPTURA
                        if i == 6:
                            if tabuleiro_cores[i - 1][j] == ESPACO:
                                if tabuleiro_captura_verdes[i - 1][j] != AREA_XEQUE:
                                    if tabuleiro_cores[i - 1][j] == CAPTURA_PEAO:
                                        tabuleiro_captura_verdes[i - 1][j] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_verdes[i - 1][j] == 0:
                                        tabuleiro_captura_verdes[i - 1][j] = MOVIMENTO_PEAO

                            if tabuleiro_cores[i - 2][j] == ESPACO:
                                if tabuleiro_captura_verdes[i - 2][j] != AREA_XEQUE:
                                    if tabuleiro_cores[i - 2][j] == CAPTURA_PEAO:
                                        tabuleiro_captura_verdes[i - 2][j] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_verdes[i - 2][j] == 0:
                                        tabuleiro_captura_verdes[i - 2][j] = MOVIMENTO_PEAO
                        else:
                            if tabuleiro_captura_verdes[i - 1][j] != AREA_XEQUE:
                                if tabuleiro_cores[i - 1][j] == ESPACO:
                                    if tabuleiro_captura_verdes[i - 1][j] == CAPTURA_PEAO:
                                        tabuleiro_captura_verdes[i - 1][j] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_verdes[i - 1][j] == 0:
                                        tabuleiro_captura_verdes[i - 1][j] = MOVIMENTO_PEAO

                        if i - 1 >= 0 and j - 1 >= 0:
                            if tabuleiro_captura_verdes[i - 1][j - 1] != AREA_XEQUE:
                                if tabuleiro_cores[i - 1][j - 1] == cor or tabuleiro_cores[i - 1][j - 1] == ESPACO:
                                    if tabuleiro_captura_verdes[i - 1][j - 1] == MOVIMENTO_PEAO:
                                        tabuleiro_captura_verdes[i - 1][j - 1] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_verdes[i - 1][j - 1] == 0:
                                        tabuleiro_captura_verdes[i - 1][j - 1] = CAPTURA_PEAO
                                elif tabuleiro_cores[i - 1][j - 1] == AZUIS:
                                    tabuleiro_captura_verdes[i - 1][j - 1] = CAPTURA

                    # Peões Azuis

                    else:
                        if i + 1 < TAMANHO_TABULEIRO and j + 1 < TAMANHO_TABULEIRO:
                            if tabuleiro_captura_azuis[i + 1][j + 1] != AREA_XEQUE:
                                if tabuleiro_cores[i + 1][j + 1] == cor or tabuleiro_cores[i + 1][j + 1] == ESPACO:
                                    if tabuleiro_captura_azuis[i + 1][j + 1] == MOVIMENTO_PEAO:
                                        tabuleiro_captura_azuis[i + 1][j + 1] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_azuis[i + 1][j + 1] == MOV_CAPTURA_PEAO:
                                        pass
                                    else:
                                        tabuleiro_captura_azuis[i + 1][j + 1] = CAPTURA_PEAO
                                elif tabuleiro_cores[i + 1][j + 1] == VERDES:
                                    tabuleiro_captura_azuis[i + 1][j + 1] = CAPTURA

                        if i == 1:
                            if tabuleiro_cores[i + 1][j] == ESPACO:
                                if tabuleiro_captura_azuis[i + 1][j] != AREA_XEQUE:
                                    if tabuleiro_captura_azuis[i + 1][j] == CAPTURA_PEAO:
                                        tabuleiro_captura_azuis[i + 1][j] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_azuis[i + 1][j] == MOV_CAPTURA_PEAO:
                                        pass
                                    else:
                                        tabuleiro_captura_azuis[i + 1][j] = MOVIMENTO_PEAO
                            if tabuleiro_captura_azuis[i + 2][j] != AREA_XEQUE:
                                if tabuleiro_cores[i + 2][j] == ESPACO:
                                    if tabuleiro_captura_azuis[i + 2][j] == CAPTURA_PEAO:
                                        tabuleiro_captura_azuis[i + 2][j] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_azuis[i + 2][j] == MOV_CAPTURA_PEAO:
                                        pass
                                    else:
                                        tabuleiro_captura_azuis[i + 2][j] = MOVIMENTO_PEAO
                        else:
                            if tabuleiro_captura_azuis[i + 1][j] != AREA_XEQUE:
                                if tabuleiro_cores[i + 1][j] == ESPACO:
                                    if tabuleiro_captura_azuis[i + 1][j] == CAPTURA_PEAO:
                                        tabuleiro_captura_azuis[i + 1][j] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_azuis[i + 1][j] == MOV_CAPTURA_PEAO:
                                        pass
                                    else:
                                        tabuleiro_captura_azuis[i + 1][j] = MOVIMENTO_PEAO

                        if i + 1 < TAMANHO_TABULEIRO and j - 1 >= 0:
                            if tabuleiro_captura_azuis[i + 1][j - 1] != AREA_XEQUE:
                                if tabuleiro_cores[i + 1][j - 1] == cor or tabuleiro_cores[i + 1][j - 1] == ESPACO:
                                    if tabuleiro_captura_azuis[i + 1][j - 1] == MOVIMENTO_PEAO:
                                        tabuleiro_captura_azuis[i + 1][j - 1] = MOV_CAPTURA_PEAO
                                    elif tabuleiro_captura_azuis[i + 1][j - 1] == MOV_CAPTURA_PEAO:
                                        pass
                                    else:
                                        tabuleiro_captura_azuis[i + 1][j - 1] = CAPTURA_PEAO
                                elif tabuleiro_cores[i + 1][j - 1] == VERDES:
                                    tabuleiro_captura_azuis[i + 1][j - 1] = CAPTURA

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
                                                    tabuleiro_captura_verdes[i+l][j+c] = CAPTURA
                                                else:
                                                    tabuleiro_captura_azuis[i + l][j + c] = CAPTURA

                                            if tabuleiro_cores[i+l][j+c] == cor:
                                                if cor == VERDES and tabuleiro[i+l][j+c] != REI_V:
                                                    tabuleiro_captura_verdes[i+l][j+c] = CAPTURA
                                                else:
                                                    if cor == AZUIS and tabuleiro[i+l][j+c] != REI_A:
                                                        tabuleiro_captura_azuis[i + l][j + c] = CAPTURA

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

    if (tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] != REI_V and turno == VERDES) or \
            (tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] != REI_A and turno == AZUIS):
        if (xeque and turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0])-1][COLUNA_REFERENCIA.index(movimento_p[1])] == AREA_XEQUE) or \
            (xeque and turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == AREA_XEQUE) or \
                not xeque or (xeque and turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0])-1][COLUNA_REFERENCIA.index(movimento_p[1])] == PEÇA_XEQUE) or \
                    (xeque and turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == PEÇA_XEQUE):

            if tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_V and turno == VERDES or \
                    tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == PEAO_A and turno == AZUIS:

                if verificar_peao(posi_atual_p, movimento_p, turno):
                    mover_peça(P_PEAO, posi_atual_p, movimento_p, turno)
                    valido = True

                else:
                    peça_erro = P_PEAO

            elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_V and turno == VERDES or \
                    tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == CAVALO_A and turno == AZUIS:

                if verificar_cavalo(posi_atual_p, movimento_p, turno):
                    mover_peça(P_CAVALO, posi_atual_p, movimento_p, turno)
                    valido = True

                else:
                    peça_erro = P_CAVALO

            elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_V and turno == VERDES or \
                    tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == TORRE_A and turno == AZUIS:

                if verificar_torre(posi_atual_p, movimento_p, turno):
                    mover_peça(P_TORRE, posi_atual_p, movimento_p, turno)
                    valido = True

                else:
                    peça_erro = P_TORRE

            elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_V and turno == VERDES or \
                    tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == BISPO_A and turno == AZUIS:

                if verificar_bispo(posi_atual_p, movimento_p, turno):
                    mover_peça(P_BISPO, posi_atual_p, movimento_p, turno)
                    valido = True

                else:
                    peça_erro = P_BISPO

            elif tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_V and turno == VERDES or \
                    tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == RAINHA_A and turno == AZUIS:

                if verificar_bispo(posi_atual_p, movimento_p, turno) or verificar_torre(posi_atual_p, movimento_p, turno):
                    mover_peça(P_RAINHA, posi_atual_p, movimento_p, turno)
                    valido = True

                else:
                    peça_erro = P_RAINHA

        else:
            print("Você não pode mover a peça nessa posição, pois seu rei está em XEQUE.")

    if tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_V and turno == VERDES or \
            tabuleiro[int(posi_atual_p[0]) - 1][COLUNA_REFERENCIA.index(posi_atual_p[1])] == REI_A and turno == AZUIS:

        if (turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0])-1][COLUNA_REFERENCIA.index(movimento_p[1])] == 0) or \
                (turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == MOVIMENTO_PEAO) or \
                (turno == VERDES and tabuleiro_captura_azuis[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == PEÇA_XEQUE):
            if verificar_rei(posi_atual_p, movimento_p, turno):
                mover_peça(P_REI, posi_atual_p, movimento_p, turno)
                valido = True
            else:
                peça_erro = P_REI

        elif (turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == 0) or \
              (turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == MOVIMENTO_PEAO) or \
                (turno == AZUIS and tabuleiro_captura_verdes[int(movimento_p[0]) - 1][COLUNA_REFERENCIA.index(movimento_p[1])] == PEÇA_XEQUE):
            if verificar_rei(posi_atual_p, movimento_p, turno):
                mover_peça(P_REI, posi_atual_p, movimento_p, turno)
                valido = True
            else:
                peça_erro = P_REI

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
    print(MSG_TUTORIAL1)
    sleep(2.5)
    print(MSG_TUTORIAL2)
    sleep(2.5)
    print(MSG_TUTORIAL3)
    sleep(2.5)
    print(MSG_TUTORIAL4)
    sleep(2.5)
    input(MSG_TUTORIAL5)


def verificar_xeque():
    global xeque
    xeque = False
    if tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == CAPTURA or tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == AREA_XEQUE or \
            tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == CAPTURA_PEAO or tabuleiro_captura_azuis[posis_reis[0][0]][posis_reis[0][1]] == MOV_CAPTURA_PEAO:
        xeque = True
    if tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == CAPTURA or tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == AREA_XEQUE or \
            tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == CAPTURA_PEAO or tabuleiro_captura_verdes[posis_reis[1][0]][posis_reis[1][1]] == MOV_CAPTURA_PEAO:
        xeque = True


def verificar_xeque_mate():
    cont = 0
    if turno == VERDES:
        for i in range(TAMANHO_TABULEIRO):
            for j in range(TAMANHO_TABULEIRO):
                if tabuleiro_captura_verdes[i][j] == CAPTURA and (tabuleiro_captura_azuis[i][j] == AREA_XEQUE or tabuleiro_captura_azuis[i][j] == PEÇA_XEQUE):
                    return False
                elif tabuleiro_captura_verdes[i][j] == MOVIMENTO_PEAO and (tabuleiro_captura_azuis[i][j] == AREA_XEQUE or tabuleiro_captura_azuis[i][j] == PEÇA_XEQUE):
                    return False
                elif tabuleiro_captura_verdes[i][j] == MOV_CAPTURA_PEAO and tabuleiro_captura_azuis[i][j] == AREA_XEQUE or tabuleiro_captura_azuis[i][j] == PEÇA_XEQUE:
                    return False

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and i == j):
                    if ((posis_reis[0][0]) + i >= 0 and (posis_reis[0][0]) + i < TAMANHO_TABULEIRO) and \
                            ((posis_reis[0][1]) + j >= 0 and (posis_reis[0][1]) + j < TAMANHO_TABULEIRO):
                        if tabuleiro_captura_azuis[(posis_reis[0][0])+i][(posis_reis[0][1])+j] == 0 or \
                                tabuleiro_captura_azuis[(posis_reis[0][0])+i][(posis_reis[0][1])+j] == PEÇA_XEQUE:
                            if tabuleiro_cores[(posis_reis[0][0])+i][(posis_reis[0][1])+j] != VERDES:
                                cont += 1

        if cont != 0:
            return False

        return True

    else:
        for i in range(TAMANHO_TABULEIRO):
            for j in range(TAMANHO_TABULEIRO):
                if tabuleiro_captura_azuis[i][j] == CAPTURA and (tabuleiro_captura_verdes[i][j] == AREA_XEQUE or tabuleiro_captura_verdes[i][j] == PEÇA_XEQUE):
                    return False
                elif tabuleiro_captura_azuis[i][j] == MOVIMENTO_PEAO and (tabuleiro_captura_verdes[i][j] == AREA_XEQUE or tabuleiro_captura_verdes[i][j] == PEÇA_XEQUE):
                    return False
                elif tabuleiro_captura_azuis[i][j] == MOV_CAPTURA_PEAO and (tabuleiro_captura_verdes[i][j] == AREA_XEQUE or tabuleiro_captura_verdes[i][j] == PEÇA_XEQUE):
                    return False

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and i == j):
                    if ((posis_reis[1][0]) + i >= 0 and (posis_reis[1][0]) + i < TAMANHO_TABULEIRO) and \
                            ((posis_reis[1][1]) + j >= 0 and (posis_reis[1][1]) + j < TAMANHO_TABULEIRO):
                        if tabuleiro_captura_verdes[(posis_reis[1][0]) + i][(posis_reis[1][1]) + j] == 0 or \
                                tabuleiro_captura_verdes[(posis_reis[1][0]) + i][(posis_reis[1][1]) + j] == PEÇA_XEQUE:
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
