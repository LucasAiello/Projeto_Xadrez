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
                linha.append(SEPARADOR_VAZIO)
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


def validar_movimento(p_atual, deslocamento):
    global turno
    global tabuleiro
    global tabuleiro_cores
    linha_atual = str(p_atual[0])
    linha_deslocamento = str(deslocamento[0])

    try:
        if linha_atual.isdigit() and (int(linha_atual[0]) >= 1 and int(linha_atual[0]) <= 8):
            for i in range(len(coluna_referencia)):
                if p_atual[1] == coluna_referencia[i]:
                    if tabuleiro_cores[int(p_atual[0])-1][coluna_referencia.index(p_atual[1])-1] == turno:
                        if linha_deslocamento.isdigit() and (int(linha_deslocamento[0]) >= 1 and int(linha_deslocamento[0]) <= 8):
                            for i in range(len(coluna_referencia)):
                                if deslocamento[1] == coluna_referencia[i]:
                                    return True
    except:
        return False


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
    posi_atual, posi_deslocamento = input().split()
    if validar_movimento(posi_atual, posi_deslocamento):
        pass
    else:
        print("Comando incorreto.")
    trocar_turno()
