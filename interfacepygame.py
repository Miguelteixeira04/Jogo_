import pygame
pygame.init()

screen_width = 1280 
screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo do Semáforo")

# Definição das cores (opcional)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (68, 68, 68)

# Variáveis para armazenar os nomes dos jogadores
nome_jogador1 = ""
nome_jogador2 = ""
jogador_atual = 1
digitando = True

# import fundo menu inicial
menu_inicial = pygame.image.load('menu_jogo.png')
menu_redim = pygame.transform.scale(menu_inicial, (1280, 720))
# import fundo comecar
menu_comecar = pygame.image.load('menu_comecar.png')
menu_comecar_redim = pygame.transform.scale(menu_comecar, (1280, 720))
# import fundo regras
menu_regras= pygame.image.load('menu_regras.png')
menu_regras_redim = pygame.transform.scale(menu_regras, (1280, 720))
# import fundo nomes
menu_nomes = pygame.image.load("jogadores.png")
menu_nomes = pygame.transform.scale(menu_nomes, (1280, 720))

# import botao sair
botao_sair = pygame.image.load('sair.png')
sair_redim = pygame.transform.scale(botao_sair, (236,101))
# import botao comecar
botao_comecar = pygame.image.load('comecar.png')
comecar_redim = pygame.transform.scale(botao_comecar, (281,106))
# import botao carregar
botao_carregar = pygame.image.load('carregar.png')
carregar_redim = pygame.transform.scale(botao_carregar, (281,106))
# import botao regras
botao_regras = pygame.image.load('regras.png')
regras_redim = pygame.transform.scale(botao_regras, (281,106))
# import botao 1v1
botao_1v1 = pygame.image.load('1v1.png')
botao_1v1_redim = pygame.transform.scale(botao_1v1, (352,184))
# import botao 1vbot
botao_1vbot = pygame.image.load('1vbot.png')
botao_1vbot_redim = pygame.transform.scale(botao_1vbot, (352,194))
# import botao voltar
botao_voltar = pygame.image.load('voltar.png')
botao_voltar_redim = pygame.transform.scale(botao_voltar, (73,54))


def abrir_janela_regras():
    main_menu = False

    janela_regras = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jogo do Semáforo")

    run_janela_regras = True
    while run_janela_regras:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_janela_regras = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if botao_voltar_redim.get_rect(topleft=(1200,5)).collidepoint(mouse_pos):
                    run_janela_regras = False

        janela_regras.blit(menu_regras_redim, (0,0))
        janela_regras.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

    main_menu = True

def abrir_janela_comecar():
    main_menu = False

    janela_comecar = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jogo do Semáforo")

    run_janela_comecar = True
    while run_janela_comecar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_janela_comecar = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if botao_1v1_redim.get_rect(topleft=(150,300)).collidepoint(mouse_pos):
                    print("esta a dar")

                elif botao_1vbot_redim.get_rect(topleft=(800,295)).collidepoint(mouse_pos):
                    print("tbm funciona")
                
                elif botao_voltar_redim.get_rect(topleft=(1200,5)).collidepoint(mouse_pos):
                    run_janela_comecar = False


        janela_comecar.blit(menu_comecar_redim, (0,0))
        janela_comecar.blit(botao_1v1_redim, (150, 300))
        janela_comecar.blit(botao_1vbot_redim, (800, 295))
        janela_comecar.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

    main_menu = True


def inserir_nomes():

    janela_nomes = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jogo do Semáforo")

    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if jogador_atual == 1:
                        jogador_atual = 2
                    else:
                        digitando = False
                elif evento.key == pygame.K_BACKSPACE:
                    if jogador_atual == 1:
                        nome_jogador1 = nome_jogador1[:-1]
                    else:
                        nome_jogador2 = nome_jogador2[:-1]
                else:
                    if jogador_atual == 1:
                        nome_jogador1 += evento.unicode
                    else:
                        nome_jogador2 += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if posicao_texto_jogador1.collidepoint(evento.pos):
                        jogador_atual = 1
                        nome_jogador1 = ""
                    elif posicao_texto_jogador2.collidepoint(evento.pos):
                        jogador_atual = 2
                        nome_jogador2 = ""

    # Desenhar a imagem de fundo
    janela_nomes.blit(menu_nomes, (0, 0))

    # Exibindo o nome digitado na janela
    fonte = pygame.font.Font(None, 46)
    texto_jogador1 = fonte.render(nome_jogador1, True, BRANCO)
    texto_jogador2 = fonte.render(nome_jogador2, True, BRANCO)

    posicao_texto_jogador1 = texto_jogador1.get_rect(midleft=(menu_nomes // 2 - 525, menu_nomes // 2 + 48))
    posicao_texto_jogador2 = texto_jogador2.get_rect(midleft=(menu_nomes // 2 + 155, menu_nomes // 2 + 48))

    # Desenhar retângulos interativos para reescrever o nome
    pygame.draw.rect(janela_nomes,CINZA, posicao_texto_jogador1)
    pygame.draw.rect(janela_nomes, CINZA, posicao_texto_jogador2)

    janela_nomes.blit(texto_jogador1, posicao_texto_jogador1)
    janela_nomes.blit(texto_jogador2, posicao_texto_jogador2)

    pygame.display.flip()



########### MAIN ####################

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
                abrir_janela_comecar()

            elif carregar_redim.get_rect(topleft=(500, 375)).collidepoint(mouse_pos):
                print("Botão carregar foi clicado!")

            elif regras_redim.get_rect(topleft=(500, 500)).collidepoint(mouse_pos):
                abrir_janela_regras()

    # apresentar os botoes no ecra
    screen.blit(menu_redim, (0,0))
    screen.blit(sair_redim, (1052,625))
    screen.blit(comecar_redim, (500, 250))
    screen.blit(carregar_redim, (500, 375))
    screen.blit(regras_redim, (500,500))

    pygame.display.update()


