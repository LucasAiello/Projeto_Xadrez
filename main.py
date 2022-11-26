PRETAS = "pretas"
BRANCAS = "brancas"
TAMANHO_TABULEIRO = 8
ESPACO = u'\u2001'
SEPARADOR_VAZIO = ''
SEPARADOR_VERTICAL1 = '| '
SEPARADOR_VERTICAL = ' | '
SEPARADOR_VERTICAL0 = ' |'
SEPARADOR_HORIZ = '_'*38


def montando_tabuleiro():
    global tabuleiro_cores
    global tabuleiro

    for i in range(TAMANHO_TABULEIRO):
        tabuleiro.append([])
        for j in range(TAMANHO_TABULEIRO):
            if i <= 1 or i >= 6:
                if i == 1:
                    tabuleiro[i].append(pecas_pretas[-1])
                elif i == 0:
                    for h in range(TAMANHO_TABULEIRO):
                        tabuleiro[i].append(pecas_pretas[h])
                elif i == 6:
                    tabuleiro[i].append("\u2659")
                elif i == 7:
                    for h in range(TAMANHO_TABULEIRO):
                        tabuleiro[i].append(pecas_brancas[h])
            else:
                tabuleiro[i].append(ESPACO)

    # Matriz de cores para referencia

    for i in range(TAMANHO_TABULEIRO):
        linha = []
        for j in range(TAMANHO_TABULEIRO):
            if i == 0 or i == 1:
                linha.append("p")
            elif i == 6 or i == 7:
                linha.append("b")
            else:
                linha.append(SEPARADOR_VAZIO)
        tabuleiro_cores.append(linha)


def imprime_tabuleiro():
    for i in range(TAMANHO_TABULEIRO):
        if i ==0 :
            for h in range(TAMANHO_TABULEIRO+1):
                print(ESPACO,end=coluna[h])
            print()
        print(' ',SEPARADOR_HORIZ)
        for j in range(TAMANHO_TABULEIRO):

            if j == TAMANHO_TABULEIRO-1:
                print(SEPARADOR_VERTICAL+tabuleiro[i][j], end= SEPARADOR_VERTICAL0)
            else:
                if j==0:
                    print(i+1, SEPARADOR_VERTICAL1, end=tabuleiro[i][j] )
                else:
                    print(SEPARADOR_VERTICAL, end=tabuleiro[i][j] )
        print()
        if i == TAMANHO_TABULEIRO-1:
            print(' ',SEPARADOR_HORIZ)


def trocar_turno():
    global turno
    if turno == BRANCAS:
        turno = PRETAS
    else:
        turno = BRANCAS


turno = BRANCAS
pecas_brancas = ['\u2656', '\u2657', '\u2658', '\u2654', '\u2655', '\u2658', '\u2657', '\u2656']
pecas_pretas = ['\033[30m\u265c\033[m',  '\033[30m\u265d\033[m', '\033[30m\u265e\033[m',
             '\033[30m\u265a\033[m',  '\033[30m\u265b\033[m', '\033[30m\u265e\033[m',
             '\033[30m\u265d\033[m', '\033[30m\u265c\033[m', '\033[30m\u2659\033[m']

tabuleiro = []
tabuleiro_cores = []
coluna = [' ', 'a ', ' b', '  c',  '  d', '  e', '  f ', ' g', '  h']


montando_tabuleiro()
imprime_tabuleiro()
trocar_turno()
