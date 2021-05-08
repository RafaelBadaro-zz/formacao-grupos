
from modelos import *
import numpy as np

from mutacao import *


def preparar_roleta(cromossomos):
    soma_notas_ff = 0

    for cromossomo in cromossomos:
        soma_notas_ff += cromossomo.nota_ff

    # Dicionario que contem o <key: Cromossomo, value: Percentual>
    dicionario = dict()
    # Calcular as porcentagens
    for cromossomo in cromossomos:
        # Tirando o porcentagens com duas casas decimais
        percentual = round(
            (cromossomo.nota_ff * 1)/soma_notas_ff, 2)

        dicionario.update({cromossomo: percentual})

    return dicionario


def recalcular_porcentagem(dicionario):
    soma_notas_ff = 0
    for cromossomo in dicionario:
        soma_notas_ff += cromossomo.nota_ff

    dicionario_recalculado = dict()
    for cromossomo in dicionario:
        percentual = round(
            (cromossomo.nota_ff * 1)/soma_notas_ff, 2)

        dicionario_recalculado.update({cromossomo: percentual})

    return dicionario_recalculado


def sortear_pai(dicionario):
    cromossomos = []
    porcentagens = []
    # Separar em duas listas os cromossomos e as porcentagens de sorteio de cada um
    for i in dicionario:
        cromossomos.append(i)
        porcentagens.append(dicionario[i])

    # A soma das porcentagens tem que sempre ser igual a 1
    # Podem existir mais casos, mas os que detectei são 2, a porcentagem fica 0,01 acima ou abaixo: 1.01 ou 0.99

    # Garante que para número iguais apenas um será alterado
    ocorreu_reajuste = False
    if round(sum(porcentagens), 2) == 1.01:
        # No caso de acima: remover 0,01 no que tem a menor porcentagem
        menor_porcentagem = min(porcentagens)
        for i in range(len(porcentagens)):
            if not ocorreu_reajuste and porcentagens[i] == menor_porcentagem:
                porcentagens[i] = round(porcentagens[i] - 0.01, 2)
                ocorreu_reajuste = True

    elif round(sum(porcentagens), 2) == 0.99:
        # No caso de abaixo, adicionar 0,01 no que tem a maior porcentagem
        maior_porcentagem = max(porcentagens)
        for i in range(len(porcentagens)):
            if not ocorreu_reajuste and porcentagens[i] == maior_porcentagem:
                porcentagens[i] = round(porcentagens[i] + 0.01, 2)
                ocorreu_reajuste = True

    pai_sorteado = np.random.choice(cromossomos, p=porcentagens)
    return pai_sorteado


def gerar_nova_geracao(dicionario, tamPopulacao, atividade, tamCromossomo):
    numero_nova_geracao = 0
    nova_geracao = []
    while(tamPopulacao >= numero_nova_geracao):
        dicionario_copia = dicionario.copy()
        pai1 = sortear_pai(dicionario_copia)
        dicionario_copia.pop(pai1)
        dicionario_recalculado = recalcular_porcentagem(dicionario_copia)
        pai2 = sortear_pai(dicionario_recalculado)
        filho_nova_geracao = cruzar(pai1, pai2, atividade, tam_cromossomo)
        nova_geracao.append(filho_nova_geracao)
        numero_nova_geracao += 1

    return nova_geracao


def rodar_roleta(cromossomos, tamPopulacao, atividade, tamCromossomo):
    gerar_nova_geracao(preparar_roleta(cromossomos, tamPopulacao, atividade, tamCromossomo)
