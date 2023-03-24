import random 

tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]
p1 = "X"
p2 = "O"

def imprimirTabuleiro():
    print ("-------------Tabuleiro-------------")
    indices = [0,1,2]
    print ("\t\t0\t1\t2")
    for i in indices:
        print("\t",i,"\t", end="")
        for j in indices:
            print (tabuleiro[i][j],"\t",end="")
        print()

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
                x = 1
                return x
            else: 
                print("Você Perdeu!")
                x = 2
                return x
      
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != 0 :
            if tabuleiro[0][coluna] == "X":
                print("Você Venceu!")
                x = 1
                return x
            else: 
                print("Você Perdeu!")
                x = 2
                return x
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != 0 :
        if tabuleiro [0][0] == "X":
            print("Você Venceu!")
            x = 1
            return x
        else: 
            print("Você Perdeu!")
            x = 2
            return x
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != 0 :
        if tabuleiro[0][2] == "X":
            print("Você Venceu!")
            x = 1
            return x
        else: 
            print("Você Perdeu!")
            x = 2
            return x
    
    ocorrencias = 0
    for lista in tabuleiro:
        ocorrencias += lista.count(0)
    if ocorrencias == 0:
        print("Empate!")
        x = 3
        return x

def jogar():
    while True:
        try:
            imprimirTabuleiro()
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
        
        x = verificarVencedor(tabuleiro)
        if x == 1 or x == 2 or x == 3:
            return x
        

def main():
    resultados = open("resultados.txt","a+")
    print(" \n \n ---J O G O   D A   V E L H A--- ")
    print("1 - Jogar")
    print("2 - Resultados")
    print("3 - Sair")

    opcao = int(input())
    if opcao == 1:
        x = jogar()
        if x == 1:
            nome = input("Insira seu nome para registrar na lista de vencedores  ")
            resultados.write(nome)
            resultados.write("\n")
        if x == 2:
            resultados.write("CPU vencedora \n")
        if x == 3:
            resultados.write("Empate \n")
    if opcao == 2:
        resultados.seek(0)
        resultado = resultados.read()
        print(resultado)
    if opcao == 3:
        exit()

main()
    