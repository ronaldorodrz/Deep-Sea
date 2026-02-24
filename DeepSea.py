import random
import time
quantidade = 0
metros = 0
tanques = 0
turno = 0

print('''\033[96m
██████╗ ███████╗███████╗██████╗     ███████╗███████╗ █████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔════╝
██║  ██║█████╗  █████╗  ██████╔╝    ███████╗█████╗  ███████║███████╗
██║  ██║██╔══╝  ██╔══╝  ██╔═══╝     ╚════██║██╔══╝  ██╔══██║╚════██║
██████╔╝███████╗███████╗██║         ███████║███████╗██║  ██║███████║
╚═════╝ ╚══════╝╚══════╝╚═╝         ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝
⛵ Bem-vindo ao Deep Sea! Prepare-se para uma aventura submarina! 🌊''')

print('''\033[96m
------  Explicação do Jogo  ------
\033[0m
1- Tudo se inicia com os mergulhadores no submarino.
2- A cada turno, é gasto pelo menos 1 tanque de oxigênio.
3- Um tesouro é encontrado a cada metro de profundidade.
4- Quanto mais profundo, maior o valor e peso dos tesouros.
5- Um mergulhador pode carregar mais de um tesouro consigo.
6- Ao final da partida, será definido um vencedor.
7- O mergulhador precisa estar no submarino até o final da 
   última rodada e ter o maior valor em tesouros a bordo.

\033[93m💡 Dica: Deposite os tesouros no submarino para economizar oxigênio! 💡\033[0m''')

# CONFIGURAÇÃO DO JOGO.
print('\033[96m\n------  Fase de configuração 🔧  ------\033[0m\n')

# QUANTIDADE DE JOGADORES.
while quantidade not in [4, 5, 6]:
    quantidade = int(input('Escolha quantos jogadores irão jogar, entre 4, 5 ou 6: '))
    if quantidade in [4, 5, 6]:
        print(f'\033[92mFoi escolhido {quantidade} jogadores.\033[0m')
    else:
        print('\033[91mDados inválidos.\033[0m')

# TAMANHO DO MAPA EM METROS.
while metros not in [15, 30, 45]:
    metros = int(input('Vocês querem que a profundidade do mapa seja de 15, 30 ou 45 metros: '))
    if metros in [15, 30, 45]:
        print(f"\033[92mFoi escolhido {metros} metros.\033[0m")
    else:
        print('\033[91mDados inválidos.\033[0m')

# QUANTIDADE DE TANQUES.
while not 45 <= tanques <= 120:
    tanques = int(input('Escolha quantos tanques serão consumidos, entre 45 a 120: '))
    if 45 <= tanques <= 120:
        print(f"\033[92mFoi escolhido {tanques} tanques.\033[0m")
    else:
        print('\033[91mDados inválidos.\033[0m')

# LISTA DE INICIALIZAÇÃO DOS JOGADORES.
posição_do_jogador = [0] * quantidade
tesouro_do_jogador = [0] * quantidade
tesouro = [[] for _ in range(metros + 1)]

# STATUS DOS JOGADORES.
def status_do_jogador(posição_do_jogador, tesouro_do_jogador):
    print('\n\033[96m------  Status dos Jogadores  ------\033[0m\n')
    for i in range(quantidade):
        print(f"Jogador {i+1} - Posição: {posição_do_jogador[i]} metros, tesouro: {tesouro_do_jogador[i]}")

# MAPA DO JOGO.
def print_mapa(posição_do_jogador):
    print('\033[96m\n------  Mapa do jogo 🗺️  ------\n\033[0m')
    mapa = ["[        ]"] * (metros + 1)
    for i in range(quantidade):
        jogador = posição_do_jogador[i]
        if 'J' in mapa[jogador]:
            mapa[jogador] = mapa[jogador].replace(']', f'J{i+1}   ]')
        else:
            mapa[jogador] = f"[   J{i+1}   ]"
    for i in range(len(mapa)):
        print(f"{mapa[i]}  - {i} metros")

# PESO DOS TESOUROS.
def peso_dos_tesouros(profundidade, metros):
    terço = metros // 3  
    if profundidade < terço:
        return 1
    elif profundidade < 2 * terço:
        return 2
    else:
        return 4

# VENCEDOR DO JOGO.
def vencedor(tesouro_do_jogador):
    maior_tesouro = max(tesouro_do_jogador)
    return maior_tesouro

# OXIGENIO RESTANTE.
def oxigenio(tanques):
    if tanques > 0:
        print(f"\033[91mTanques restantes: {tanques}\n\033[0m")
    elif tanques == 0:
        return 
    elif tanques < 0:
        return 

# PRESSIONE ENTER.
input('\n\033[91mPRESSIONE ENTER PARA COMEÇAR O JOGO.\033[0m')

# TURNO DOS JOGADORES. 
while tanques > 0:
    escolha = 0
    print_mapa(posição_do_jogador)
    status_do_jogador(posição_do_jogador, tesouro_do_jogador)
    jogador_atual = turno % quantidade
    print(f"\n\033[96m------  Turno do Jogador {jogador_atual + 1}  ------\033[0m")
# ESCOLHA A SUA JOGADA.
    while escolha not in [1, 2, 3, 4, 5]:
        print('\n[1] Passar a vez\n[2] Descer\n[3] Subir\n[4] Pegar tesouro\n[5] Não pegar tesouro.\n')
        escolha = int(input("Qual a sua escolha: "))
        if escolha not in [1, 2, 3, 4, 5]:
            print('\033[91mDados inválidos.\033[0m')

# MOVIMENTO DOS JOGADORES + TESOURO.
    if escolha in [1, 2, 3, 4, 5]:
        if escolha == 1:
            print('\033[92mVocê passou a vez.\n\033[0m')
        elif escolha == 2:
            movimento = random.randint(0, 3)
            posição_nova = posição_do_jogador[jogador_atual] + movimento
            if posição_nova > metros:
                posição_nova = metros
            posição_do_jogador[jogador_atual] = posição_nova
            print(f"\n\033[92mVocê desceu {movimento} metro.\033[0m")
        elif escolha == 3:
            movimento = random.randint(0, 3)
            posição_nova = posição_do_jogador[jogador_atual] - movimento
            if posição_nova < 0:
                posição_nova = 0
            posição_do_jogador[jogador_atual] = posição_nova
            print(f"\n\033[92mVocê subiu {movimento} metro.\033[0m")
        elif escolha == 4:
            profundidade = posição_do_jogador[jogador_atual]
            if profundidade not in tesouro[profundidade]:
                peso_do_tesouro = peso_dos_tesouros(profundidade, metros)
                tesouro_do_jogador[jogador_atual] += peso_do_tesouro
                tesouro[profundidade].append(profundidade)
                print(f'\033[92mVocê pegou um tesouro de {peso_do_tesouro} kg.\033[0m')
            else:
                print('\033[91mAlguém já pegou este tesouro.\033[0m')
        elif escolha == 5:
            print('\033[92mVocê não quis pegar o tesouro.\033[0m')

# CADA PARTIDA GASTA O OXIGENIO.
    consumo_de_oxigenio = tesouro_do_jogador[jogador_atual] + 1
    tanques -= consumo_de_oxigenio
    oxigenio(tanques)
    turno += 1

# FIM DO JOGO.
print('\033[96m\n------  Fim de Jogo ⛵  ------\033[0m\n')

# VENCEDOR DO JOGO.
print(f'O jogo teve um total de {turno} turnos.')
vencedor_do_jogo = tesouro_do_jogador.index(vencedor(tesouro_do_jogador)) + 1
print(f"\nO vencedor da partida é: Jogador {vencedor_do_jogo} com {tesouro_do_jogador[vencedor_do_jogo - 1]} kg de tesouros.\n")

# PRESSIONE ENTER.
input('\033[91mPRESSIONE ENTER PARA TERMINAR O JOGO.\033[0m')