import random


def gera():
    return random.randint(1, 100)


def chutarnumero():
    res = gera()
    tentativa = 0
    print("\nPalpite gerado!")

    palpite = 0

    while palpite is not res:
        tentativa += 1
        palpite = int(input("\nQual seu palpite (de 1 a 100): "))
        if palpite > res:
            print("\nErrou! É um valor menor que ", palpite)
        elif palpite < res:
            print("\nErrou! É um valor maior que ", palpite)
        else:
            print("\nParabéns! O número gerado foi ", res,
                  "Acertou em ", tentativa, " tentativas!")


while True:
    chutarnumero()
