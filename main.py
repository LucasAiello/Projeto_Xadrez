from logica import *
from time import sleep


def validar_jogada():
    global posi_atual_p
    global movimento_p

    if posi_atual_p[0].isnumeric() and movimento_p[0].isnumeric():
        if int(movimento_p[0])-1 >= 0 and int(movimento_p[0])-1 <= 7:
            for i in range(len(COLUNA_REFERENCIA)):
                if movimento_p[1] == COLUNA_REFERENCIA[i]:
                    return True


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


def imprimir_erro():
    if erro != NENHUM and erro != ERRO_REI_EM_XEQUE and erro != ERRO_REI_FICARA_XEQUE:
        print(MSG_MOVIMENTO_INVALIDO.format(erro))
    elif erro == NENHUM:
        print(NENHUM)
    elif erro == ERRO_REI_EM_XEQUE:
        print(ERRO_REI_EM_XEQUE)
    elif erro == ERRO_REI_FICARA_XEQUE:
        print(ERRO_REI_FICARA_XEQUE)
    else:
        if not xeque:
            print(MSG_ESPAÇO_VAZIO)


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


montando_tabuleiro()
criar_referencia_cor()
imprimir_tutorial()

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
            print(MSG_XEQUE_MATE)
            if turno == VERDES:
                print(MSG_VITORIA_AZUIS)
            else:
                print(MSG_VITORIA_VERDES)
            break
        else:
            print(MSG_XEQUE)

    coordenada_jogada = input()

    if criar_posis(coordenada_jogada):
        if validar_jogada():
            jogar()
            if valido:
                trocar_turno()
            else:
                imprimir_erro()
        else:
            print(MSG_COMANDO_INVALIDO)
    else:
        print(MSG_COMANDO_INVALIDO)
