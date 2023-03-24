import random 

tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]
p1 = "X"
p2 = "O"

def imprimirTabuleiro():
    for linha in tabuleiro:
        for elemento in linha:
            print (elemento, end = " ")
        print()

imprimirTabuleiro()

def jogarMaquina():
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = p2
            imprimirTabuleiro()
            break

        ocorrencias = 0
        for lista in tabuleiro:
            ocorrencias += lista.count(0)
        if ocorrencias == 0:
            break

def verificarVencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != 0 :
            if linha[0] == "X":
                print("Você Venceu!")
                imprimirTabuleiro()
            else: 
                print("Você Perdeu!")
                imprimirTabuleiro()
            return exit()
        
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != 0 :
            if tabuleiro[0][coluna] == "X":
                print("Você Venceu!")
                imprimirTabuleiro()
            else: 
                print("Você Perdeu!")
                imprimirTabuleiro()
            return exit()
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != 0 :
        if tabuleiro [0][0] == "X":
            print("Você Venceu!")
            imprimirTabuleiro()
        else: 
            print("Você Perdeu!")
            imprimirTabuleiro()
        return exit()
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != 0 :
        if tabuleiro[0][2] == "X":
            print("Você Venceu!")
            imprimirTabuleiro()
        else: 
            print("Você Perdeu!")
            imprimirTabuleiro()
        return exit()
    
    ocorrencias = 0
    for lista in tabuleiro:
        ocorrencias += lista.count(0)
    if ocorrencias == 0:
        print("Empate!")
        imprimirTabuleiro()
        return exit()

def jogar():
    while True:
        try:
            linha = int(input("Digite a linha: "))
            if linha < 0 or linha > 2:
                print ("Linha inválida")
                continue
            coluna = int(input("Digite a coluna: "))
            if coluna < 0 or coluna > 2:
                print ("Coluna inválida")
                continue
            if tabuleiro[linha][coluna] != 0:
                print ("Jogada inválida, por favor escolha uma casa não ocupada")
                continue
            else:
                tabuleiro[linha][coluna] = p1

        except:
            print ("Jogada inválida, por favor escolha uma casa não ocupada")
        
        jogarMaquina()
        
        verificarVencedor(tabuleiro)

jogar()