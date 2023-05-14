import pygame
pygame.init()

screen_width = 1280 
screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo do Semáforo")

# Definição das cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (68, 68, 68)

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
menu_nomes = pygame.image.load("menu_nomes.png")
menu_nomes_redim = pygame.transform.scale(menu_nomes, (1280, 720))
# import fundo nome com bot
menu_nomebot = pygame.image.load("menu_nomebot.png")
menu_nomebot_redim = pygame.transform.scale(menu_nomebot, (1280, 720))
# import fundo escolha do bot
menu_escolhabot = pygame.image.load("menu_escolhabot.png")
menu_escolhabot_redim = pygame.transform.scale(menu_escolhabot, (1280, 720))


# import botao sair
botao_sair = pygame.image.load('sair.png')
sair_redim = pygame.transform.scale(botao_sair, (236,101))
# import botao comecar
botao_comecar = pygame.image.load('comecar.png')
comecar_redim = pygame.transform.scale(botao_comecar, (281,106))
# import botao carregar
botao_carregar = pygame.image.load('carregar.png')
carregar_redim = pygame.transform.scale(botao_carregar, (281,110))
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
# import botao facil
botao_facil = pygame.image.load('facil.png')
botao_facil_redim = pygame.transform.scale(botao_facil, (319,106))
# import botao medio
botao_medio = pygame.image.load('medio.png')
botao_medio_redim = pygame.transform.scale(botao_medio, (319,106))
# import botao dificil
botao_dificil = pygame.image.load('dificil.png')
botao_dificil_redim = pygame.transform.scale(botao_dificil, (319,106))

# mostrar as regras do jogo
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

# mostrar qd se clica no botao comecar (1v1 e 1vbot)
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
                    abrir_janela_nomes_1v1()

                elif botao_1vbot_redim.get_rect(topleft=(800,295)).collidepoint(mouse_pos):
                    abrir_janela_nomes_1vbot()
                
                elif botao_voltar_redim.get_rect(topleft=(1200,5)).collidepoint(mouse_pos):
                    run_janela_comecar = False
    

        janela_comecar.blit(menu_comecar_redim, (0,0))
        janela_comecar.blit(botao_1v1_redim, (150, 300))
        janela_comecar.blit(botao_1vbot_redim, (800, 295))
        janela_comecar.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

    main_menu = True

# inserir o nome dos jogadores 1v1
def abrir_janela_nomes_1v1():

    main_menu = False
    janela_nomes = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jogo do Semáforo")

    digitando = True
    jogador_atual = 1
    nome_jogador1 = ""
    nome_jogador2 = ""

    while digitando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                digitando = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if jogador_atual == 1:
                        jogador_atual = 2
                    else:
                        pass # para evitar que depois da inserção dos nomes o programa volte para a janela anterior, ao clicar na tecla ENTER!!
                
                elif event.key == pygame.K_BACKSPACE:
                    if jogador_atual == 1:
                        nome_jogador1 = nome_jogador1[:-1]
                    else:
                        nome_jogador2 = nome_jogador2[:-1]
                
                else:
                    if jogador_atual == 1:
                        nome_jogador1 += event.unicode
                    else:
                        nome_jogador2 += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:  
                mouse_pos = pygame.mouse.get_pos()       

                if event.button == 1:
                    if posicao_texto_jogador1.collidepoint(event.pos):
                        jogador_atual = 1
                        nome_jogador1 = ""
                    elif posicao_texto_jogador2.collidepoint(event.pos):
                        jogador_atual = 2
                        nome_jogador2 = ""
                    elif botao_voltar_redim.get_rect(topleft=(1200,5)).collidepoint(mouse_pos):
                        digitando = False

        pygame.display.update()
   
        janela_nomes.blit(menu_nomes_redim, (0, 0))
        janela_nomes.blit(botao_voltar_redim, (1200, 5))

        # Exibindo o nome digitado na janela
        fonte = pygame.font.Font(None, 46)
        texto_jogador1 = fonte.render(nome_jogador1, True, BRANCO)
        texto_jogador2 = fonte.render(nome_jogador2, True, BRANCO)

        posicao_texto_jogador1 = texto_jogador1.get_rect(midleft=(screen_width // 2 - 525, screen_height // 2 + 48))
        posicao_texto_jogador2 = texto_jogador2.get_rect(midleft=(screen_width // 2 + 155, screen_height // 2 + 48))

        # Desenhar retângulos interativos para reescrever o nome
        pygame.draw.rect(janela_nomes,CINZA, posicao_texto_jogador1)
        pygame.draw.rect(janela_nomes, CINZA, posicao_texto_jogador2)

        janela_nomes.blit(texto_jogador1, posicao_texto_jogador1)
        janela_nomes.blit(texto_jogador2, posicao_texto_jogador2)

        pygame.display.update()
   
# inserir o nome do jogador 1vbot
def abrir_janela_nomes_1vbot():
    
    janela_nomebot = pygame.display.set_mode((screen_width, screen_height))
    
    digitando = True
    jogador_atual = 1
    nome_jogador = ""

    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    abrir_janela_dificuldade() #clicar no enter, passa a prox janela

                elif evento.key == pygame.K_BACKSPACE:
                    nome_jogador = nome_jogador[:-1]

                else:
                    nome_jogador += evento.unicode

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if evento.button == 1:
                    if posicao_texto_jogador.collidepoint(evento.pos):
                        jogador_atual = 1
                        nome_jogador = ""
                    elif botao_voltar_redim.get_rect(topleft=(1200, 5)).collidepoint(mouse_pos):
                        return True

        janela_nomebot.blit(menu_nomebot_redim, (0, 0))
        janela_nomebot.blit(botao_voltar_redim, (1200, 5))

        # Exibindo o nome digitado na janela
        fonte = pygame.font.Font(None, 46)
        texto_jogador = fonte.render(nome_jogador, True, BRANCO)

        posicao_texto_jogador = texto_jogador.get_rect(midleft=(screen_width // 2 - 525, screen_height // 2 + 48))

        # Desenhar retângulo interativo para reescrever o nome
        pygame.draw.rect(janela_nomebot, CINZA, posicao_texto_jogador)

        janela_nomebot.blit(texto_jogador, posicao_texto_jogador)

        pygame.display.update()

    return False

# escolher dificuldade do bot
def abrir_janela_dificuldade():
    main_menu = False
    
    janela_dificuldade = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jogo do Semáforo")

    digitando = True
    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
        
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if botao_facil_redim.get_rect(topleft=(700,295)).collidepoint(mouse_pos):
                    print("funciona")

                elif botao_medio_redim.get_rect(topleft=(700,418)).collidepoint(mouse_pos):
                    print("tbm funciona")
                
                elif botao_dificil_redim.get_rect(topleft=(700,540)).collidepoint(mouse_pos):
                    print("tbm funciona :)")
                
                elif botao_voltar_redim.get_rect(topleft=(1200,5)).collidepoint(mouse_pos):
                    digitando = False 
        
        janela_dificuldade.blit(menu_escolhabot_redim, (0, 0))
        janela_dificuldade.blit(botao_facil_redim, (700, 295))
        janela_dificuldade.blit(botao_medio_redim, (700, 418))
        janela_dificuldade.blit(botao_dificil_redim, (700, 540))
        janela_dificuldade.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

    main_menu = True

#


################## MAIN ####################
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
    screen.blit(carregar_redim, (500, 372))
    screen.blit(regras_redim, (500,500))

    pygame.display.update()


