import random as rd
rd.seed()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

jogador_atual = " "
matriz = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]

#Menu
def menu():

    print("|---------------------------------------------------|")
    print("|\tBem-vindo ao jogo matemático do semáforo    |")
    print("|---------------------------------------------------|\n")
    print("Jogar uma partida (1)")
    print("Carregar uma partida apartir de um ficheiro (2)")
    print("Apresentar uma descrição do jogo (3)")
    print("Sair da aplicação (4)\n")

    print("                                                                           ---------------------------------")
    print("                                                                          |Trabalho realizado por:          | ")
    print("                                                                          |                                 |")
    print("                                                                          |   Diogo Cabral         al78834  |")
    print("                                                                          |   Maria Inês Cardoso   al78222  |")
    print("                                                                          |   Miguel Teixeira      al78321  |")
    print("                                                                          |                                 | ")
    print("                                                                          |                                 |")
    print("                                                                           ---------------------------------")
    
    menu = int(input(""))
    
    if menu == 1:
        jogar()
    
def jogar():
    print("\nJogar 1v1 (1)")
    print("Jogar contra um bot (2)\n")    
    
    jogar1 = int(input(""))
    
    if jogar1 == 1:
        nome1 = input("\nInsira o nome do jogador 1: ")
        nome2 = input("Insira o nome do jogador 2: ")
        
        primeiro = rd.randint(1,2)
                
        if primeiro == 1:
            print("\nO primeiro jogador é o " + nome1)
            print("O segundo jogador é o " + nome2)
            primeiro = nome1
            segundo = nome2
            jogo(primeiro, segundo, jogar1)
        else:
            print("\nO primeiro jogador é o " + nome2)
            print("O segundo jogador é o " + nome1)
            primeiro = nome2
            segundo = nome1
            jogo(primeiro, segundo, jogar1)
     
        
    elif jogar1 == 2:
        nome1 = input("Insira o nome do jogador: ")
        
        primeiro = rd.randint(1,2)
        
        if primeiro == 1:
            print("\nO primeiro jogador é o " + nome1)
            print("O segundo jogador é o BOT\n")
            print("\n")
            jogo(nome1, "BOT", jogar1)
        else:
            print("\nO primeiro jogador é o BOT")
            print(f"O segundo jogador é o {nome1}")    
            print("\n")   
            jogo("BOT", nome1, jogar1) 
    else: 
        print("Escolha o numero 1 ou 2.\n")
        jogar()

        
def imprimir_matriz():

    print("\n") 
    print("\t   A    B    C    D")   
    print("\t  _______________________")
    print("0:\t" + " |  " + str(matriz[0][0]) + "  |  " + str(matriz[0][1]) + "  |  " + str(matriz[0][2]) + "  |  " + str(matriz[0][3]) + "  |  " )
    print("\t |-----|-----|-----|-----|")
    print("1:\t" + " |  "+ str(matriz[1][0]) + "  |  " + str(matriz[1][1]) + "  |  " + str(matriz[1][2]) + "  |  " + str(matriz[1][3]) + "  |  " )
    print("\t |-----|-----|-----|-----|")
    print("2:\t" + " |__" + str(matriz[2][0]) + "__|__" + str(matriz[2][1]) + "__|__" + str(matriz[2][2]) + "__|__" + str(matriz[2][3]) + "__|" )
    

def jogo(primeiro, segundo, jogar1):
    
    jogador_atual = primeiro
    vitoria = False

    if jogar1 == 1:
       
        while True:
         imprimir_matriz()
         jogador_atual, vitoria = colocar(primeiro, segundo, jogador_atual)
         if vitoria == True:
             break
          
    elif jogar1 == 2:
        while True:
            imprimir_matriz()
            jogada_bot()
            
            
        
   
   
def colocar(primeiro, segundo, jogador_atual):
    
    l = int(input("\nLinha: "))
    c = int(input("Coluna: "))
    
    if l < 0 or l > 2 or c < 0 or c > 3:
        print("Posição inválida.")
        colocar(primeiro, segundo, jogador_atual)
        return

    print("\nGreen [G]\nYellow [Y]\nRed [R]")
    cor = input("").upper()
    
    if cor == "G" and matriz[l][c] == " ":
        matriz[l][c] = cor
    elif cor == "Y" and matriz[l][c] == "G":
        matriz[l][c] = cor  
    elif cor == "R" and matriz[l][c] == "Y":
        matriz[l][c] = cor
    elif cor == "G" and (matriz[l][c] == "Y" or matriz[l][c] == "R"):
        print("\nNão pode colocar a cor verde nesta posição, tente novamente.")  
    elif cor == "Y" and (matriz[l][c] == "R" or matriz[l][c] == " "):
        print("\nNão pode colocar a cor amarela nesta posição, tente novamente.") 
    elif cor == "R" and (matriz[l][c] == "G" or matriz[l][c] == " "):
        print("\nNão pode colocar a cor vermelho nesta posição, tente novamente")    
    else:
        print("Posição já preenchida.")
        
    if cor == "Y" and matriz[l][c] == "G":
        matriz[l][c] = cor   
        colocar(primeiro, segundo, jogador_atual) 
        
    vitoria, cor = verificar_vitoria(jogador_atual)
    if vitoria:
        print(f"\nO jogador {cor} venceu!")
    elif jogador_atual == primeiro:
        print(f"\nTurno do(a) {segundo}")
        jogador_atual = segundo
    elif jogador_atual == segundo:
        print(f"\nTurno do(a) {primeiro}")
        jogador_atual = primeiro
    
    return jogador_atual, vitoria
        
    
        
        
        
def verificar_vitoria(jogador_atual):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != ' ':
            return True, jogador_atual

    for j in range(3):
        if matriz[0][j] == matriz[1][j] == matriz[2][j] != ' ':
            return True, jogador_atual

    if matriz[0][0] == matriz[1][1] == matriz[2][2] != ' ':
        return True, jogador_atual
    
    if matriz[0][1] == matriz[1][2] == matriz[2][3] != ' ':
        return True, jogador_atual
    
    if matriz[0][3] == matriz[1][2] == matriz[2][1] != ' ':
        return True, jogador_atual
    
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != ' ':
        return True, jogador_atual

    if matriz[0][2] == matriz[1][1] == matriz[2][0] != ' ':
        return True, jogador_atual

    return False, None

def jogada_bot():
    while True:
        l = rd.randint(0, 2)
        c = rd.randint(0, 3)
        
        cor = ['G', 'Y', 'R']
        
        for i in range(3):
            if matriz[l][c] == " ":
                if cor[i] == "G" and matriz[l][c] == " ":
                    return l, c, cor[i]
                elif cor[i] == "Y" and matriz[l][c] == "G":
                    return l, c, cor[i]
                elif cor[i] == "R" and matriz[l][c] == "Y":
                    return l, c, cor[i]
        continue

menu()
