import pygame
pygame.init()

screen_width = 1280 
screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo do Semáforo")

# import fundo menu inicial
menu_inicial = pygame.image.load('menu_jogo.png')
menu_redim = pygame.transform.scale(menu_inicial, (1280, 720))
# import botao sair
botao_sair = pygame.image.load('sair.png')
sair_redim = pygame.transform.scale(botao_sair, (236,101))
# import botao comecar
botao_comecar = pygame.image.load('comecar.png')
comecar_redim = pygame.transform.scale(botao_comecar, (281,106))
# import botao carregar
botao_carregar = pygame.image.load('regras.png')
carregar_redim = pygame.transform.scale(botao_carregar, (281,106))
# import botao regras
botao_regras = pygame.image.load('regras.png')
regras_redim = pygame.transform.scale(botao_regras, (281,106))
# import fundo comecar
menu_comecar = pygame.image.load('menu_comecar.png')
menu_comecar_redim = pygame.transform.scale(menu_comecar, (1280, 720))

def textos():
    return 'Descrição do Jogo:\n  Autor: Alan Parr\nMaterial: 8 peças verdes, 8 amarelas e 8 vermelhas partilhadas pelos jogadores.\n  Objetivo: Ser o primeiro a conseguir uma linha de três peças da mesma cor na horizontal, vertical ou diagonal.\n\nRegras do jogo:\nO jogo realiza-se no seguinte tabuleiro, inicialmente vazio. \n  Em cada jogada, cada jogador realiza uma das seguintes ações. \nColoca uma peça verde num quadrado vazio; \n  *Substitui uma peça verde por uma peça amarela '

def abrir_janela():
    main_menu = False  # Fecha o menu
    screen.fill((0, 0, 255))  # Preenche a tela com azul
    janela = pygame.display.set_mode((1280, 720))  # Cria uma nova janela
    janela.fill((255, 255, 255))  # Preenche a janela com branco
    fonte = pygame.font.Font('freesansbold.ttf', 20)
    texto = textos()
    linhas = texto.splitlines()  # Divide o texto em várias linhas
    y = 50  # Posição vertical inicial

    for linha in linhas:
        texto_renderizado = fonte.render(linha, True, (0, 0, 0))  # Renderiza a linha de texto
        janela.blit(texto_renderizado, (50, y))  # Exibe a linha de texto na nova janela
        y += 30  # Incrementa a posição vertical para a próxima linha

    run_janela = True
    while run_janela:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_janela = False  # Fecha a janela ao clicar no botão de fechar

        pygame.display.update()

    # Ao sair do loop, significa que a janela foi fechada
    # Agora você pode voltar para o menu principal
    main_menu = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # detectar quando o usuário clica nos botões
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if sair_redim.get_rect(topleft=(1052,625)).collidepoint(mouse_pos):
                pygame.quit()
                quit()

            elif comecar_redim.get_rect(topleft=(500, 250)).collidepoint(mouse_pos):
                # fechar o menu inicial
                pygame.display.quit()
                #pygame.display.set_mode((0, 0)) caso queiramos so minimizar o menu inicial e nao fechar mm, mas ns se está a funcionar bem
                                
                # abrir nova janela
                tela_comecar = pygame.display.set_mode((screen_width, screen_height))
                pygame.display.set_caption("Jogo do Semáforo")
                while running:    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                    
                    tela_comecar.blit(menu_comecar_redim, (0,0))
                    pygame.display.update()

            elif carregar_redim.get_rect(topleft=(500, 375)).collidepoint(mouse_pos):
                print("Botão carregar foi clicado!")

            elif regras_redim.get_rect(topleft=(500, 500)).collidepoint(mouse_pos):
                abrir_janela()

    # apresentar os botoes no ecra
    screen.blit(menu_redim, (0,0))
    screen.blit(sair_redim, (1052,625))
    screen.blit(comecar_redim, (500, 250))
    screen.blit(carregar_redim, (500, 375))
    screen.blit(regras_redim, (500,500))

    pygame.display.update()


