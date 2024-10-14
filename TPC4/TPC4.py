def menu():
    print(""" Menu:
    (1) Criar Lista 
    (2) Ler Lista
    (3) Soma
    (4) Média
    (5) Maior
    (6) Menor
    (7) estaOrdenada por ordem crescente
    (8) estaOrdenada por ordem decrescente
    (9) Procura um elemento
    (0) Sair """)

    return int(input("Selecione a opção pretendida:"))

def criarLista():
    lista = []
    import random
    i = int(input("introduza o número de elementos que pretendes que a lista tenha:"))
    lista = [random.randint(0, 100) for x in range(i)]
    print(lista)
    return lista

def lerLista():
    N = int(input("introduza um número:"))
    lista = []
    i = 0
    while i < N:
        n = int(input("introduza um número:"))
        lista.append(n)
        i = i + 1
    print(lista)
    return lista

def somaLista(lista):
    i = 0
    soma = 0
    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1
    print(f"A soma é {soma}")
    return soma

def mediaLista (lista):
    i = 0
    soma = 0
    while i < len(lista):
        num = lista[i]
        soma = soma + num
        media = soma / len(lista)
        i = i + 1
    print(f"A média é {media}")
    return media 

def maiorLista(lista):
    i = 0
    maior = lista[i]
    for num in lista:
        if num > maior:
            maior = num
    print(f"O maior número é o {maior}")
    return maior

def menorLista(lista):
    i = 0
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    print(f"O menor número é o {menor}")
    return menor

def ordenadacrescenteLista(lista):
    ordenada = True
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            ordenada = False
        i = i + 1
    if ordenada == True:
        print("Sim. A lista está ordenada de forma crescente. ")
    else:
        print("Não. A lista não está ordenada de forma crescente.")

def ordenadadecrescenteLista(lista):
    ordenada = True
    i = 0
    while i < len(lista) - 1:
        if lista[i] < lista[i + 1]:
            ordenada = False
        i = i + 1
    if ordenada == True:
        print("Sim. A lista está ordenada de forma decrescente.")
    else:
        print("Não. A lista não está ordenada de forma decrescente.")

def procuraelemlista(lista):
    elem = int(input("introduzir o elemento que deseja procurar:"))
    i = 0
    if elem in lista:
        while i < len(lista):
            if elem == lista[i]:
                posição = i + 1
                print(f"O elemento {elem} está na posição {posição}")
            i = i + 1
    else:
        print("-1")

        
lista = []
opção = -1
while opção != 0:
    opção = menu()
    if opção == 1:
        lista = criarLista()
    elif opção == 2:
        lista = lerLista()
    elif opção == 3:
        if lista != []:
            somaLista(lista)
        else:
            print("Crie uma lista (selecione opção 1 ou 2)")
    elif opção == 4:
        if lista != []:
            mediaLista (lista)
        else:
            print("Crie uma lista (selecione opção 1 ou 2)")
    elif opção == 5:
        if lista != []:
            maiorLista(lista)
        else:
            print("Crie uma lista (selecione opção 1 ou 2)")
    elif opção == 6:
        if lista != []:
            menorLista(lista)
        else:
            print("Crie uma lista (selecione opção 1 ou 2)")
    elif opção == 7:
        if lista != []:
            ordenadacrescenteLista(lista)
        else:
            print("Crie uma lista (selecione opção 1 ou 2)")
    elif opção == 8:
        if lista != []:
            ordenadadecrescenteLista(lista)
        else:
            print("Crie uma lista (selecione opção 1 ou 2)")
    elif opção == 9:
        if lista != []:
            procuraelemlista(lista)
        else:
            print("Crie uma lista (selecione opção 1 ou 2)")
    else:
        print("Opção inválida")
print("Terminou. Obrigada! Volte sempre!")