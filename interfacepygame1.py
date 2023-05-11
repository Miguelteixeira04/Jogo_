import pygame

#compor a espessura das linhas pretas qd se clica no botao!!!!


# dimensao do ecra
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# titulo da janela
pygame.display.set_caption("Jogo do Semáforo")

num_linhas = 3
num_colunas = 4

# dimensao dos quadrados
cell_width = screen_width // num_colunas
cell_height = screen_height // num_linhas
cell = (cell_width, cell_height)

# cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
COR_ECRA = (238, 232, 232)

# criando a matriz que representa os botões
botoes = []
for l in range(num_linhas):
    botoes.append([0] * num_colunas) #nao percebi esta parte!!!!

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONUP:
            # verificar se o clique ocorreu dentro de um botão vazio
            posicao = pygame.mouse.get_pos() # retorna a posição atual do cursor do mouse na tela
            c = posicao[0] // cell_width
            l = posicao[1] // cell_height
            if botoes[l][c] == 0:
                botoes[l][c] = 1

        #fazer um coiso para nao deixar por os amarelos e vermelhos no vazio!!!!

    #cor da tela
    screen.fill(COR_ECRA)

    # desenhar os botões
    for l in range(num_linhas):
        pygame.draw.line(screen, BLACK, (0, l * cell_height - 1), (screen_width, l * cell_height - 1)) # desenha linha preta na horizontal
        for c in range(num_colunas):
            cell = pygame.Rect(c * cell_width, l * cell_height, cell_width, cell_height)
            pygame.draw.line(screen, BLACK, (c * cell_width - 1, 0), (c * cell_width - 1, screen_height)) # desenha linha preta na vertical

            if botoes[l][c] == 1:
                pygame.draw.circle(screen, GREEN, cell.center, cell_width // 3)
            else:
                pygame.draw.rect(screen, BLACK, cell, 1)

    pygame.display.update()

pygame.quit()
