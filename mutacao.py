
from random import randint

from modelos import *


def cruzar(c1, c2, atividade, tam_cromossomo):

    mascara = gerar_mascara(tam_cromossomo)
    pessoas_nova_geracao = []

    for i in range(tam_cromossomo):
        if mascara[i] == 0:
            if i < len(c2.pessoas) and c2.pessoas[i] not in pessoas_nova_geracao:
                pessoas_nova_geracao.append(c2.pessoas[i])
        else:
            if i < len(c1.pessoas) and c1.pessoas[i] not in pessoas_nova_geracao:
                pessoas_nova_geracao.append(c1.pessoas[i])

    novo_cromossomo = Cromossomo(pessoas_nova_geracao, atividade)

    return novo_cromossomo

# p1, p2, p3

# 010

# p2, p5, p7

# p2, p2, p3


def gerar_mascara(tam_cromossomo):

    mascara = []

    for i in range(tam_cromossomo):
        mascara.append(randint(0, 1))

    return mascara
