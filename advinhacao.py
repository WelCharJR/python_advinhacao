import random

def jogar():
    
    print("*******************************")
    print("Bem vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    
    print("(1) Facil (2) Medio (3) Dificil")
    nivel = int(input("Escolha o nivel de dificuldade"))
    
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
        
    else: total_de_tentativas = 5
        

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas) )
        
        chute = int(input("Digite um numero de 1 a 100:"))

        print("seu numero foi", chute)
        
        if(chute < 1 or chute > 100):
            print("Coloque um numero de 1 a 100!!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
        perdeu  = rodada == total_de_tentativas
        
        if(acertou):
            print("Você acertou!!!!!! Seus pontos foram {}".format(pontos))
            break
        else:
            if(maior):
                print("você errou o chute foi maior que o numero secreto")
            elif(menor):
                print("você errou o chute foi menor que o numero secreto")
                
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
        if(perdeu):
            print("Você perdeu o numero secreto era {}. E seus pontos foram {}".format(numero_secreto, pontos))
            
    print("fim de jogo")

if(__name__ == "__main__"):
    jogar()