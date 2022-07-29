import advinhacao
import forca
def escolhe_jogo():
    print("*******************************")
    print("********Escolha um jogo********")
    print("*******************************")

    print("(1) jogo de advinhação (2) jogo da forca")
    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando advinhação")
        advinhacao.jogar()
    elif jogo == 2:
        print("Jogando forca")
        forca.jogar()
        
if (__name__ == "__main__"):
    escolhe_jogo()