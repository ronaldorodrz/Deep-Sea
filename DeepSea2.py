import pygame
import time
import random

# INICIALIZADOR
# Inicializa todos os módulos do Pygame.
pygame.init()

# TELA
# Define a altura e a largura da tela.
largura, altura = 1130, 680
tela = pygame.display.set_mode((largura, altura))
# Define o título da janela.
pygame.display.set_caption("Deep Sea 2")
# Define o tamanho da matriz.
tamanho_matriz = 550 

# CORES
# Define as cores usadas no jogo.
preto = (0, 0, 0)
branco = (255, 250, 250)
cinza = (28, 28, 28)
# FONTE
# Define a fonte e o tamanho do texto.
fonte = pygame.font.Font('TEXTO/textofonte.ttf', 40)
fonte_menor = pygame.font.Font('TEXTO/textofonte.ttf', 30)
fonte_botao = pygame.font.Font('TEXTO/textofonte.ttf', 25)

# IMAGENS
# Carrega e redimensiona a imagem de fundo.
fundo = pygame.image.load('IMAGENS/imagemfundo.jpg')
novo_fundo = pygame.transform.scale(fundo, (largura, altura))
submarino = pygame.image.load('IMAGENS/sub.png')
novo_submarino = pygame.transform.scale(submarino, ((largura // 4) + 30, altura // 6))
# Obter tamanho da imagem redimensionada
largura_sub, altura_sub = novo_submarino.get_size()
# Calcular posição para centralizar no topo
x_central = (largura - largura_sub) // 2
y_topo = -1 
# Carrega e define o ícone da janela.
icon = pygame.image.load('IMAGENS/submarino.png')
pygame.display.set_icon(icon)

# BOTÕES
# Define a largura e altura dos botões.
botao_largura, botao_altura = 200, 50
# Calcula a posição central do botão.
botao_x = (largura - botao_largura) // 2
botao_y = (altura - botao_altura) // 2 + 100
# Define o raio de curvatura da borda do botão.
raio_borda = 25

# BOTÃO
# Função para desenhar o botão com texto e borda arredondada.
def botao(texto, cor, pos_x, pos_y, largura, altura, alpha):
    # Obtém a posição do mouse.
    mouse_pos = pygame.mouse.get_pos()
    # Verifica se o mouse está sobre o botão.
    mouse_sobre = pygame.Rect(pos_x, pos_y, largura, altura).collidepoint(mouse_pos)
    # Ajusta a transparência com base na posição do mouse.
    alpha = 250 if mouse_sobre else 100
    # Cria uma superfície com transparência para o botão.
    botao_surf = pygame.Surface((largura, altura), pygame.SRCALPHA)
    # Desenha o retângulo do botão com bordas arredondadas.
    pygame.draw.rect(botao_surf, (*preto, alpha), (0, 0, largura, altura), border_radius=raio_borda)
    # Exibe o botão na tela na posição especificada.
    tela.blit(botao_surf, (pos_x, pos_y))
    # Renderiza e centraliza o texto no botão.
    texto_renderizado = fonte_botao.render(texto, True, branco)
    texto_rect = texto_renderizado.get_rect(center=(pos_x + largura // 2, pos_y + altura // 2))
    # Exibe o texto no botão.
    tela.blit(texto_renderizado, texto_rect)
    # Retorna se o mouse está sobre o botão
    return mouse_sobre

# VERIFICAÇÃO DO CLIQUE NO BOTÃO
# Função para verificar se o botão foi clicado com base na posição do mouse.
def verificar_clique(pos_mouse, pos_botao, tamanho_botao):
    # Cria um retângulo representando o botão.
    botao_rect = pygame.Rect(pos_botao[0], pos_botao[1], tamanho_botao[0], tamanho_botao[1])
    # Verifica se o clique do mouse está dentro da área do botão.
    return botao_rect.collidepoint(pos_mouse)

# TELA INICIAL
# Exibe a tela inicial com opções de navegação e título do jogo.
def Tela_Inicial():
    jogando = True  # Controla o loop da tela inicial.
    cooldown = 0.5  # Define um intervalo para cliques consecutivos.
    # Loop principal da tela de inicial.
    while jogando:
        # Captura eventos do pygame, como clicar no botão de fechar.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Verifica se a janela foi fechada.
                pygame.quit()  # Fecha a aplicação.
                return  # Sai da função.
        # Renderiza o fundo da tela inicial.
        tela.blit(novo_fundo, (0, 0))
        # Centraliza e exibe o título do jogo na tela.
        texto_nova_tela = fonte.render("Deep Sea 2: Aventura Aguarda!", True, branco)
        tela.blit(texto_nova_tela, ((largura - texto_nova_tela.get_width()) // 2, (altura - texto_nova_tela.get_height()) // 2 - 50))
        # Cria botões para navegar para outras telas.
        botao("Configurações", branco, botao_x, botao_y, botao_largura, botao_altura, 128)
        botao("Tutorial", branco, botao_x, botao_y + 70, botao_largura, botao_altura, 128)
        # Detecta a posição do mouse e verifica cliques nos botões.
        pos_mouse = pygame.mouse.get_pos()  # Pega a posição atual do mouse.
        if pygame.mouse.get_pressed()[0]:  # Verifica se o botão esquerdo foi clicado.
            time.sleep(cooldown)  # Adiciona um intervalo para evitar múltiplos cliques.
            # Verifica se o clique foi no botão "Configurações".
            if verificar_clique(pos_mouse, (botao_x, botao_y), (botao_largura, botao_altura)):
                Tela_configuração()  # Abre a tela de configuração.
            # Verifica se o clique foi no botão "Tutorial".
            elif verificar_clique(pos_mouse, (botao_x, botao_y + 70), (botao_largura, botao_altura)):
                Tela_Explicação()  # Abre a tela de tutorial.
        # Atualiza a tela para exibir os elementos desenhados.
        pygame.display.update()

# TELA DE EXPLICAÇÃO
# Exibe um tutorial com instruções sobre o jogo.
def Tela_Explicação():
    jogando = True  # Controla o loop da tela de explicação.
    cooldown = 0.5  # Define um intervalo para cliques consecutivos.
    # Loop principal da tela de explicação.
    while jogando:
        # Captura eventos do pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Verifica se a janela foi fechada.
                pygame.quit()  # Fecha a aplicação.
                return  # Sai da função.
        # Renderiza o fundo da tela de explicação.
        tela.blit(novo_fundo, (0, 0))
        # Lista de instruções exibidas no tutorial.
        explicacoes = [
            '',
            '',
            '',
            '1- Comece sua aventura no submarino com os demais mergulhadores.',
            '2- Todos compartilham o mesmo tanque de oxigênio.',
            '3- Quanto mais profundo o tesouro, maior seu valor e peso.',
            '4- Cada movimento consome ao menos 1 unidade de oxigênio.',
            '5- O consumo de oxigênio aumenta conforme o peso do tesouro.',
            '6- O mapa do fundo do mar pode ter 9x9 ou 15x15 metros.',
            '7- No seu turno, você pode passar, mover, pegar ou depositar um tesouro.',
            '8- A distância percorrida é decidida aleatoriamente.',
            '9- O vencedor é aquele que retornar ao submarino com os tesouros mais valiosos.']
        # Centraliza e exibe o título do tutorial.
        texto_nova_tela = fonte.render("Tutorial de Mergulho:", True, branco)
        tela.blit(texto_nova_tela, ((largura - texto_nova_tela.get_width()) // 2, (altura - texto_nova_tela.get_height()) // 2 - 240))
        # Exibe as instruções linha por linha.
        for i, linha in enumerate(explicacoes):
            texto_explicacao = fonte_botao.render(linha, True, branco)
            tela.blit(texto_explicacao, (50, 50 + i * 40))  # Define a posição inicial e o espaçamento entre linhas.
        # Cria o botão para voltar à tela inicial.
        botao("Voltar", branco, botao_x, altura - 100, botao_largura, botao_altura, 128)
        # Detecta cliques no botão "Voltar".
        pos_mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Verifica se o botão esquerdo foi clicado.
            time.sleep(cooldown)  # Adiciona um intervalo para evitar múltiplos cliques.
            if verificar_clique(pos_mouse, (botao_x, altura - 100), (botao_largura, botao_altura)):
                jogando = False  # Encerra o loop e retorna à tela inicial.
        # Atualiza a tela para exibir os elementos desenhados.
        pygame.display.update()

# TELA DE CONFIGURAÇÃO
# Permite ao jogador personalizar os parâmetros do jogo, como dificuldade, tamanho do mapa e quantidade de tanques.
def Tela_configuração():
    jogando = True  # Controla o loop da tela de configuração.
    cooldown = 0.5  # Define um intervalo para cliques consecutivos.
    # Inicializa as variáveis que armazenam as opções escolhidas.
    global dificuldade, metros, tanques
    dificuldade = None
    metros = None
    tanques = None
    # Loop principal da tela de configuração.
    while jogando:
        # Captura eventos do pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Verifica se a janela foi fechada.
                pygame.quit()  # Fecha a aplicação.
                return  # Sai da função.
        # Renderiza o fundo da tela de configuração.
        tela.blit(novo_fundo, (0, 0))
        # Exibe o título da tela no topo.
        texto_nova_tela = fonte.render("Personalizar Jogo", True, branco)
        tela.blit(texto_nova_tela, ((largura - texto_nova_tela.get_width()) // 2, (altura - texto_nova_tela.get_height()) // 2 - 240))
        # Exibe os textos descritivos para cada configuração.
        texto_dificuldade = fonte.render("Dificuldade: ", True, branco)
        tela.blit(texto_dificuldade, ((largura - texto_dificuldade.get_width()) // 2 - 420, (altura - texto_dificuldade.get_height()) // 2 - 120))
        texto_metros = fonte.render("Metros: ", True, branco)
        tela.blit(texto_metros, ((largura - texto_metros.get_width()) // 2 - 420, (altura - texto_metros.get_height()) // 2 - 15))
        texto_tanque = fonte.render("Tanques: ", True, branco)
        tela.blit(texto_tanque, ((largura - texto_tanque.get_width()) // 2 - 420, (altura - texto_tanque.get_height()) // 2 + 85))
        # Cria botões para cada opção de configuração e navegação.
        botao("Jogar", branco, botao_x, botao_y + 120, botao_largura, botao_altura, 128)  # Começa o jogo.
        botao("Voltar", branco, botao_x, botao_y + 180, botao_largura, botao_altura, 128)  # Volta para a tela inicial.
        # Botões para selecionar a dificuldade do jogo.
        botao("Fácil", branco, botao_x - 180, botao_y - 220, botao_largura, botao_altura, 128)
        botao("Médio", branco, botao_x + 60, botao_y - 220, botao_largura, botao_altura, 128)
        botao("Difícil", branco, botao_x + 300, botao_y - 220, botao_largura, botao_altura, 128)
        # Botões para selecionar o tamanho do mapa (metros).
        botao("9x9", branco, botao_x - 180, botao_y - 120, botao_largura, botao_altura, 128)
        botao("15x15", branco, botao_x + 60, botao_y - 120, botao_largura, botao_altura, 128)
        # Botões para selecionar a quantidade de tanques disponíveis.
        botao("160", branco, botao_x - 180, botao_y - 15, botao_largura, botao_altura, 128)
        botao("500", branco, botao_x + 60, botao_y - 15, botao_largura, botao_altura, 128)
        # Captura a posição do mouse e verifica cliques nos botões.
        pos_mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Verifica se o botão esquerdo foi clicado.
            time.sleep(cooldown)  # Adiciona um intervalo para evitar múltiplos cliques.
            # Verifica se o botão "Jogar" foi clicado.
            if verificar_clique(pos_mouse, (botao_x, botao_y + 120), (botao_largura, botao_altura)):
                # Apenas inicia o jogo se todas as opções forem selecionadas.
                if dificuldade and metros and tanques:
                    Tela_jogo(metros, dificuldade, tanques, tamanho_matriz)
            # Define a dificuldade com base no botão clicado.
            elif verificar_clique(pos_mouse, (botao_x - 180, botao_y - 220), (botao_largura, botao_altura)):
                dificuldade = 'Fácil'
            elif verificar_clique(pos_mouse, (botao_x + 60, botao_y - 220), (botao_largura, botao_altura)):
                dificuldade = 'Médio'
            elif verificar_clique(pos_mouse, (botao_x + 300, botao_y - 220), (botao_largura, botao_altura)):
                dificuldade = 'Difícil'
            # Define o tamanho do mapa (metros).
            elif verificar_clique(pos_mouse, (botao_x - 180, botao_y - 120), (botao_largura, botao_altura)):
                metros = int(9)
            elif verificar_clique(pos_mouse, (botao_x + 60, botao_y - 120), (botao_largura, botao_altura)):
                metros = int(15)
            # Define a quantidade de tanques disponíveis.
            elif verificar_clique(pos_mouse, (botao_x - 180, botao_y - 15), (botao_largura, botao_altura)):
                tanques = int(160)
            elif verificar_clique(pos_mouse, (botao_x + 60, botao_y - 15), (botao_largura, botao_altura)):
                tanques = int(500)
            # Verifica se o botão "Voltar" foi clicado e retorna à tela inicial.
            elif verificar_clique(pos_mouse, (botao_x, botao_y + 180), (botao_largura, botao_altura)):
                jogando = False  # Encerra o loop da tela de configuração.
        # Atualiza a tela para exibir os elementos desenhados.
        pygame.display.update()

# TELA DE FIM DE JOGO
def Tela_Fim(pontuacoes, nomes_jogadores):
    # Inicializa a variável que controla o loop da tela de fim de jogo.
    jogando = True  
    # Ordena os jogadores com base na pontuação em ordem decrescente.
    ranking = sorted(zip(pontuacoes, nomes_jogadores), reverse=True, key=lambda x: x[0])
    # Loop principal da tela de fim de jogo.
    while jogando:
        # Captura os eventos gerados pelo Pygame (ex.: teclado, mouse, fechamento de janela).
        for event in pygame.event.get():
            # Verifica se o evento é do tipo "fechar a janela".
            if event.type == pygame.QUIT:  
                pygame.quit()  # Encerra o Pygame.
                return  # Sai da função imediatamente.
        # Renderiza o fundo da tela de fim de jogo.
        tela.blit(novo_fundo, (0, 0))
        # Texto principal
        texto_fim1 = fonte.render("Você sobreviveu às profundezas!", True, branco)
        # Texto de agradecimento
        texto_fim2 = fonte_menor.render("Obrigado por explorar Deep Sea 2!", True, branco)
        # Instrução para o jogador
        texto_fim3 = fonte_menor.render("Pressione o 'X' no canto da tela para encerrar sua aventura.", True, branco)
        # Exibe os textos principais
        tela.blit(texto_fim1, ((largura - texto_fim1.get_width()) // 2, altura // 3))
        tela.blit(texto_fim2, ((largura - texto_fim2.get_width()) // 2, altura // 3 + 50))
        tela.blit(texto_fim3, ((largura - texto_fim3.get_width()) // 2, altura // 3 + 100))
        # Exibe o ranking dos jogadores
        y_offset = altura // 2 + 25  # Ajuste vertical para a posição do ranking
        for i, (pontuacao, jogador) in enumerate(ranking):
            texto_ranking = fonte_menor.render(f"{i + 1}. {jogador}: {pontuacao} pontos", True, branco)
            tela.blit(texto_ranking, ((largura - texto_ranking.get_width()) // 2, y_offset))
            y_offset += 40  # Aumenta o espaço para o próximo jogador no ranking
        # Captura eventos do pygame, como clicar no botão de fechar.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Verifica se a janela foi fechada.
                pygame.quit()  # Fecha a aplicação.
                return  # Sai da função.
        # Atualiza a tela com as mudanças feitas (fundo e textos renderizados).
        pygame.display.update()
    # Encerra o Pygame após sair do loop principal.
    pygame.quit()

# TELA DO JOGO
# Função principal que gerencia o estado do jogo, os movimentos dos jogadores, tesouros, bombas, e a pontuação.
def Tela_jogo(metros, dificuldade, tanques, tamanho_matriz):
    # Inicializa variáveis de controle do jogo.
    jogando = True
    cooldown = 0.5  # Tempo de espera entre ações.
    vez = 0  # Indica a vez do jogador (0 a 3).
    movimento = random.randint(0, 3)  # Movimento aleatório inicial.
    pontuacoes = [0, 0, 0, 0]  # Pontuação de cada jogador.
    nomes_jogadores = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"]  # Nomes dos jogadores.
    # Cores atribuídas aos jogadores.
    cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]  # Vermelho, Verde, Azul, Branco.
    # Posições iniciais dos jogadores.
    pos_jogadores = [
        [0, metros // 2],  
        [0, metros // 2],
        [0, metros // 2],
        [0, metros // 2],]
    # Inicializa a matriz de tesouros com valores variados para cada área.
    tesouros = [[1 for _ in range(metros)] for _ in range(metros)]
    for linha in range(metros):
        for coluna in range(metros):
            if linha < 5:
                tesouros[linha][coluna] = 1  # Tesouro de valor 1.
            elif linha < 10:
                tesouros[linha][coluna] = 2  # Tesouro de valor 2.
            else:
                tesouros[linha][coluna] = 4  # Tesouro de valor 4.
    # Inicializa a matriz de bombas como vazia.
    bombas = [[False for _ in range(metros)] for _ in range(metros)]
    # Função para calcular o número de bombas com base na dificuldade.
    def calcular_bombas(dificuldade):
        total_celulas = metros * metros
        if dificuldade == "Fácil":
            porcentagem = 0.01  # 1% de bombas.
        elif dificuldade == "Médio":
            porcentagem = 0.05  # 5% de bombas.
        elif dificuldade == "Difícil":
            porcentagem = 0.15  # 15% de bombas.
        return int(total_celulas * porcentagem)
    # Calcula o número total de bombas.
    num_bombas = calcular_bombas(dificuldade)
    # Coloca as bombas em posições aleatórias.
    for _ in range(num_bombas):
        while True:
            linha = random.randint(3, metros - 1)
            coluna = random.randint(0, metros - 1)
            if not bombas[linha][coluna]:  # Se não houver bomba na posição, coloca a bomba.
                bombas[linha][coluna] = True
                break
    # Função para pegar um tesouro quando um jogador se move para uma célula.
    def pegar_tesouro(pos_jogador):
        linha, coluna = pos_jogador
        if 0 <= linha < len(tesouros) and 0 <= coluna < len(tesouros[0]):
            tesouro = tesouros[linha][coluna]
            if tesouro > 0:
                tesouros[linha][coluna] = 0  # Remove o tesouro da célula.
                pontuacoes[vez] += tesouro  # Atualiza a pontuação do jogador.
                print(f"{nomes_jogadores[vez]}: {pontuacoes[vez]} pontos")  # Exibe a pontuação.
    # Função para verificar se um jogador atingiu uma bomba.
    def checar_bomba(pos_jogador):
        linha, coluna = pos_jogador
        if 0 <= linha < len(bombas) and 0 <= coluna < len(bombas[0]):
            if bombas[linha][coluna]:  # Se houver bomba na célula.
                bombas[linha][coluna] = False  # Desativa a bomba.
    # Função para calcular o consumo de oxigênio com base no peso acumulado dos tesouros e a quantidade de células mergulhadas.
    def calcular_consumo(pos_jogador, peso_tesouro):
        linha, coluna = pos_jogador
        # A quantidade de oxigênio consumida depende das células mergulhadas e o peso acumulado dos tesouros
        return (linha + coluna) * peso_tesouro + 1
    # Função para calcular o peso dos tesouros ao longo da profundidade
    def calcular_peso_tesouro(linha):
        if linha < 5:
            return 1  # Peso do tesouro é 1kg
        elif linha < 10:
            return 2  # Peso do tesouro é 2kg
        else:
            return 4  # Peso do tesouro é 4kg
    # Loop principal do jogo enquanto a variável 'jogando' for verdadeira.
    while jogando:
        acessiveis = calcular_acessiveis(pos_jogadores[vez], movimento, pos_jogadores, metros)  # Calcula as células acessíveis.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Se o evento for o fechamento da janela.
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:  # Se o evento for um clique do mouse.
                if evento.button == 1:  # Se for o botão esquerdo do mouse.
                    destino = obter_celula_clicada(evento.pos, metros, tamanho_matriz)  # Obtém a célula clicada.
                    if destino == pos_jogadores[vez]:  # Se o jogador clicou na célula onde ele está.
                        movimento = random.randint(0, 3)  # Gera um novo movimento aleatório.
                        vez = (vez + 1) % 4  # Passa a vez para o próximo jogador.
                        tanques -= 1  # Diminui o número de tanques restantes.
                    elif tanques <= 0:  # Se não houver tanques, exibe a tela de fim.
                        Tela_Fim(pontuacoes, nomes_jogadores)
                    elif destino in acessiveis:  # Se o destino for uma célula acessível.
                        pos_jogadores[vez] = destino  # Atualiza a posição do jogador.
                        tanques -= 1  # Diminui o número de tanques restantes.
                        # Calcula o peso do tesouro na célula
                        peso_tesouro = calcular_peso_tesouro(destino[0])
                        # Calcula o consumo de oxigênio
                        consumo = calcular_consumo(destino, peso_tesouro)
                        tanques -= consumo  # Diminui o número de tanques com base no consumo
                        movimento = random.randint(0, 3)  # Gera um novo movimento aleatório.
                        pegar_tesouro(destino)  # Chama a função para pegar tesouro.
                        checar_bomba(destino)  # Chama a função para checar se atingiu bomba.
                        vez = (vez + 1) % 4  # Passa a vez para o próximo jogador.
        # Exibição da tela com as informações atualizadas.
        tela.blit(novo_fundo, (0, 0))  # Atualiza o fundo da tela.
        texto_tanques = fonte_menor.render(f"Tanques restantes: {tanques}", True, branco)
        tela.blit(texto_tanques, ((largura - texto_tanques.get_width()) // 2 - 380, (altura - texto_tanques.get_height()) // 2 - 300))
        texto_jogador = fonte_menor.render(f"{nomes_jogadores[vez]}", True, cores[vez])
        tela.blit(texto_jogador, ((largura - texto_jogador.get_width()) // 2 - 480, (altura - texto_jogador.get_height()) // 2 - 250))
        Tela_matriz(metros, tamanho_matriz, pos_jogadores, acessiveis, tesouros, bombas)  # Exibe a matriz do jogo.
        # Botão para voltar ao menu inicial.
        botao("Voltar", branco, botao_x, botao_y + 210, botao_largura, botao_altura, 128)
        pos_mouse = pygame.mouse.get_pos()  # Obtém a posição do mouse.
        if pygame.mouse.get_pressed()[0]:  # Se o botão esquerdo do mouse for pressionado.
            time.sleep(cooldown)  # Espera um curto período.
            if verificar_clique(pos_mouse, (botao_x, botao_y + 210), (botao_largura, botao_altura)):
                Tela_Inicial()  # Chama a função para voltar à tela inicial.
        pygame.display.update()  # Atualiza a tela.

# TELA DA MATRIZ
# Função responsável por desenhar a matriz do jogo com os jogadores, acessibilidade, tesouros e bombas.
def Tela_matriz(metros, tamanho, pos_jogadores, acessiveis, tesouros, bombas):
    # Calcula o tamanho de cada célula com base no tamanho da tela e na quantidade de metros.
    tamanho_celula = tamanho // metros
    # Calcula as dimensões totais da matriz (largura e altura).
    largura_matriz = metros * tamanho_celula
    altura_matriz = metros * tamanho_celula
    # Calcula a posição inicial para centralizar a matriz na tela.
    x_inicial = (largura - largura_matriz) // 2
    y_inicial = (altura - altura_matriz) // 2
    # Loop para desenhar as células da matriz.
    for linha in range(metros):
        for coluna in range(metros):
            # Calcula as coordenadas x e y para desenhar cada célula.
            x = x_inicial + coluna * tamanho_celula
            y = y_inicial + linha * tamanho_celula 
            # Se a célula é acessível, pinta a célula de verde.
            if [linha, coluna] in acessiveis:
                pygame.draw.rect(tela, (0, 255, 0), (x, y, tamanho_celula, tamanho_celula))
            # Verifica se há tesouros na célula e desenha um círculo com cores diferentes, dependendo do tipo de tesouro.
            if tesouros[linha][coluna] == 1:
                pygame.draw.circle(tela, (255, 255, 0), (x + tamanho_celula // 2, y + tamanho_celula // 2), tamanho_celula // 4)
            elif tesouros[linha][coluna] == 2:
                pygame.draw.circle(tela, (255, 140, 0), (x + tamanho_celula // 2, y + tamanho_celula // 2), tamanho_celula // 4)
            elif tesouros[linha][coluna] == 4:
                pygame.draw.circle(tela, (184, 134, 11), (x + tamanho_celula // 2, y + tamanho_celula // 2), tamanho_celula // 4)
            # Se houver uma bomba na célula, desenha um círculo cinza para representar a bomba.
            if bombas[linha][coluna]:
                pygame.draw.circle(tela, ((28,28,28)), (x + tamanho_celula // 2, y + tamanho_celula // 2), tamanho_celula // 4)
            # Desenha um contorno branco ao redor de cada célula.
            pygame.draw.rect(tela, branco, (x, y, tamanho_celula, tamanho_celula), 1)
    # Carrega e redimensiona as imagens dos jogadores para o tamanho das células.
    imagens_jogadores = [
        pygame.transform.scale(pygame.image.load("IMAGENS/mergulhador.png"), (tamanho_celula, tamanho_celula)),
        pygame.transform.scale(pygame.image.load("IMAGENS/mergulhador1.png"), (tamanho_celula, tamanho_celula)),
        pygame.transform.scale(pygame.image.load("IMAGENS/mergulhador2.png"), (tamanho_celula, tamanho_celula)),
        pygame.transform.scale(pygame.image.load("IMAGENS/mergulhador3.png"), (tamanho_celula, tamanho_celula)),]
    # Loop para desenhar os jogadores nas posições especificadas.
    for i, pos in enumerate(pos_jogadores):
        linha, coluna = pos
        # Calcula as coordenadas x e y para desenhar o jogador na célula.
        x = x_inicial + coluna * tamanho_celula
        y = y_inicial + linha * tamanho_celula
        # Desenha a imagem do jogador na tela.
        tela.blit(imagens_jogadores[i], (x, y))

# OBTER CÉLULA CLICADA
# Função para determinar qual célula foi clicada com base na posição do mouse.
def obter_celula_clicada(mouse_pos, metros, tamanho_matriz):
    # Obtém a posição do mouse.
    x_mouse, y_mouse = mouse_pos
    # Calcula o tamanho de cada célula com base no tamanho total da matriz e metros.
    tamanho_celula = tamanho_matriz // metros
    # Calcula as coordenadas iniciais da matriz, para centralizá-la.
    x_inicial = (largura - tamanho_matriz) // 2
    y_inicial = (altura - tamanho_matriz) // 2
    # Verifica se o mouse está dentro dos limites da matriz.
    if x_inicial <= x_mouse < x_inicial + tamanho_matriz and y_inicial <= y_mouse < y_inicial + tamanho_matriz:
        # Calcula a coluna e linha da célula clicada com base na posição do mouse.
        coluna = (x_mouse - x_inicial) // tamanho_celula
        linha = (y_mouse - y_inicial) // tamanho_celula
        # Retorna a posição da célula clicada como uma lista [linha, coluna].
        return [linha, coluna]
    # Se o clique não estiver dentro da matriz, retorna None.
    return None

# CALCULAR CÉLULAS ACESSÍVEIS
# Função para calcular as células acessíveis a partir de uma posição, dentro de uma distância máxima.
def calcular_acessiveis(pos, max_dist, posicoes, metros):
    # Obtém a linha e a coluna da posição inicial.
    linha, coluna = pos
    acessiveis = []  # Lista para armazenar as células acessíveis.
    # Loop para verificar as células ao redor, dentro da distância máxima.
    for d in range(1, max_dist + 1):
        # Verifica se a célula acima da posição está acessível.
        if linha - d >= 0 and [linha - d, coluna] not in posicoes:
            acessiveis.append([linha - d, coluna])
        # Verifica se a célula abaixo da posição está acessível.
        if linha + d < metros and [linha + d, coluna] not in posicoes:
            acessiveis.append([linha + d, coluna])
        # Verifica se a célula à esquerda da posição está acessível.
        if coluna - d >= 0 and [linha, coluna - d] not in posicoes:
            acessiveis.append([linha, coluna - d])
        # Verifica se a célula à direita da posição está acessível.
        if coluna + d < metros and [linha, coluna + d] not in posicoes:
            acessiveis.append([linha, coluna + d])
    # Retorna a lista de células acessíveis.
    return acessiveis

# VERIFICAR CLIQUE
# Função para verificar se o mouse clicou dentro dos limites de um botão.
def verificar_clique(pos_mouse, pos_botao, dimensao_botao):
    # Obtém a posição do mouse.
    x, y = pos_mouse
    # Obtém a posição do botão e suas dimensões.
    botao_x, botao_y = pos_botao
    botao_largura, botao_altura = dimensao_botao
    # Verifica se o mouse está dentro dos limites do botão.
    return botao_x <= x <= botao_x + botao_largura and botao_y <= y <= botao_y + botao_altura

# JOGO PRINCIPAL
Tela_Inicial()  # Renderiza a tela inicial.