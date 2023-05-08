import random as rd
rd.seed()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

matriz = [["","","",""], ["","","",""], ["","","",""]]

#Menu
def menu():


    print("Bem-vido ao jogo do semáforo!!!!")
    print("Jogar uma partida (1)")
    print("Carregar uma partida apartir de um ficheiro (2)")
    print("Apresentar uma descrição do jogo (3)")
    print("Sair da aplicação (4)\n")
    
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
            jogo()
        else:
            print("\nO primeiro jogador é o " + nome2)
            print("O segundo jogador é o " + nome1)
            jogo()
        
    elif jogar1 == 2:
        nome1 = input("Insira o nome do jogador: ")
        
        primeiro = rd.randint(1,2)
        
        if primeiro == 1:
            print("\nO primeiro jogador é o " + nome1)
            print("O segundo jogador é o BOT\n")
            print("\n")
            jogo()
        else:
            print("\nO primeiro jogador é o BOT")
            print(f"O segundo jogador é o {nome1}")    
            print("\n")   
            jogo() 
    else: 
        print("Escolha o numero 1 ou 2.\n")
        jogar()
        
def imprimir_matriz():
    
    print("\n") 
    print("\t   A    B    C    D")   
    print("\t _____________________")
    print("0:\t" + " |  " + str(matriz[0][0]) + "  |  " + str(matriz[0][1]) + "  |  " + str(matriz[0][2]) + "  |  " + str(matriz[0][3]) + "  |  " )
    print("\t |----|----|----|----|")
    print("1:\t" + " |  "+ str(matriz[1][0]) + "  |  " + str(matriz[1][1]) + "  |  " + str(matriz[1][2]) + "  |  " + str(matriz[1][3]) + "  |  " )
    print("\t |----|----|----|----|")
    print("2:\t" + " |__" + str(matriz[2][0]) + "__|__" + str(matriz[2][1]) + "__|__" + str(matriz[2][2]) + "__|__" + str(matriz[2][3]) + "__|" )
    

def jogo():
    
    imprimir_matriz()    
    colocar()

def colocar():
    l = int(input("\nLinha: "))
    c = int(input("Coluna: "))
    
    print("\nGreen [G]\nYellow [Y]\nRed [R]")
    
    cor = input("").upper()

    if matriz[l][c] == "" or matriz[l][c] == None:
        if cor == "G":
            matriz[l][c] = "G"
        elif cor == "Y":
            matriz[l][c] = "Y"
        else:
            matriz[l][c] = "R"
    else:
        print("Posição já preenchida.")
        colocar()
        
menu()

