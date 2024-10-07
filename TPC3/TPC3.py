def menu():
    print("Pretendes jogar ao jogo dos 21 fósforos? A regras são as seguintes: ")
    print("O jogo inicia com 21 fósforos, cada jogador(computador ou utilizador) alternadamente pode tirar 1,2,3 ou 4 fósforos, perdendo o jogador que tirar o último fósforo.")
    print("1) se pretede ser você a começar")
    print("2) se pretende que seja o computador a começar o jogo")
    print("3) se não pretende jogar agora")

def modo1():
    f = 21 
    while f > 1 :
        x = int(input("introduza o número de fósforos que pretende retirar (1/2/3/4):"))
        while x > 4 or x < 1:
            print("Apenas pode retirar 1, 2, 3 ou 4 fósforos.")
            x = int(input("introduza o número de fósforos que pretende retirar (1/2/3/4):"))
        f = f - x
        computador = 5 - x
        f = f - computador
        print(f"Eu retiro {computador} fósforos, restando {f} fósforos. Quantos pretendes retirar? ")
    print("lamento, mas você perdeu, retirou o último fósforo")

def modo2():
    f = 21
    from random import randint
    while f > 1 :
        n = randint(1,4)
        f = f - n
        print(f"eu retiro {n} fósforos, restando {f} fósforos. Quatos pretendes retirar?")
        x = int(input("introduza o número de fósforos que pretendes retirar (1/2/3/4):"))
        while x > 4 or x < 1:
            print("Apenas pode retirar 1, 2, 3 ou 4 fósforos.")
            x = int(input("introduza o número de fósforos que pretende retirar (1/2/3/4):"))
        f = f - x
        if f == 1:
            print("Você é o vencedor. Parabéns!")
        if n + x < 5:
            n = 5 - (x + n)
            while f > 1:
                f = f - n
                print(f"eu retirei {n} fósforos, restando {f} fósforos. Quantos pretendes retirar?")
                x = int(input("introduza o número de fósforos que pretendes retirar (1/2/3/4):"))
                while x > 4 or x < 1:
                    print("Apenas pode retirar 1, 2, 3 ou 4 fósforos.")
                    x = int(input("introduza o número de fósforos que pretende retirar (1/2/3/4):"))
                f = f - x
                n = 5 - x
            print("lamento, mas você perdeu.")
        elif n + x > 5:
            n = 10 - (x + n) 
            while f > 1:
                f = f - n
                print(f"eu retirei {n} fósforos, restando {f} fósforos. Quantos pretendes retirar?")
                x = int(input("introduza o número de fósforos que pretendes retirar (1/2/3/4):"))
                while x > 4 or x < 1:
                    print("Apenas pode retirar 1, 2, 3 ou 4 fósforos.")
                    x = int(input("introduza o número de fósforos que pretende retirar (1/2/3/4):"))
                f = f - x
                n = 5 - x
            print("lamento, mas você perdeu.")
            
menu()
opção = int(input("seleciona a opção pretendida:"))
while opção != 3:
    if opção == 1:
        modo1()
        print("Pretende jogar novamente?")
        resposta = input("introduza a sua resposta (sim/não):")
        if resposta == "sim":
            menu()
            opção = int(input("seleciona a opção pretendida:"))
        else: 
            print("Obrigada, volte sempre!")
    elif opção == 2:
        modo2()
        print("Pretende jogar novamente?")
        resposta = input("introduza a sua resposta (sim/não):")
        if resposta == "sim":
            menu()
            opção = int(input("seleciona a opção pretendida:"))
        else: 
            print("Obrigada, volte sempre!")
    else:
        print("opção desconhecida")
print("Obrigada, volte sempre!")