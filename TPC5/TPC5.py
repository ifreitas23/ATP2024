def criarSala(cinema1):
    nlugares = int(input("introduza o número de lugares da sala:"))
    filme = input("introduza o nome do filme:")
    vendidos = []
    novasala =(nlugares, vendidos, filme)
    for sala in cinema1:
        if novasala == sala:
            print("Sala já existe")
    if novasala not in cinema1:
        cinema1.append(novasala)
        print("Sala criada com sucesso")

def inserirSala(cinema1, sala):
    res = cinema1
    res.append(sala)
    return cinema1

from datetime import date

def listar(cinema1):
    print("Lugares               Filme  ")
    print("-----------------------------")
    for sala in cinema1:
        print(f"  {sala[0]}               {sala[2]} ")
    today = date.today()
    print("-----------------------------")
    print(today)

def listarDisponibilidade(cinema1):
    print("Filme         Nº lugares disponíveis")
    print("------------------------------------")
    for sala in cinema1:
        print(f"{sala[2]}               {sala[0]-len(sala[1])}")
    today = date.today()
    print("------------------------------------")
    print(today)

def disponivel(cinema1, filme, lugar):
    for sala in cinema1:
        if filme == sala[2]:
            if lugar in sala[1]:
                return print(False)
            else:
                return print(True)
    else:
        print("Esse filme não se encontra dísponivel")
            
def venderBilhete(cinema1, filme, lugar):
    for sala in cinema1:
        if filme == sala[2]:
            if lugar not in sala[1]:
                sala[1].append(lugar)
                print(f"O bilhete com lugar {lugar} está vendido")
            else:
                print("Lugar indisponível")
    else:
        print("Esse filme não se encontra dísponivel")

def menu():
    print("""
          Menu: 
          1) Criar Sala
          2) Listar Cinema
          3) Listar Disponibilidade
          4) Verificar Disponibilidade
          5) Vender Bilhete
          0) Sair  """)  


sala1 = (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = []
cinema1 = inserirSala(cinema1,sala1)
cinema1 = inserirSala(cinema1,sala2)

menu()
opção = int(input("introduz a opção pretendida"))
while opção != 0:
    if opção == 1:
        criarSala(cinema1)
    elif opção == 2:
        listar(cinema1)
    elif opção == 3:
        if cinema1 == []:
            print("O cinema não apresenta filmes em exibição")
        else:
            listarDisponibilidade(cinema1)
    elif opção == 4:
        if cinema1 == []:
            print("O cinema não apresenta filmes em exibição")
        else:
            filme = input("introduz o filme que pretendes ver:")
            lugar = input("introduz o lugar que pretendes:")
            disponivel(cinema1, filme, lugar)
    elif opção == 5:
        if cinema1 == []:
            print("O cinema não apresenta filmes em exibição")
        else:
            filme = input("introduz o filme que pretendes ver:")
            lugar = input("introduz o lugar que pretendes:")
            venderBilhete(cinema1, filme, lugar)
    elif opção not in [0,1,2,3,4,5]:
        print('Opção inválida')
    menu()
    opção = int(input("introduz a opção pretendida"))
print("Obrigada, volte sempre!")