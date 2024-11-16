#TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
#Data = (Int,Int,Int)
#TempMin = Float
#TempMax = Float
#Precipitacao = Float
tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def medias(tabMeteo):
    res = []
    for data, tempMin, tempMax, precipitação in tabMeteo:
        media = (tempMin + tempMax)/2
        res.append((data, media))
    return res
print(medias(tabMeteo1))


def guardartabMeteo(tabMeteo, fnome):
    ficheiro = open(fnome,"w")
    for i in tabMeteo:
        linha = f"{i[0][0]}::{i[0][1]}::{i[0][2]}::{i[1]}::{i[2]}::{i[3]}\n"
        ficheiro.write(linha)
    ficheiro.close()

def carregaTabMeteo(fnome):
    res = []
    ficheiro = open(fnome)
    for linha in ficheiro:
        if linha != "":
            campos = linha.split("::")
            data = (int(campos[0]),int(campos[1]),int(campos[2]))
            res.append((data,float(campos[3]),float(campos[4]),float(campos[5])))
    ficheiro.close()
    return res

def minMin(tabMeteo):
    menor = tabMeteo[0][1]
    for data, tmin, tmax, precep in tabMeteo[1:]:
        if tmin < menor:
            menor = tmin
    return menor

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, precep in tabMeteo:
        amplitude = tmax - tmin
        res.append((data, amplitude))
    return res

def maxChuva(tabMeteo):
    max = tabMeteo[0][3]
    for data, tmin, tmax, precepit in tabMeteo:
        if precepit > max:
            max = precepit
            maxdata = data
    return data, max

def diasChuvosos(tabMeteo, p):
    res = []
    for data,tmin,tmax,precepit in tabMeteo:
        if precepit > p:
            res.append((data,precepit))
    return res

def maxPeriodoCalor(tabMeteo, p):
    consecutivos = 0
    contador = 0
    for data,tmin,tmax,precepit in tabMeteo:
        if precepit < p:
            contador = contador + 1
        else:
            if consecutivos > contador:
                consecutivos = contador 
            contador = 0
    if contador > consecutivos:
        consecutivos = contador
    return consecutivos

import matplotlib.pyplot as plt
def grafTabMeteo(t):
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    for data, tmin, tmax, precipit in t:
        data1 = f"{data[0]}/{data[1]}/{data[2]}"
        x1.append(data1)
        y1.append(tmin)
        y2.append(tmax)
        y3.append(precipit)


    plt.plot(x1, y1, label = "Temp. mínima", marker='o', markerfacecolor='blue', markersize=6)
    plt.plot(x1, y2, label = "Temp. máxima", marker='o', markerfacecolor='orange', markersize=6)
    plt.xlabel('Data')
    plt.ylabel('Temperatura ºC')
    plt.title('Temperatura mínima e máxima')
    plt.legend()
    plt.show()
    

    plt.bar(x1,y3, color = 'skyblue')
    plt.xlabel('Data')
    plt.ylabel('Pluviosidade')
    plt.title('Pluviosidade')
    plt.show()

def menu():
    print("""Menu:
          1) Temperatura Média de cada dia
          2) Guardar Tabela Metereológica num ficheiro
          3) Carregar Tabela Metereológica de um ficheiro
          4) Temperatura Mínima mais Baixa
          5) Amplitude Térmica
          6) Dia com maior precipitação
          7) Dias em que a precipitação foi superior a x
          8) Maior número de dias consecutivos com precipitação a baixo de x
          9) Desenho dos Gráficos (Temp. mínima, Temp. máxima, Pluviosidade)
          0) Sair """)
    
tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
menu()
opção = int(input("introduz a opção pretendida:"))
while opção != 0:
    if opção == 1:
        medias(tabMeteo1)
    elif opção == 2:
        fnome = input("introduza o nome do ficheiro:")
        guardartabMeteo(tabMeteo1, fnome)
    elif opção == 3:
        carregaTabMeteo(fnome)
    elif opção == 4:
        minMin(tabMeteo1)
    elif opção == 5:
        amplTerm(tabMeteo1)
    elif opção == 6:
        maxChuva(tabMeteo1)
    elif opção == 7:
        p = float(input("introduz um limite p:"))
        diasChuvosos(tabMeteo1, p)
    elif opção == 8:
        p = float(input("introduz um limite p:"))
        maxPeriodoCalor(tabMeteo1, p)
    elif opção == 9:
        grafTabMeteo(tabMeteo1)
    else:
        print("Opção inválida!")
    menu()
    opção = int(input("introduz a opção pretendida:"))
print("Obrigada, volte sempre!")