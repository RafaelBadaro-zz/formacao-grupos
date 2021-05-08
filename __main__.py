import populacao

dados = populacao.pegarDados()
populacaoInicial = populacao.iniciarPopulacao(dados.pessoas, dados.atividades[0], 10, 5)
for individuo in populacaoInicial:
    print(str(individuo))
