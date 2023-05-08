import random as rd
rd.seed()

#Menu
def menu():


    print("Bem-vido ao jogo do semáforo!!!!")
    print("Jogar uma partida (1)")
    print("Carregar uma partida apartir de um ficheiro (2)")
    print("Apresentar uma descrição do jogo (3)")
    print("Sair da aplicação (4)")
    
    menu = int(input(""))
    
    if menu == 1:
        jogar()
    
def jogar():
    print("Jogar 1v1 (1)")
    print("Jogar contra um bot (2)")    
    
    jogar1 = int(input(""))
    
    if jogar1 == 1:
        nome1 = input("Insira o nome do jogador 1: ")
        nome2 = input("Insira o nome do jogador 2: ")
        
        primeiro = rd.randint(1,2)
        
        if primeiro == 1:
            print("O primeiro jogador é o " + nome1)
            print("O segundo jogador é o " + nome2)
        else:
            print("O primeiro jogador é o " + nome2)
            print("O segundo jogador é o " + nome1)
            jogo()
        
    elif jogar1 == 2:
        nome1 = input("Insira o nome do jogador: ")
        
        primeiro = rd.randint(1,2)
        
        if primeiro == 1:
            print("O primeiro jogador é o " + nome1)
            print("O segundo jogador é o BOT\n")
            print("\n")
        else:
            print("O primeiro jogador é o BOT")
            print(f"O segundo jogador é o {nome1}")    
            print("\n")    
    else: 
        print("Escolha o numero 1 ou 2.\n")
        jogar()
        
def jogo():
    matriz = [["","","",""], ["","","",""], ["","","",""]]
    
    print("\n")    
    print("0:\t" + " | " + matriz[0][0] + " | " + matriz[0][1] + " | " + matriz[0][2] + " | " + matriz[0][3])
    print("----------------")
    print("1:\t" + " | "+ matriz[1][0] + " | " + matriz[1][1] + " | " + matriz[1][2] + " | " + matriz[1][3])
    print("----------------")
    print("2:\t" + " | " + matriz[2][0] + " | " + matriz[2][1] + " | " + matriz[2][2] + " | " + matriz[2][3])
    

menu()

