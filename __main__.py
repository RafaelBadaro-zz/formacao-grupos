import roleta
import populacao
import modelos

# Tarefas

# Parametros de entrada:

# O tamanho de cada cromossomo
# A quantidade de gerações
# Definir o tamanho da populacao maxima, ex: populacao inical = 20, cada geracao tem que ter 20 cromossomos, se deu 40, tem q matar os 20 piores

# 1 . Pop inical -> criar json com os dados e buscar eles - Ravi - feito
# - While geracoes_requisitadas >= geracoes_atuais:
# 2 . aplicar a ff -> Laercio
# 3 . Selecionar quem vai fazer o cruzamento (os pais):  roleta viciada -> Badaró - feito
# 4 . Gerar máscara e aplicar o cruzamento -> Badaró e Ravi
# 5 . Matar população - Ravi - feito
# - EndWhile


def iniciar():
    tamPopulacao = 5
    tamEquipe = 5
    qntGeracoes = 9
    qntGeracoesAtuais = 0

    dados = populacao.pegarDados()
    populacaoInicial = populacao.iniciarPopulacao(
        dados.pessoas, dados.atividades[0], tamPopulacao, tamEquipe)

    atividade = dados.atividades[0]

    print('Atividade em avaliação:', atividade.nome)
    while qntGeracoes >= qntGeracoesAtuais:

        if qntGeracoesAtuais == 0:
            novaGeracao = roleta.rodar_roleta(
                populacaoInicial, tamPopulacao, atividade, tamEquipe)
        else:
            novaGeracao = roleta.rodar_roleta(
                novaGeracao, tamPopulacao, atividade, tamEquipe)

        novaGeracao = populacao.thanos(novaGeracao, tamPopulacao)
        qntGeracoesAtuais += 1

        print('-----------------')
        print('Geração:', qntGeracoesAtuais)
        for i in range(len(novaGeracao)):
            print('Equipe:', str(i), '-> Nota:', novaGeracao[i])

    print('------------------------------------------------------')
    print('Melhor equipe -> Nota:', novaGeracao[0].nota_ff)
    print('Pessoas dentro da equipe:')
    for i in novaGeracao[0].pessoas:
        print('Pessoa:', i.id)


iniciar()
