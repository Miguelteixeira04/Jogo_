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

    print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")                                        
    print("┃\tBem-vindo ao jogo matemático do semáforo    ┃                                ┃Trabalho realizado por:          ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                ┃   Diogo Cabral         al78834  ┃")
    print("Jogar uma partida (1)                                                                ┃   Maria Inês Cardoso   al78222  ┃")
    print("Carregar uma partida apartir de um ficheiro (2)                                      ┃   Miguel Teixeira      al78321  ┃")
    print("Apresentar uma descrição do jogo / Regras (3)                                        ┃                                 ┃")
    print("Sair da aplicação (4)                                                                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")


    menu = int(input(""))
    
    if menu == 1:
        jogar()
    if menu == 2:
        guardado()
    if menu == 3:
        regras()
    if menu == 4:
        return
    
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
            jogo(primeiro, segundo, jogar1, nome1, nome2)
        else:
            print("\nO primeiro jogador é o " + nome2)
            print("O segundo jogador é o " + nome1)
            primeiro = nome2
            segundo = nome1
            jogo(primeiro, segundo, jogar1, nome1, nome2)
     
        
   # elif jogar1 == 2:
    #    nome1 = input("Insira o nome do jogador: ")
        
     #   primeiro = rd.randint(1,2)
        
      #  if primeiro == 1:
       #     nome2 = "Igor Dinho"
        #    print("\nO primeiro jogador é o " + nome1)
         #   print(f"O segundo jogador é o {nome2}\n")
          #  print("\n")
           # primeiro = nome1
    #        jogada_bot(primeiro, segundo, jogar1, nome1, nome2)
     #   else:
      #      nome1 = "Eva Gabunda"
       #     print(f"\nO primeiro jogador é o {nome1}")
        #    print(f"O segundo jogador é o {nome2}")    
         #   print("\n")   
          #  primeiro = nome1
     #       segundo = nome2
      #      jogada_bot(primeiro, segundo, jogar1, nome1, nome2) 
    else: 
        print("Escolha o numero 1 ou 2.\n")
        jogar()

def guardado():
    print("Ola")
def voltar() : 
    opcao = input("Pressione '2' para voltar atrás ou '3' para voltar ao menu :  ")
    print("\n")
    if opcao == '2':
     regras()
    if opcao == '3':
        menu()
    else:
        print("Insira um número válido!")
def regras():
    escolha = int(input("Apresentar uma descrição do jogo (1) \t Regras do jogo (2) :  "))
    if escolha == 1 :
        print("\n")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃            Descrição do jogo           ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
        print("* Autor: Alan Parr \n")
        print("* Material: 8 peças verdes, 8 amarelas e 8 vermelhas partilhadas pelos jogadores.\n")
        print("* Objetivo: Ser o primeiro a conseguir uma linha de três peças da mesma cor na horizontal, vertical ou diagonal.\n")
        voltar()
    else:
        print("\n")
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃              Regras do jogo            ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
        print("* O jogo realiza-se no seguinte tabuleiro, inicialmente vazio. Em cada jogada, cada jogador realiza uma das seguintes ações.\n")
        print("* Coloca uma peça verde num quadrado vazio;\n")
        print("* Substitui uma peça verde por uma peça amarela\n")
        print("* Substitui uma peça amarela por uma peça vermelha\n")
        print("* De notar que as peças vermelhas não podem ser substituídas. Isto significa que o jogo tem de terminar sempre: à medida que o tabuleiro fica com peças vermelhas, é inevitável que surja uma linha de três peças.\n")
        voltar()

        
def imprimir_matriz():

    print("\n") 
    print("\t    A     B     C     D")   
    print("\t  _______________________")
    print("0:\t" + " |  " + str(matriz[0][0]) + "  |  " + str(matriz[0][1]) + "  |  " + str(matriz[0][2]) + "  |  " + str(matriz[0][3]) + "  |  " )
    print("\t |-----|-----|-----|-----|")
    print("1:\t" + " |  "+ str(matriz[1][0]) + "  |  " + str(matriz[1][1]) + "  |  " + str(matriz[1][2]) + "  |  " + str(matriz[1][3]) + "  |  " )
    print("\t |-----|-----|-----|-----|")
    print("2:\t" + " |__" + str(matriz[2][0]) + "__|__" + str(matriz[2][1]) + "__|__" + str(matriz[2][2]) + "__|__" + str(matriz[2][3]) + "__|" )
    

def jogo(primeiro, segundo, jogar1, nome1, nome2):
    
    jogador_atual = primeiro
    vitoria = False
    res = 0
    res2 = 0

    if jogar1 == 1:
       
        while True:
         imprimir_matriz()
         jogador_atual, vitoria = colocar(primeiro, segundo, jogador_atual)
         if vitoria == True:
             break
        
  #  elif jogar1 == 2:
       # while True:
        #    imprimir_matriz()
         #   jogador_atual, vitoria = jogada_bot(primeiro,segundo,jogador_atual)
          #  if vitoria == True:
           #     break
            
    print("\nDeseja voltar a jogar?")
    print("[1] Sim      [2] Não")
    res = int(input(""))
    if res == 1:
        res = jogar1
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                matriz[i][j] = ' '
                
        primeiro = rd.randint(1,2)
        
        if primeiro == 1:
            print("\nO primeiro jogador é o " + nome1)
            print("O segundo jogador é o " + nome2)
            primeiro = nome1
            segundo = nome2
            jogo(primeiro, segundo, jogar1, nome1, nome2)
        else:
            print("\nO primeiro jogador é o " + nome2)
            print("O segundo jogador é o " + nome1)
            primeiro = nome2
            segundo = nome1
            jogo(primeiro, segundo, jogar1, nome1, nome2)
    else:
        print("\nDeseja voltar ao menu?")
        print("[1] Sim      [2] Não")
        res2 = int(input(""))
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                matriz[i][j] = ' '
        if res2 == 1:
            menu()
        else: 
            return
   
def colocar(primeiro, segundo, jogador_atual):
    
    l = int(input("\nLinha: "))
    c = int(input("Coluna: "))
    
    if l < 0 or l > 2 or c < 0 or c > 3:
        print("Posição inválida.")
        colocar(primeiro, segundo, jogador_atual)

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
        colocar(primeiro, segundo, jogador_atual)
    elif cor == "Y" and (matriz[l][c] == "R" or matriz[l][c] == " "):
        print("\nNão pode colocar a cor amarela nesta posição, tente novamente.") 
        colocar(primeiro, segundo, jogador_atual)
    elif cor == "R" and (matriz[l][c] == "G" or matriz[l][c] == " "):
        print("\nNão pode colocar a cor vermelho nesta posição, tente novamente")
        colocar(primeiro, segundo, jogador_atual)    
    else:
        print("Posição já preenchida.")
        colocar(primeiro, segundo, jogador_atual)    
    if cor == "Y" and matriz[l][c] == "G":
        matriz[l][c] = cor   
        colocar(primeiro, segundo, jogador_atual) 
        
    vitoria, cor = verificar_vitoria(jogador_atual)
    if vitoria:
        print(f"\nO jogador {cor} venceu!")
        imprimir_matriz()
    elif jogador_atual == primeiro:
        print(f"\nÉ a vez do(a) {segundo}")
        jogador_atual = segundo
    elif jogador_atual == segundo:
        print(f"\nÉ a vez do(a) {primeiro}")
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

#def jogada_bot(primeiro, segundo, jogador_atual):
    
   # if primeiro == "BOT":
    #    l = rd.randint(0, 2)
     #   c = rd.randint(0, 3)
        
      #  cor = ['G', 'Y', 'R']
        
       # for i in range(3):
        #    if matriz[l][c] == " ":
         #       if cor[i] == "G" and matriz[l][c] == " ":
          #          return l, c, cor[i]
           #     elif cor[i] == "Y" and matriz[l][c] == "G" :
            #        return l, c, cor[i]
             #   elif cor[i] == "R" and matriz[l][c] == "Y":
              #      return l, c, cor[i]
                
      #  jogador_atual = segundo
        
   # else:
    #    l = int(input("\nLinha: "))
     #   c = int(input("Coluna: "))
    
      #  if l < 0 or l > 2 or c < 0 or c > 3:
       #     print("Posição inválida.")
        #    if cor == "G" and matriz[l][c] == " ":
         #       matriz[l][c] = cor
          #  elif cor == "Y" and matriz[l][c] == "G":
          #      matriz[l][c] = cor  
          #  elif cor == "R" and matriz[l][c] == "Y":
       #         matriz[l][c] = cor
        #    elif cor == "G" and (matriz[l][c] == "Y" or matriz[l][c] == "R"):
         #       print("\nNão pode colocar a cor verde nesta posição, tente novamente.")
          #      jogada_bot(primeiro, segundo, jogador_atual)
      #      elif cor == "Y" and (matriz[l][c] == "R" or matriz[l][c] == " "):
       #         print("\nNão pode colocar a cor amarela nesta posição, tente novamente.") 
        #        jogada_bot(primeiro, segundo, jogador_atual)
         #   elif cor == "R" and (matriz[l][c] == "G" or matriz[l][c] == " "):
          #      print("\nNão pode colocar a cor vermelho nesta posição, tente novamente")
      #          jogada_bot(primeiro, segundo, jogador_atual)    
       #     else:
        #        print("Posição já preenchida.")
         #       jogada_bot(primeiro, segundo, jogador_atual)
          #  if cor == "Y" and matriz[l][c] == "G":
       #         matriz[l][c] = cor   
        #        jogada_bot(primeiro, segundo, jogador_atual) 
                
    #    jogador_atual = primeiro
    
  #  vitoria, cor = verificar_vitoria(jogador_atual)
   # if vitoria:
    #    print(f"\nO jogador {cor} venceu!")
     #   imprimir_matriz()
  #  elif jogador_atual == primeiro:
   #     print(f"\nÉ a vez do(a) {segundo}")
    #    jogador_atual = segundo
 #   elif jogador_atual == segundo:
  #       print(f"\nÉ a vez do(a) {primeiro}")
   #      jogador_atual = primeiro
    
   # return jogador_atual, vitoria      

menu()