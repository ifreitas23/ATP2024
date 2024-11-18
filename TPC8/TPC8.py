#tpc1 - Listas em compreensão

# a) Lista formada pelos elementos que não são comuns às duas listas:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = [n for n in lista1 + lista2 if (n in lista1) != (n in lista2)]
print(ncomuns)

#b) Lista formada pelas palavras do texto compostas por mais de 3 letras:
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = [pal for pal in texto.split(" ") if len(pal)>3]
print(lista)

#c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(i+1, x) for i, x in enumerate(lista)]
print(listaRes)

#tpc2

#a) Especifique uma função que dada uma string e uma substring não vazia, 
# calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings:
def strCount(s, subs):
    pal = s.split(subs)
    return len(pal)-1


#b) Especifique uma função que recebe uma lista de números inteiros positivos e devolve o menor produto
#  que for possível calcular multiplicando os 3 menores inteiros da lista:
def produtoM3(lista):
    trocas = True
    while trocas:
        trocas = False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                trocas = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
    prod = lista[0] * lista[1] * lista[2]
    return prod

#c) Especifique uma função que dado um número inteiro positivo, 
# repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado:
def reduxInt(n):
    while n >= 10:
        soma = 0
        for i in str(n):
            soma = soma + int(i)
        n = soma
    return n

#d)Especifique uma função que recebe duas strings, `string1` e `string2`, e devolve o índice 
# da primeira ocorrência de `string2` em `string1`, caso não ocorra nenhuma vez a função deverá retornar `-1`:
def myIndexOf(s1, s2):
    f = s1.split(" ")
    if s2 in f:
        i = 0
        for caracter in s1:
            if caracter == s2[0]:
                print(i)
            i = i + 1
    else:
        print(-1)
    return

#tpc3 - A rede social

#a) `quantosPost`, que indica quantos posts estão registados:
def quantosPost(redeSocial):
    return len(redeSocial)

#b) `postsAutor`, que devolve a lista de posts de um determinado autor:
def postsAutor(redeSocial, autor):
    res = []
    for post in redeSocial:
        if post["autor"] == autor:
            res.append(post)
    return res

#c) `autores`, que devolve a lista de autores de posts ordenada alfabeticamente:
def autores(redeSocial):
    res = []
    for post in redeSocial:
        res.append(post["autor"])
    res.sort()
    return res

#d) `insPost`, que acrescenta um novo post à rede social a partir dos parâmetros recebidos
#  e devolve a nova rede social. 
def insPost(redeSocial,conteudo, autor, dataCriacao, comentarios):
    id = f"p{len(redeSocial)+1}"
    novopost = {"id": id,
                "conteudo": conteudo,
                "autor": autor,
                "dataCriação": dataCriacao,
                "comentarios": comentarios}
    redeSocial.append(novopost)
    return redeSocial

#e) `remPost`, que remove um post da rede, correspondente ao `id` recebido.
def remPost(redeSocial, id):
    for post in redeSocial:
        if post["id"] == id:
            redeSocial.remove(post)
    return redeSocial

#f) `postsPorAutor`, que devolve uma distribuição de posts por autor.
def postsPorAutor(redeSocial):
    distrib = {}
    for post in redeSocial:
        autor = post["autor"]
        if autor in distrib:
            distrib[autor] = distrib[autor] + 1
        else:
            distrib[autor] = 1
    return distrib

#g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.
def comentadoPor(redeSocial, autor):
    res = []
    for post in redeSocial:
        for cometario in post["comentarios"]:
            if cometario["autor"] == autor:
                res.append(post)
    return res