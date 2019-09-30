def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()

    letras_acertadas = ["_" for l in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        index = 0
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (letra == chute):
                    letras_acertadas[index] = letra

                index = index + 1

            print(letras_acertadas)
            print("Jogando...")
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if (enforcou):
        print("Você perdeu!!")
    elif (acertou):
        print("Você ganhou!!")
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()