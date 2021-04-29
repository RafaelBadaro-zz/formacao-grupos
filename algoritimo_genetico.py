
# Cromossomo
class Equipe:

    # Classe equipe
    # geracao - um número que indica qual a geracao da equipe
    # pessoas - um vetor que indica as pessoas que compoe essa equipe

    def __init__(self, geracao, pessoas):
        self.geracao = geracao
        self.pessoas = pessoas


class Pessoa:
    def __init__(self, habilidades, preferencias):
        self.habilidades = habilidades
        self.preferencias = preferencias


class Habilidade:

    # Classe habilidade
    # nota - um numbero que indica a pontuacao da pessoa na habilidade
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


class Preferencia:

    def __init__(self, nome_atividade, nota):
        self.nome_atividade = nome_atividade
        self.nota = nota


class Atividade:

    # As habilidades requisitadas por atividade
    habilidades_requisitadas = {
        'A1': ['H1', 'H2', 'H3'],
        'A2': ['H1', 'H3', 'H4'],
    }


h1 = Habilidade('H1', 2)
h2 = Habilidade('H2', 4)
h3 = Habilidade('H3', 8)
h4 = Habilidade('H4', 1)

hds = [h1, h2, h3, h4]

p1 = Preferencia('A1', 4)
p2 = Preferencia('A2', 7)

prefs = [p1, p2]

pessoa = Pessoa(hds, prefs)

for x in range(len(pessoa.habilidades)):
    print("Nome:" + str(pessoa.habilidades[x].nome))
    print("Nota:" + str(pessoa.habilidades[x].nota))


input()
