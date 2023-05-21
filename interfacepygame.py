import pygame
import random
random.seed()

pygame.init()

screen_width = 1280 
screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo do Semáforo")

# Definição das cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (68, 68, 68)

# import pagina inicial
pagina_inicial = pygame.image.load('pagina_inicial.png')
pagina_inicial_redim = pygame.transform.scale(pagina_inicial, (1280, 720)) 
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
# import fundo tabuleiro 
menu_tabuleiro = pygame.image.load("menu_tabuleiro.png")
menu_tabuleiro_redim = pygame.transform.scale(menu_tabuleiro, (1280, 720))
# import fundo vitoria
menu_vitoria = pygame.image.load("vitoria.png")
menu_vitoria_redim = pygame.transform.scale(menu_vitoria, (1280, 720))

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
# import botao passar vez
botao_passarvez = pygame.image.load('passarvez.png')
botao_passarvez_redim = pygame.transform.scale(botao_passarvez, (334,78))

# import botao tabuleiro
botao_tabuleiro_1_1 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_1_1_redim = pygame.transform.scale(botao_tabuleiro_1_1, (163, 133))

botao_tabuleiro_1_2 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_1_2_redim = pygame.transform.scale(botao_tabuleiro_1_2, (163, 133))

botao_tabuleiro_1_3 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_1_3_redim = pygame.transform.scale(botao_tabuleiro_1_1, (163, 133))

botao_tabuleiro_1_4 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_1_4_redim = pygame.transform.scale(botao_tabuleiro_1_4, (163, 133))

botao_tabuleiro_2_1 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_2_1_redim = pygame.transform.scale(botao_tabuleiro_2_1, (163, 133))

botao_tabuleiro_2_2 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_2_2_redim = pygame.transform.scale(botao_tabuleiro_2_2, (163, 133))

botao_tabuleiro_2_3 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_2_3_redim = pygame.transform.scale(botao_tabuleiro_2_3, (163, 133))

botao_tabuleiro_2_4 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_2_4_redim = pygame.transform.scale(botao_tabuleiro_2_4, (163, 133))

botao_tabuleiro_3_1 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_3_1_redim = pygame.transform.scale(botao_tabuleiro_3_1, (163, 133))

botao_tabuleiro_3_2 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_3_2_redim = pygame.transform.scale(botao_tabuleiro_3_2, (163, 133))

botao_tabuleiro_3_3 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_3_3_redim = pygame.transform.scale(botao_tabuleiro_3_3, (163, 133))
                                                   
botao_tabuleiro_3_4 = pygame.image.load('botao_tabuleiro.png')
botao_tabuleiro_3_4_redim = pygame.transform.scale(botao_tabuleiro_3_4, (163, 133))

# import label nome1
label_nome1 = pygame.image.load('nome1.png')
label_nome1_redim = pygame.transform.scale(label_nome1, (332,77))
# import label nome2
label_nome2 = pygame.image.load('nome2.png')
label_nome2_redim = pygame.transform.scale(label_nome2, (332,77))

# import botao menu (para a vitoria)
botao_menu = pygame.image.load('menu.png')
botao_menu_redim = pygame.transform.scale(botao_menu, (236,101)) #compor igual ao botao sair acho

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
                         abrir_tabuleiro_1v1(nome_jogador1[:15], nome_jogador2[:15])  # Limiting names to 15 characters

                elif event.key == pygame.K_BACKSPACE:
                    if jogador_atual == 1:
                        nome_jogador1 = nome_jogador1[:-1]
                    else:
                        nome_jogador2 = nome_jogador2[:-1]
                
                else:
                    if jogador_atual == 1:
                        if len(nome_jogador1) < 15:  # Limiting name length to 15 characters
                            nome_jogador1 += event.unicode
                    else:
                        if len(nome_jogador2) < 15:  # Limiting name length to 15 characters
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

        fonte = pygame.font.Font(None, 46)
        texto_jogador1 = fonte.render(nome_jogador1, True, BRANCO)
        texto_jogador2 = fonte.render(nome_jogador2, True, BRANCO)

        posicao_texto_jogador1 = texto_jogador1.get_rect(midleft=(screen_width // 2 - 525, screen_height // 2 + 48))
        posicao_texto_jogador2 = texto_jogador2.get_rect(midleft=(screen_width // 2 + 155, screen_height // 2 + 48))

        pygame.draw.rect(janela_nomes, CINZA, posicao_texto_jogador1)
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
                    if len(nome_jogador) < 15:  # Limitador de 15 caracteres
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
    nome_jogador = ""  # Variável para armazenar o nome do jogador
    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
        
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if botao_facil_redim.get_rect(topleft=(700,295)).collidepoint(mouse_pos):
                    abrir_tabuleiro_1vbot_facil(nome_jogador)

                elif botao_medio_redim.get_rect(topleft=(700,418)).collidepoint(mouse_pos):
                    abrir_tabuleiro_1vbot_medio(nome_jogador)
                
                elif botao_dificil_redim.get_rect(topleft=(700,540)).collidepoint(mouse_pos):
                    abrir_tabuleiro_1vbot_dificil(nome_jogador)  # Passa o nome do jogador como argumento
                
                elif botao_voltar_redim.get_rect(topleft=(1200, 5)).collidepoint(mouse_pos):
                    digitando = False 
        
        janela_dificuldade.blit(menu_escolhabot_redim, (0, 0))
        janela_dificuldade.blit(botao_facil_redim, (700, 295))
        janela_dificuldade.blit(botao_medio_redim, (700, 418))
        janela_dificuldade.blit(botao_dificil_redim, (700, 540))
        janela_dificuldade.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

    main_menu = True

def abrir_tabuleiro_1v1(nome_jogador1,nome_jogador2):
    janela_tabuleiro = pygame.display.set_mode((screen_width, screen_height))

    # Selecionar aleatoriamente o nome do jogador
    nome_jogador_selecionado = random.choice([nome_jogador1, nome_jogador2])
    
    circulo_redim = pygame.image.load('circulo.png')
    circulo_redim = pygame.transform.scale(circulo_redim, (125, 125))
    triangulo_redim = pygame.image.load('triangulo.png')
    triangulo_redim = pygame.transform.scale(triangulo_redim, (150, 150))
    quadrado_redim = pygame.image.load('quadrado.png')
    quadrado_redim = pygame.transform.scale(quadrado_redim, (150, 150))

    botao_vazio_redim = pygame.Surface((125, 125))
    botao_vazio_redim.fill((166, 124, 74))

    digitando = True
    imagem_botao_1_1 = botao_vazio_redim
    imagem_botao_1_2 = botao_vazio_redim
    imagem_botao_1_3 = botao_vazio_redim
    imagem_botao_1_4 = botao_vazio_redim 
    imagem_botao_2_1 = botao_vazio_redim
    imagem_botao_2_2 = botao_vazio_redim
    imagem_botao_2_3 = botao_vazio_redim
    imagem_botao_2_4 = botao_vazio_redim
    imagem_botao_3_1 = botao_vazio_redim
    imagem_botao_3_2 = botao_vazio_redim
    imagem_botao_3_3 = botao_vazio_redim
    imagem_botao_3_4 = botao_vazio_redim

    jogador_atual = 1

    vitoria(imagem_botao_1_1,imagem_botao_1_2,imagem_botao_1_3,imagem_botao_1_4,imagem_botao_2_1,imagem_botao_2_2,imagem_botao_2_3,imagem_botao_2_4,imagem_botao_3_1,imagem_botao_3_2,imagem_botao_3_3,imagem_botao_3_4)

    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if sair_redim.get_rect(topleft=(1052, 625)).collidepoint(mouse_pos):
                    pygame.quit()
                    quit() 
                elif botao_voltar_redim.get_rect(topleft=(1200, 5)).collidepoint(mouse_pos):
                    digitando = False
                
                elif botao_tabuleiro_1_1_redim.get_rect(topleft=(80, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_1_2_redim.get_rect(topleft=(254, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_3_redim.get_rect(topleft=(428, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_4_redim.get_rect(topleft=(602, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_1_redim.get_rect(topleft=(80, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_2_redim.get_rect(topleft=(254, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_3_redim.get_rect(topleft=(428, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
               
                elif botao_tabuleiro_2_4_redim.get_rect(topleft=(602, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_1_redim.get_rect(topleft=(80, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_2_redim.get_rect(topleft=(254, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_3_redim.get_rect(topleft=(428, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_3_4_redim.get_rect(topleft=(602, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do jogador 2")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

        janela_tabuleiro.blit(botao_voltar_redim, (1200, 5))
        janela_tabuleiro.blit(menu_tabuleiro_redim, (0, 0))

        janela_tabuleiro.blit(botao_tabuleiro_1_1_redim, (80, 214))
        janela_tabuleiro.blit(botao_tabuleiro_1_2_redim, (254, 214))
        janela_tabuleiro.blit(botao_tabuleiro_1_3_redim, (428, 214))
        janela_tabuleiro.blit(botao_tabuleiro_1_4_redim, (602, 214))

        janela_tabuleiro.blit(botao_tabuleiro_2_1_redim, (80, 358))
        janela_tabuleiro.blit(botao_tabuleiro_2_2_redim, (254, 358))
        janela_tabuleiro.blit(botao_tabuleiro_2_3_redim, (428, 358))
        janela_tabuleiro.blit(botao_tabuleiro_2_4_redim, (602, 358))

        janela_tabuleiro.blit(botao_tabuleiro_3_1_redim, (80, 502))
        janela_tabuleiro.blit(botao_tabuleiro_3_2_redim, (254, 502))
        janela_tabuleiro.blit(botao_tabuleiro_3_3_redim, (428, 502))
        janela_tabuleiro.blit(botao_tabuleiro_3_4_redim, (602, 502))

        # compor posiçao das peças
        if imagem_botao_1_1 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_1, (100, 217))
        elif imagem_botao_1_1 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_1, (86, 205))
        elif imagem_botao_1_1 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_1_1, (87, 205))

        if imagem_botao_1_2 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_2, (274, 217))
        elif imagem_botao_1_2 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_2, (260, 205))
        elif imagem_botao_1_2 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_1_2, (261, 205))

        if imagem_botao_1_3 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_3, (448, 217))
        elif imagem_botao_1_3 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_3, (434, 205))
        elif imagem_botao_1_3 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_1_3, (435, 205))

        if imagem_botao_1_4 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_4, (622, 217))
        elif imagem_botao_1_4 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_1_4, (608, 205))
        elif imagem_botao_1_4 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_1_4, (609, 205))

        if imagem_botao_2_1 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_1, (100, 361))
        elif imagem_botao_2_1 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_1, (86, 349))
        elif imagem_botao_2_1 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_2_1, (87, 349))

        if imagem_botao_2_2 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_2, (274, 361))
        elif imagem_botao_2_2 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_2, (260, 349))
        elif imagem_botao_2_2 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_2_2, (261, 349))

        if imagem_botao_2_3 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_3, (448, 361))
        elif imagem_botao_2_3 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_3, (434, 349))
        elif imagem_botao_2_3 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_2_3, (435, 349))

        if imagem_botao_2_4 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_4, (622, 361))
        elif imagem_botao_2_4 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_2_4, (608, 349))
        elif imagem_botao_2_4 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_2_4, (609, 349))

        if imagem_botao_3_1 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_1, (100, 505))
        elif imagem_botao_3_1 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_1, (86, 493))
        elif imagem_botao_3_1 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_3_1, (87, 493))

        if imagem_botao_3_2 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_2, (274, 505))
        elif imagem_botao_3_2 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_2, (260, 493))
        elif imagem_botao_3_2 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_3_2, (261, 493))

        if imagem_botao_3_3 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_3, (448, 505))
        elif imagem_botao_3_3 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_3, (434, 493))
        elif imagem_botao_3_3 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_3_3, (435, 493))

        if imagem_botao_3_4 == circulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_4, (622, 505))
        elif imagem_botao_3_4 == triangulo_redim:
            janela_tabuleiro.blit(imagem_botao_3_4, (608, 493))
        elif imagem_botao_3_4 == quadrado_redim:
            janela_tabuleiro.blit(imagem_botao_3_4, (609, 493))

        # Renderizar e posicionar o texto nome1
        fonte = pygame.font.Font(None, 46)
        texto_nome1 = fonte.render(nome_jogador1, True, BRANCO)
        posicao_nome1 = (900, 290)
        janela_tabuleiro.blit(label_nome1_redim, (855, 265))
        janela_tabuleiro.blit(texto_nome1, posicao_nome1)

        texto_nome2 = fonte.render(nome_jogador2, True, BRANCO)
        posicao_nome2 = (900, 375)
        janela_tabuleiro.blit(label_nome2_redim, (855, 350))
        janela_tabuleiro.blit(texto_nome2, posicao_nome2)

        if nome_jogador_selecionado == nome_jogador1:
            texto_nome_selecionado = fonte.render(nome_jogador_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro.blit(label_nome1_redim, (855, 120))
            janela_tabuleiro.blit(texto_nome_selecionado, posicao_nome_selecionado)

        else:
            texto_nome_selecionado = fonte.render(nome_jogador_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro.blit(label_nome2_redim, (855, 120))
            janela_tabuleiro.blit(texto_nome_selecionado, posicao_nome_selecionado)

        janela_tabuleiro.blit(botao_passarvez_redim, (855, 500))
        janela_tabuleiro.blit(sair_redim, (1052, 625))
        janela_tabuleiro.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

def vitoria(imagem_botao_1_1,imagem_botao_1_2,imagem_botao_1_3,imagem_botao_1_4,imagem_botao_2_1,imagem_botao_2_2,imagem_botao_2_3,imagem_botao_2_4,imagem_botao_3_1,imagem_botao_3_2,imagem_botao_3_3,imagem_botao_3_4):
    vit = False

    ##linhas
    if(imagem_botao_1_1 == imagem_botao_1_2 and imagem_botao_1_1 == imagem_botao_1_3 and imagem_botao_1_1 != '' and  imagem_botao_1_2 != '' and  imagem_botao_1_3 != '' ) :
        vit = True
    if(imagem_botao_1_2 == imagem_botao_1_3 and imagem_botao_1_2 == imagem_botao_1_4 and imagem_botao_1_2 != '' and  imagem_botao_1_3 != '' and  imagem_botao_1_4 != '' ) :
        vit = True
    if(imagem_botao_2_1 == imagem_botao_2_2 and imagem_botao_2_1 == imagem_botao_2_3 and imagem_botao_2_1 != '' and  imagem_botao_2_2 != '' and  imagem_botao_2_3 != '' ) :
        vit = True
    if(imagem_botao_2_2 == imagem_botao_2_3 and imagem_botao_2_2 == imagem_botao_2_4 and imagem_botao_2_2 != '' and  imagem_botao_2_3 != '' and  imagem_botao_2_4 != '' ) :
        vit = True
    if(imagem_botao_3_1 == imagem_botao_3_2 and imagem_botao_3_1 == imagem_botao_3_3 and imagem_botao_3_1 != '' and  imagem_botao_3_2 != '' and  imagem_botao_3_3 != '' ) :
        vit = True
    if(imagem_botao_3_2 == imagem_botao_3_3 and imagem_botao_3_2 == imagem_botao_3_4 and imagem_botao_3_2 != '' and  imagem_botao_3_3 != '' and  imagem_botao_3_4 != '' ) :
        vit = True

    ##colunas
    if(imagem_botao_1_1 == imagem_botao_2_1 and imagem_botao_1_1 == imagem_botao_3_1 and imagem_botao_1_1 != '' and  imagem_botao_2_1 != '' and  imagem_botao_3_1 != '' ) :
        vit = True
    if(imagem_botao_1_2 == imagem_botao_2_2 and imagem_botao_1_2 == imagem_botao_3_2 and imagem_botao_1_2 != '' and  imagem_botao_2_2 != '' and  imagem_botao_3_2 != '' ) :
        vit = True
    if(imagem_botao_1_3 == imagem_botao_2_3 and imagem_botao_1_3 == imagem_botao_3_3 and imagem_botao_1_3 != '' and  imagem_botao_2_3 != '' and  imagem_botao_3_3 != '' ) :
        vit = True
    if(imagem_botao_1_4 == imagem_botao_2_4 and imagem_botao_1_4 == imagem_botao_3_4 and imagem_botao_1_4 != '' and  imagem_botao_2_4 != '' and  imagem_botao_3_4 != '' ) :
        vit = True

    #diagonais
    if(imagem_botao_1_1 == imagem_botao_2_2 and imagem_botao_1_1 == imagem_botao_3_3 and imagem_botao_1_1 != '' and  imagem_botao_2_2 != '' and  imagem_botao_3_3 != '' ) :
        vit = True
    if(imagem_botao_1_2 == imagem_botao_2_3 and imagem_botao_1_2 == imagem_botao_3_4 and imagem_botao_1_2 != '' and  imagem_botao_2_3 != '' and  imagem_botao_3_4 != '' ) :
        vit = True
    if(imagem_botao_3_1 == imagem_botao_2_2 and imagem_botao_3_1 == imagem_botao_1_3 and imagem_botao_3_1 != '' and  imagem_botao_2_2 != '' and  imagem_botao_1_3 != '' ) :
        vit = True
    if(imagem_botao_3_2 == imagem_botao_2_3 and imagem_botao_3_2 == imagem_botao_1_4 and imagem_botao_3_2 != '' and  imagem_botao_2_3 != '' and  imagem_botao_1_4 != '' ) :
        vit = True

def abrir_tabuleiro_1vbot_facil(nome_jogador):

    janela_tabuleiro_1vbot_facil = pygame.display.set_mode((screen_width, screen_height))

    bot = "BOT"
    nome_ou_bot_selecionado = random.choice([nome_jogador, bot])

    circulo_redim = pygame.image.load('circulo.png')
    circulo_redim = pygame.transform.scale(circulo_redim, (125, 125))
    triangulo_redim = pygame.image.load('triangulo.png')
    triangulo_redim = pygame.transform.scale(triangulo_redim, (150, 150))
    quadrado_redim = pygame.image.load('quadrado.png')
    quadrado_redim = pygame.transform.scale(quadrado_redim, (150, 150))

    botao_vazio_redim = pygame.Surface((125, 125))
    botao_vazio_redim.fill((166, 124, 74))

    digitando = True
    imagem_botao_1_1 = botao_vazio_redim
    imagem_botao_1_2 = botao_vazio_redim
    imagem_botao_1_3 = botao_vazio_redim
    imagem_botao_1_4 = botao_vazio_redim 
    imagem_botao_2_1 = botao_vazio_redim
    imagem_botao_2_2 = botao_vazio_redim
    imagem_botao_2_3 = botao_vazio_redim
    imagem_botao_2_4 = botao_vazio_redim
    imagem_botao_3_1 = botao_vazio_redim
    imagem_botao_3_2 = botao_vazio_redim
    imagem_botao_3_3 = botao_vazio_redim
    imagem_botao_3_4 = botao_vazio_redim

    jogador_atual = 1

    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if sair_redim.get_rect(topleft=(1052, 625)).collidepoint(mouse_pos):
                    pygame.quit()
                    quit() 
                elif botao_voltar_redim.get_rect(topleft=(1200, 5)).collidepoint(mouse_pos):
                    digitando = False
                
                elif botao_tabuleiro_1_1_redim.get_rect(topleft=(80, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_1_2_redim.get_rect(topleft=(254, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_3_redim.get_rect(topleft=(428, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_4_redim.get_rect(topleft=(602, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_1_redim.get_rect(topleft=(80, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_2_redim.get_rect(topleft=(254, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_3_redim.get_rect(topleft=(428, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
               
                elif botao_tabuleiro_2_4_redim.get_rect(topleft=(602, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_1_redim.get_rect(topleft=(80, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_2_redim.get_rect(topleft=(254, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_3_redim.get_rect(topleft=(428, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_3_4_redim.get_rect(topleft=(602, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                

        janela_tabuleiro_1vbot_facil.blit(botao_voltar_redim, (1200, 5))
        janela_tabuleiro_1vbot_facil.blit(menu_tabuleiro_redim, (0, 0))

        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_1_1_redim, (80, 214))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_1_2_redim, (254, 214))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_1_3_redim, (428, 214))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_1_4_redim, (602, 214))

        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_2_1_redim, (80, 358))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_2_2_redim, (254, 358))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_2_3_redim, (428, 358))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_2_4_redim, (602, 358))

        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_3_1_redim, (80, 502))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_3_2_redim, (254, 502))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_3_3_redim, (428, 502))
        janela_tabuleiro_1vbot_facil.blit(botao_tabuleiro_3_4_redim, (602, 502))

        # compor posiçao das peças
        if imagem_botao_1_1 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_1, (100, 217))
        elif imagem_botao_1_1 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_1, (86, 205))
        elif imagem_botao_1_1 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_1, (87, 205))

        if imagem_botao_1_2 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_2, (274, 217))
        elif imagem_botao_1_2 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_2, (260, 205))
        elif imagem_botao_1_2 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_2, (261, 205))

        if imagem_botao_1_3 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_3, (448, 217))
        elif imagem_botao_1_3 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_3, (434, 205))
        elif imagem_botao_1_3 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_3, (435, 205))

        if imagem_botao_1_4 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_4, (622, 217))
        elif imagem_botao_1_4 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_4, (608, 205))
        elif imagem_botao_1_4 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_1_4, (609, 205))

        if imagem_botao_2_1 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_1, (100, 361))
        elif imagem_botao_2_1 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_1, (86, 349))
        elif imagem_botao_2_1 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_1, (87, 349))

        if imagem_botao_2_2 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_2, (274, 361))
        elif imagem_botao_2_2 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_2, (260, 349))
        elif imagem_botao_2_2 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_2, (261, 349))

        if imagem_botao_2_3 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_3, (448, 361))
        elif imagem_botao_2_3 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_3, (434, 349))
        elif imagem_botao_2_3 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_3, (435, 349))

        if imagem_botao_2_4 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_4, (622, 361))
        elif imagem_botao_2_4 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_4, (608, 349))
        elif imagem_botao_2_4 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_2_4, (609, 349))

        if imagem_botao_3_1 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_1, (100, 505))
        elif imagem_botao_3_1 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_1, (86, 493))
        elif imagem_botao_3_1 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_1, (87, 493))

        if imagem_botao_3_2 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_2, (274, 505))
        elif imagem_botao_3_2 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_2, (260, 493))
        elif imagem_botao_3_2 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_2, (261, 493))

        if imagem_botao_3_3 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_3, (448, 505))
        elif imagem_botao_3_3 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_3, (434, 493))
        elif imagem_botao_3_3 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_3, (435, 493))

        if imagem_botao_3_4 == circulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_4, (622, 505))
        elif imagem_botao_3_4 == triangulo_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_4, (608, 493))
        elif imagem_botao_3_4 == quadrado_redim:
            janela_tabuleiro_1vbot_facil.blit(imagem_botao_3_4, (609, 493))
 

        # Renderizar e posicionar o texto nome1
        fonte = pygame.font.Font(None, 46)
        texto_nome = fonte.render(nome_jogador, True, BRANCO)
        posicao_nome1 = (900, 290)
        janela_tabuleiro_1vbot_facil.blit(label_nome1_redim, (855, 265))
        janela_tabuleiro_1vbot_facil.blit(texto_nome, posicao_nome1)

        texto_nome2 = fonte.render("BOT", True, BRANCO)
        posicao_nome2 = (900, 375)
        janela_tabuleiro_1vbot_facil.blit(label_nome2_redim, (855, 350))
        janela_tabuleiro_1vbot_facil.blit(texto_nome2, posicao_nome2)

        if nome_ou_bot_selecionado == nome_jogador:
            texto_nome_selecionado = fonte.render(nome_ou_bot_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro_1vbot_facil.blit(label_nome1_redim, (855, 120))
            janela_tabuleiro_1vbot_facil.blit(texto_nome_selecionado, posicao_nome_selecionado)
        else:
            texto_nome_selecionado = fonte.render(nome_ou_bot_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro_1vbot_facil.blit(label_nome2_redim, (855, 120))
            janela_tabuleiro_1vbot_facil.blit(texto_nome_selecionado, posicao_nome_selecionado)

        janela_tabuleiro_1vbot_facil.blit(texto_nome_selecionado, posicao_nome_selecionado)
        janela_tabuleiro_1vbot_facil.blit(botao_passarvez_redim, (855, 500))
        janela_tabuleiro_1vbot_facil.blit(sair_redim, (1052, 625))
        janela_tabuleiro_1vbot_facil.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

def abrir_tabuleiro_1vbot_medio(nome_jogador):

    janela_tabuleiro_1vbot_medio = pygame.display.set_mode((screen_width, screen_height))

    bot = "BOT"
    nome_ou_bot_selecionado = random.choice([nome_jogador, bot])

    circulo_redim = pygame.image.load('circulo.png')
    circulo_redim = pygame.transform.scale(circulo_redim, (125, 125))
    triangulo_redim = pygame.image.load('triangulo.png')
    triangulo_redim = pygame.transform.scale(triangulo_redim, (150, 150))
    quadrado_redim = pygame.image.load('quadrado.png')
    quadrado_redim = pygame.transform.scale(quadrado_redim, (150, 150))

    botao_vazio_redim = pygame.Surface((125, 125))
    botao_vazio_redim.fill((166, 124, 74))

    digitando = True
    imagem_botao_1_1 = botao_vazio_redim
    imagem_botao_1_2 = botao_vazio_redim
    imagem_botao_1_3 = botao_vazio_redim
    imagem_botao_1_4 = botao_vazio_redim 
    imagem_botao_2_1 = botao_vazio_redim
    imagem_botao_2_2 = botao_vazio_redim
    imagem_botao_2_3 = botao_vazio_redim
    imagem_botao_2_4 = botao_vazio_redim
    imagem_botao_3_1 = botao_vazio_redim
    imagem_botao_3_2 = botao_vazio_redim
    imagem_botao_3_3 = botao_vazio_redim
    imagem_botao_3_4 = botao_vazio_redim

    jogador_atual = 1

    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if sair_redim.get_rect(topleft=(1052, 625)).collidepoint(mouse_pos):
                    pygame.quit()
                    quit() 
                elif botao_voltar_redim.get_rect(topleft=(1200, 5)).collidepoint(mouse_pos):
                    digitando = False
                
                elif botao_tabuleiro_1_1_redim.get_rect(topleft=(80, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_1_2_redim.get_rect(topleft=(254, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_3_redim.get_rect(topleft=(428, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_4_redim.get_rect(topleft=(602, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_1_redim.get_rect(topleft=(80, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_2_redim.get_rect(topleft=(254, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_3_redim.get_rect(topleft=(428, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
               
                elif botao_tabuleiro_2_4_redim.get_rect(topleft=(602, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_1_redim.get_rect(topleft=(80, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_2_redim.get_rect(topleft=(254, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_3_redim.get_rect(topleft=(428, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_3_4_redim.get_rect(topleft=(602, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                

        janela_tabuleiro_1vbot_medio.blit(botao_voltar_redim, (1200, 5))
        janela_tabuleiro_1vbot_medio.blit(menu_tabuleiro_redim, (0, 0))

        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_1_1_redim, (80, 214))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_1_2_redim, (254, 214))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_1_3_redim, (428, 214))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_1_4_redim, (602, 214))

        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_2_1_redim, (80, 358))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_2_2_redim, (254, 358))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_2_3_redim, (428, 358))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_2_4_redim, (602, 358))

        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_3_1_redim, (80, 502))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_3_2_redim, (254, 502))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_3_3_redim, (428, 502))
        janela_tabuleiro_1vbot_medio.blit(botao_tabuleiro_3_4_redim, (602, 502))

        # compor posiçao das peças
        if imagem_botao_1_1 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_1, (100, 217))
        elif imagem_botao_1_1 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_1, (86, 205))
        elif imagem_botao_1_1 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_1, (87, 205))

        if imagem_botao_1_2 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_2, (274, 217))
        elif imagem_botao_1_2 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_2, (260, 205))
        elif imagem_botao_1_2 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_2, (261, 205))

        if imagem_botao_1_3 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_3, (448, 217))
        elif imagem_botao_1_3 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_3, (434, 205))
        elif imagem_botao_1_3 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_3, (435, 205))

        if imagem_botao_1_4 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_4, (622, 217))
        elif imagem_botao_1_4 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_4, (608, 205))
        elif imagem_botao_1_4 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_1_4, (609, 205))

        if imagem_botao_2_1 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_1, (100, 361))
        elif imagem_botao_2_1 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_1, (86, 349))
        elif imagem_botao_2_1 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_1, (87, 349))

        if imagem_botao_2_2 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_2, (274, 361))
        elif imagem_botao_2_2 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_2, (260, 349))
        elif imagem_botao_2_2 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_2, (261, 349))

        if imagem_botao_2_3 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_3, (448, 361))
        elif imagem_botao_2_3 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_3, (434, 349))
        elif imagem_botao_2_3 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_3, (435, 349))

        if imagem_botao_2_4 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_4, (622, 361))
        elif imagem_botao_2_4 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_4, (608, 349))
        elif imagem_botao_2_4 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_2_4, (609, 349))

        if imagem_botao_3_1 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_1, (100, 505))
        elif imagem_botao_3_1 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_1, (86, 493))
        elif imagem_botao_3_1 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_1, (87, 493))

        if imagem_botao_3_2 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_2, (274, 505))
        elif imagem_botao_3_2 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_2, (260, 493))
        elif imagem_botao_3_2 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_2, (261, 493))

        if imagem_botao_3_3 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_3, (448, 505))
        elif imagem_botao_3_3 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_3, (434, 493))
        elif imagem_botao_3_3 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_3, (435, 493))

        if imagem_botao_3_4 == circulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_4, (622, 505))
        elif imagem_botao_3_4 == triangulo_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_4, (608, 493))
        elif imagem_botao_3_4 == quadrado_redim:
            janela_tabuleiro_1vbot_medio.blit(imagem_botao_3_4, (609, 493))
 

        # Renderizar e posicionar o texto nome1
        fonte = pygame.font.Font(None, 46)
        texto_nome = fonte.render(nome_jogador, True, BRANCO)
        posicao_nome1 = (900, 290)
        janela_tabuleiro_1vbot_medio.blit(label_nome1_redim, (855, 265))
        janela_tabuleiro_1vbot_medio.blit(texto_nome, posicao_nome1)

        texto_nome2 = fonte.render("BOT", True, BRANCO)
        posicao_nome2 = (900, 375)
        janela_tabuleiro_1vbot_medio.blit(label_nome2_redim, (855, 350))
        janela_tabuleiro_1vbot_medio.blit(texto_nome2, posicao_nome2)

        if nome_ou_bot_selecionado == nome_jogador:
            texto_nome_selecionado = fonte.render(nome_ou_bot_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro_1vbot_medio.blit(label_nome1_redim, (855, 120))
            janela_tabuleiro_1vbot_medio.blit(texto_nome_selecionado, posicao_nome_selecionado)
        else:
            texto_nome_selecionado = fonte.render(nome_ou_bot_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro_1vbot_medio.blit(label_nome2_redim, (855, 120))
            janela_tabuleiro_1vbot_medio.blit(texto_nome_selecionado, posicao_nome_selecionado)

        janela_tabuleiro_1vbot_medio.blit(texto_nome_selecionado, posicao_nome_selecionado)
        janela_tabuleiro_1vbot_medio.blit(botao_passarvez_redim, (855, 500))
        janela_tabuleiro_1vbot_medio.blit(sair_redim, (1052, 625))
        janela_tabuleiro_1vbot_medio.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

def abrir_tabuleiro_1vbot_dificil(nome_jogador):
    
    janela_tabuleiro_1vbot_dificil = pygame.display.set_mode((screen_width, screen_height))

    bot = "BOT"
    nome_ou_bot_selecionado = random.choice([nome_jogador, bot])

    circulo_redim = pygame.image.load('circulo.png')
    circulo_redim = pygame.transform.scale(circulo_redim, (125, 125))
    triangulo_redim = pygame.image.load('triangulo.png')
    triangulo_redim = pygame.transform.scale(triangulo_redim, (150, 150))
    quadrado_redim = pygame.image.load('quadrado.png')
    quadrado_redim = pygame.transform.scale(quadrado_redim, (150, 150))

    botao_vazio_redim = pygame.Surface((125, 125))
    botao_vazio_redim.fill((166, 124, 74))

    digitando = True
    imagem_botao_1_1 = botao_vazio_redim
    imagem_botao_1_2 = botao_vazio_redim
    imagem_botao_1_3 = botao_vazio_redim
    imagem_botao_1_4 = botao_vazio_redim 
    imagem_botao_2_1 = botao_vazio_redim
    imagem_botao_2_2 = botao_vazio_redim
    imagem_botao_2_3 = botao_vazio_redim
    imagem_botao_2_4 = botao_vazio_redim
    imagem_botao_3_1 = botao_vazio_redim
    imagem_botao_3_2 = botao_vazio_redim
    imagem_botao_3_3 = botao_vazio_redim
    imagem_botao_3_4 = botao_vazio_redim

    jogador_atual = 1

    while digitando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if sair_redim.get_rect(topleft=(1052, 625)).collidepoint(mouse_pos):
                    pygame.quit()
                    quit() 
                elif botao_voltar_redim.get_rect(topleft=(1200, 5)).collidepoint(mouse_pos):
                    digitando = False
                
                elif botao_tabuleiro_1_1_redim.get_rect(topleft=(80, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_1_2_redim.get_rect(topleft=(254, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_3_redim.get_rect(topleft=(428, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_1_4_redim.get_rect(topleft=(602, 214)).collidepoint(mouse_pos):
                    if imagem_botao_1_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_1_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_1_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_1_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_1_redim.get_rect(topleft=(80, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_2_redim.get_rect(topleft=(254, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_2_3_redim.get_rect(topleft=(428, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
               
                elif botao_tabuleiro_2_4_redim.get_rect(topleft=(602, 358)).collidepoint(mouse_pos):
                    if imagem_botao_2_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_2_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_2_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_2_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_1_redim.get_rect(topleft=(80, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_1 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_1 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_1 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_1 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_2_redim.get_rect(topleft=(254, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_2 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_2 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_2 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_2 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                
                elif botao_tabuleiro_3_3_redim.get_rect(topleft=(428, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_3 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_3 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_3 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_3 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")

                elif botao_tabuleiro_3_4_redim.get_rect(topleft=(602, 502)).collidepoint(mouse_pos):
                    if imagem_botao_3_4 == botao_vazio_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = circulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                    elif imagem_botao_3_4 == circulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = triangulo_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")                       
                    elif imagem_botao_3_4 == triangulo_redim:
                        if jogador_atual == 1:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 2
                            print("É a vez do BOT")
                        elif jogador_atual == 2:
                            imagem_botao_3_4 = quadrado_redim
                            jogador_atual = 1
                            print("É a vez do jogador 1")
                

        janela_tabuleiro_1vbot_dificil.blit(botao_voltar_redim, (1200, 5))
        janela_tabuleiro_1vbot_dificil.blit(menu_tabuleiro_redim, (0, 0))

        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_1_1_redim, (80, 214))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_1_2_redim, (254, 214))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_1_3_redim, (428, 214))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_1_4_redim, (602, 214))

        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_2_1_redim, (80, 358))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_2_2_redim, (254, 358))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_2_3_redim, (428, 358))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_2_4_redim, (602, 358))

        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_3_1_redim, (80, 502))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_3_2_redim, (254, 502))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_3_3_redim, (428, 502))
        janela_tabuleiro_1vbot_dificil.blit(botao_tabuleiro_3_4_redim, (602, 502))

        # compor posiçao das peças
        if imagem_botao_1_1 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_1, (100, 217))
        elif imagem_botao_1_1 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_1, (86, 205))
        elif imagem_botao_1_1 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_1, (87, 205))

        if imagem_botao_1_2 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_2, (274, 217))
        elif imagem_botao_1_2 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_2, (260, 205))
        elif imagem_botao_1_2 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_2, (261, 205))

        if imagem_botao_1_3 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_3, (448, 217))
        elif imagem_botao_1_3 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_3, (434, 205))
        elif imagem_botao_1_3 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_3, (435, 205))

        if imagem_botao_1_4 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_4, (622, 217))
        elif imagem_botao_1_4 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_4, (608, 205))
        elif imagem_botao_1_4 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_1_4, (609, 205))

        if imagem_botao_2_1 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_1, (100, 361))
        elif imagem_botao_2_1 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_1, (86, 349))
        elif imagem_botao_2_1 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_1, (87, 349))

        if imagem_botao_2_2 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_2, (274, 361))
        elif imagem_botao_2_2 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_2, (260, 349))
        elif imagem_botao_2_2 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_2, (261, 349))

        if imagem_botao_2_3 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_3, (448, 361))
        elif imagem_botao_2_3 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_3, (434, 349))
        elif imagem_botao_2_3 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_3, (435, 349))

        if imagem_botao_2_4 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_4, (622, 361))
        elif imagem_botao_2_4 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_4, (608, 349))
        elif imagem_botao_2_4 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_2_4, (609, 349))

        if imagem_botao_3_1 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_1, (100, 505))
        elif imagem_botao_3_1 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_1, (86, 493))
        elif imagem_botao_3_1 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_1, (87, 493))

        if imagem_botao_3_2 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_2, (274, 505))
        elif imagem_botao_3_2 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_2, (260, 493))
        elif imagem_botao_3_2 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_2, (261, 493))

        if imagem_botao_3_3 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_3, (448, 505))
        elif imagem_botao_3_3 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_3, (434, 493))
        elif imagem_botao_3_3 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_3, (435, 493))

        if imagem_botao_3_4 == circulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_4, (622, 505))
        elif imagem_botao_3_4 == triangulo_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_4, (608, 493))
        elif imagem_botao_3_4 == quadrado_redim:
            janela_tabuleiro_1vbot_dificil.blit(imagem_botao_3_4, (609, 493))
 

        # Renderizar e posicionar o texto nome1
        fonte = pygame.font.Font(None, 46)
        texto_nome = fonte.render(nome_jogador, True, BRANCO)
        posicao_nome1 = (900, 290)
        janela_tabuleiro_1vbot_dificil.blit(label_nome1_redim, (855, 265))
        janela_tabuleiro_1vbot_dificil.blit(texto_nome, posicao_nome1)

        texto_nome2 = fonte.render("BOT", True, BRANCO)
        posicao_nome2 = (900, 375)
        janela_tabuleiro_1vbot_dificil.blit(label_nome2_redim, (855, 350))
        janela_tabuleiro_1vbot_dificil.blit(texto_nome2, posicao_nome2)

        if nome_ou_bot_selecionado == nome_jogador:
            texto_nome_selecionado = fonte.render(nome_ou_bot_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro_1vbot_dificil.blit(label_nome1_redim, (855, 120))
            janela_tabuleiro_1vbot_dificil.blit(texto_nome_selecionado, posicao_nome_selecionado)
        else:
            texto_nome_selecionado = fonte.render(nome_ou_bot_selecionado, True, BRANCO)
            posicao_nome_selecionado = (900, 145)
            janela_tabuleiro_1vbot_dificil.blit(label_nome2_redim, (855, 120))
            janela_tabuleiro_1vbot_dificil.blit(texto_nome_selecionado, posicao_nome_selecionado)

        janela_tabuleiro_1vbot_dificil.blit(texto_nome_selecionado, posicao_nome_selecionado)
        janela_tabuleiro_1vbot_dificil.blit(botao_passarvez_redim, (855, 500))
        janela_tabuleiro_1vbot_dificil.blit(sair_redim, (1052, 625))
        janela_tabuleiro_1vbot_dificil.blit(botao_voltar_redim, (1200, 5))

        pygame.display.update()

# menu principal com as opções de jogo
def abrir_menu_jogo():
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

############## MAIN ################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            abrir_menu_jogo()
    
    screen.blit(pagina_inicial_redim, (0,0))

    pygame.display.update()
