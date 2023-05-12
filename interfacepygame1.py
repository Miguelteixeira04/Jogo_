import pygame


def botao_sair():
    # Definir as coordenadas e dimensões do botão
    botao_largura = 150
    botao_altura = 75
    # Posição x no canto inferior direito
    botao_pos_x = largura - botao_largura - 2
    # Posição y no canto inferior direito
    botao_pos_y = altura - botao_altura - 2

    # Criar uma fonte para o texto do botão
    fonte_botao = pygame.font.Font(None, 30)

    # Renderizar o texto "Sair"
    texto_sair = fonte_botao.render("Sair", True, cor_texto_sair)

    # Desenhar o botão na janela
    pygame.draw.rect(janela, cor_botao_sair, (botao_pos_x, botao_pos_y, botao_largura, botao_altura))

    # Desenhar o texto "Sair" no botão
    texto_retangulo = texto_sair.get_rect(center=(botao_pos_x + botao_largura / 2, botao_pos_y + botao_altura / 2))
    janela.blit(texto_sair, texto_retangulo)

    # Verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Verificar se o botão do mouse foi pressionado
            if botao_pos_x <= evento.pos[0] <= botao_pos_x + botao_largura and botao_pos_y <= evento.pos[1] <= botao_pos_y + botao_altura:
                # Clicou no botão, fechar o programa
                pygame.quit()
                quit()

def label_titulo():
    # Criar uma fonte para o texto da label
    fonte_label = pygame.font.SysFont(None, 75)  # Usar uma fonte padrão

    # Renderizar o texto da label
    texto_label = fonte_label.render("JOGO DO SEMÁFORO", True, cor_texto_titulo)
    
    # Desenhar a label "JOGO DO SEMÁFORO" no topo central da janela
    label_retangulo = texto_label.get_rect(midtop=(largura / 2, 65))
    janela.blit(texto_label, label_retangulo)

#def logo_utad():
    # Desenhar a imagem do logo na janela
#    janela.blit(imagem_logo, (imagem_logo_pos_x, imagem_logo_pos_y))

#def imagem_semaforo():
     # Desenhar a imagem do semáforo na janela
#     janela.blit(imagem_tabuleiro, (imagem_pos_x, imagem_pos_y))

def botao_começar():
    # Definir as coordenadas e dimensões do botão
    botao_largura = 200
    botao_altura = 75
    # Posição x no centro da janela
    botao_pos_x = (largura - botao_largura) // 2
    # Posição y um pouco acima do centro da janela
    botao_pos_y = altura // 2 - botao_altura -45

    # Criar uma fonte para o texto do botão
    fonte_botao = pygame.font.Font(None, 30)

    # Renderizar o texto "Começar"
    texto_comecar = fonte_botao.render("Começar", True, cor_texto_sair)

    # Desenhar o botão na janela
    pygame.draw.rect(janela, cor_botao_sair, (botao_pos_x, botao_pos_y, botao_largura, botao_altura))

    # Desenhar o texto "Começar" no botão
    texto_retangulo = texto_comecar.get_rect(center=(botao_pos_x + botao_largura / 2, botao_pos_y + botao_altura / 2))
    janela.blit(texto_comecar, texto_retangulo)

def botao_carregar():
    # Definir as coordenadas e dimensões do botão
    botao_largura = 200
    botao_altura = 75
    # Posição x no centro da janela
    botao_pos_x = (largura - botao_largura) // 2
    # Posição y um pouco acima do centro da janela
    botao_pos_y = altura // 2 - botao_altura + 65

    # Criar uma fonte para o texto do botão
    fonte_botao = pygame.font.Font(None, 30)

    # Renderizar o texto "Começar"
    texto_carregar = fonte_botao.render("Carregar", True, cor_texto_sair)

    # Desenhar o botão na janela
    pygame.draw.rect(janela, cor_botao_sair, (botao_pos_x, botao_pos_y, botao_largura, botao_altura))

    # Desenhar o texto "Começar" no botão
    texto_retangulo = texto_carregar.get_rect(center=(botao_pos_x + botao_largura / 2, botao_pos_y + botao_altura / 2))
    janela.blit(texto_carregar, texto_retangulo)

def botao_descricao_regras():
    # Definir as coordenadas e dimensões do botão
    botao_largura = 200
    botao_altura = 75
    # Posição x no centro da janela
    botao_pos_x = (largura - botao_largura) // 2
    # Posição y um pouco acima do centro da janela
    botao_pos_y = altura // 2 - botao_altura + 175

    # Criar uma fonte para o texto do botão
    fonte_botao = pygame.font.Font(None, 30)

    # Renderizar o texto "Descricao/Regras"
    texto_descricao_regras = fonte_botao.render("Descricao/Regras", True, cor_texto_sair)

    # Desenhar o botão na janela
    pygame.draw.rect(janela, cor_botao_sair, (botao_pos_x, botao_pos_y, botao_largura, botao_altura))

    # Desenhar o texto "Descricao/Regras" no botão
    texto_retangulo = texto_descricao_regras.get_rect(center=(botao_pos_x + botao_largura / 2, botao_pos_y + botao_altura / 2))
    janela.blit(texto_descricao_regras, texto_retangulo)

    # Verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Verificar se o botão do mouse foi pressionado
            if botao_pos_x <= evento.pos[0] <= botao_pos_x + botao_largura and botao_pos_y <= evento.pos[1] <= botao_pos_y + botao_altura: 
                    # Clicou no botão, abrir as regras do jogo
                    from Jogo import regras #isto está a importar o Jogo todo no terminal e não so as regras :,)
                    desc_regras = regras() 
                    # Criar uma nova janela para exibir as regras
                    janela_desc_regras = pygame.display.set_mode((800, 600))
                    # Criar uma fonte para o texto das regras
                    fonte_regras = pygame.font.Font(None, 30)
                    # Renderizar o texto das regras
                    texto_regras = fonte_regras.render(desc_regras, True, cor_texto_sair)
                    # Exibir o texto das regras na nova janela
                    janela_desc_regras.blit(texto_regras, (10, 10))
                    # Atualizar a nova janela
                    pygame.display.flip() #ns se é preciso

def label_nome_diogo():
    # Criar uma fonte para o texto da label
    fonte_label = pygame.font.SysFont(None, 30)  # Usar uma fonte padrão

    # Renderizar o texto da label
    texto_label = fonte_label.render("Diogo Cabral  al78834", True, cor_nomes)
    
    # Desenhar a label no meio da lateral esquerda da janela
    label_retangulo = texto_label.get_rect(midleft=(10, altura -200))
    janela.blit(texto_label, label_retangulo)

def label_nome_ines():
    # Criar uma fonte para o texto da label
    fonte_label = pygame.font.SysFont(None, 30)  # Usar uma fonte padrão

    # Renderizar o texto da label
    texto_label = fonte_label.render("Maria Inês  al78222", True, cor_nomes)
    
    # Desenhar a label no meio da lateral esquerda da janela
    label_retangulo = texto_label.get_rect(midleft=(10, altura -160))
    janela.blit(texto_label, label_retangulo)

def label_nome_miguel():
    # Criar uma fonte para o texto da label
    fonte_label = pygame.font.SysFont(None, 30)  # Usar uma fonte padrão

    # Renderizar o texto da label
    texto_label = fonte_label.render("Miguel Teixeira  al78321", True, cor_nomes)
    
    # Desenhar a label no meio da lateral esquerda da janela
    label_retangulo = texto_label.get_rect(midleft=(10, altura -120))
    janela.blit(texto_label, label_retangulo)

def label_nome_cadeira():
    # Criar uma fonte para o texto da label
    fonte_label = pygame.font.SysFont(None, 30)  # Usar uma fonte padrão

    # Renderizar o texto da label
    texto_label = fonte_label.render("Laboratório de programação          Eng. Informática    2022/2023", True, cor_texto_titulo)
    
    # Desenhar a label no meio da lateral esquerda da janela
    label_retangulo = texto_label.get_rect(midleft=(10, altura-18))
    janela.blit(texto_label, label_retangulo)

#def imagem_simbolos():
    # Desenhar a imagem dos símbolos na janela
#    janela.blit(imagem_simbolo, (imagem_simbolos_pos_x, imagem_simbolos_pos_y))


# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
largura = 800
altura = 600

# Criar a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO DO SEMÁFORO")

# Definir as cores
cor_fundo = (244, 218, 241)  
cor_botao_sair = (64, 64, 64) #cinzento  
cor_texto_sair = (255, 255, 255) #branco
cor_texto_titulo = (214, 86, 56)  #laranja
cor_nomes = (0,0,0) #preto

##################################### Carregar logo utad ################################################
#imagem_logo = pygame.image.load("logo.png")
# Tamanho 
#largura_imagem_logo = 150
#altura_imagem_logo = int(imagem_logo.get_height() * (largura_imagem_logo / imagem_logo.get_width()))
#imagem_logo = pygame.transform.scale(imagem_logo, (largura_imagem_logo, altura_imagem_logo))
# Definir a posição da imagem do logo
#imagem_logo_pos_x = 645
#imagem_logo_pos_y = 10

##################################### Carregar imagem semáforo ###########################################
#imagem_tabuleiro = pygame.image.load("tabuleiro.png")
# Tamanho 
#largura_imagem_tabuleiro = 250
#altura_imagem_tabuleiro = int(imagem_tabuleiro.get_height() * (largura_imagem_tabuleiro / imagem_tabuleiro.get_width()))
#imagem_tabuleiro = pygame.transform.scale(imagem_tabuleiro, (largura_imagem_tabuleiro, altura_imagem_tabuleiro))
# Definir a posição da imagem do semáforo
#imagem_pos_x = 10
#imagem_pos_y = 150

##################################### Carregar imagem simbolo ###########################################
#imagem_simbolo = pygame.image.load("simbolos.png")
# Tamanho
#largura_imagem_simbolo = 250
#altura_imagem_simbolo = int(imagem_simbolo.get_height() * (largura_imagem_simbolo / imagem_simbolo.get_width()))
#imagem_simbolo = pygame.transform.scale(imagem_simbolo, (largura_imagem_simbolo, altura_imagem_simbolo))
# Definir a posição da imagem dos símbolos
#imagem_simbolos_pos_x = 530
#imagem_simbolos_pos_y = 150

def tela_menu():

# Loop principal do jogo
    rodando = True
    while rodando:
        # Verificar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                # Fechar a janela se o botão de fechar for clicado
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                botao_largura = 150
                botao_altura = 75
                botao_pos_x = largura - botao_largura - 2
                botao_pos_y = altura - botao_altura - 2
                if botao_pos_x <= evento.pos[0] <= botao_pos_x + botao_largura and botao_pos_y <= evento.pos[1] <= botao_pos_y + botao_altura:
                    # Clicou no botão, fechar o programa
                    rodando = False


        # Preencher a janela com a cor de fundo
        janela.fill(cor_fundo)

        botao_sair()
        label_titulo()
        #logo_utad()
        #imagem_semaforo()
        botao_começar()
        botao_carregar()
        botao_descricao_regras()
        label_nome_diogo()
        label_nome_ines()
        label_nome_miguel()
        label_nome_cadeira()
        #imagem_simbolos()

    # Atualizar a janela
        pygame.display.update()




tela_menu()




