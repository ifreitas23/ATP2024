#aluno = (nome, id, [notaTPC, notaProj, notaTeste])
#Turma = [aluno]

def criarTurma(turma):
    num = int(input("introduz o número de alunos que constituí a turma:"))
    while num > 0:
        nome = input("introduz o nome do aluno:")
        id = input("introduz o id do aluno:")
        notaTPC = float(input("introduz a nota do TPC:"))
        notaProj = float(input("introduz a nota do Projeto:"))
        notaTeste = float(input("introduz a nota do Teste:"))
        novo_aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        if novo_aluno not in turma:
            turma.append(novo_aluno)
            print("Aluno registado com sucesso.")
        else:
            print("O aluno registado já existe.")
            num = num + 1
        num = num - 1

def inserirAluno(turma, aluno):  
    if aluno not in turma:
        turma.append(aluno)
    else:
        print("Esse aluno já existe")

def listarTurma(turma):
    print("Nome                     ID          notaTPC         notaProj        notaTeste")
    print("------------------------------------------------------------------------------")
    for aluno in turma:
        print(f"{aluno[0]}          {aluno[1]}           {aluno[2][0]}             {aluno[2][1]}              {aluno[2][2]}")
        print("------------------------------------------------------------------------------")

def consultarId(turma,id):
    id = input("introduza o id do aluno:")
    i = 0
    while i < len(turma):
        if turma[i][1] == id:
            print(turma[i])
        i = i + 1

def guardarFicheiro(turma):
    ficheiro = open("turmabiomed.txt", "w")
    for aluno in turma:
        linha = f"{aluno[0]}::{aluno[1]}::{aluno[2][0]}::{aluno[2][1]}::{aluno[2][2]}\n"
        ficheiro.write(linha)
    ficheiro.close()
    print("Ficheiro guardado em turmabiomed.txt")

def carregarTurma(fnome):
    res = []
    ficheiro = open(fnome)
    for linha in ficheiro:
        if linha != "":
            campos = linha.split("::")
            notas = (float(campos[2]), float(campos[3]), float(campos[4]))
            res.append((campos[0], campos[1], notas))
    ficheiro.close()
    return print(res)

def menu():
    print("""Menu:
          1) Criar turma
          2) Inserir aluno na turma
          3) Listar turma
          4) Consultar aluno por id
          5) Guardar a turma em ficheiro
          6) Carregar uma turma dum ficheiro
          0) Sair""")


turma = []
menu()
opção = int(input("introduz a opção pretendida"))
while opção != 0:
    if opção == 1:
        criarTurma(turma)
    elif opção == 2:
        nome = input("introduz o nome do aluno:")
        id = input("introduz o id do aluno:")
        notaTPC = float(input("introduz a nota do TPC:"))
        notaProj = float(input("introduz a nota do Projeto:"))
        notaTeste = float(input("introduz a nota do Teste:"))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        inserirAluno(turma, aluno)
    elif opção == 3:
        if turma == []:
            print("A turma não existe")
        else:
            listarTurma(turma)
    elif opção == 4:
        if turma == []:
            print("A turma não existe")
        else:
            consultarId(turma,id)
    elif opção == 5:
        if turma == []:
            print("A turma não existe")
        else:
            guardarFicheiro(turma)
    elif opção == 6:
        carregarTurma("turmabiomed.txt")
    else:
        print("Opção inválida!")
    menu()
    opção = int(input("introduz a opção pretendida"))
print("Obrigada, volte sempre!")