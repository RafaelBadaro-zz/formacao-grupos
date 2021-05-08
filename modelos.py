class Pessoa:
    def __init__(self, id, nome):
        self.nome = nome
        self.id = id
        self.pessoasHabilidades = []
        self.pessoasAtividades = []


class Atividade:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.pessoasAtividades = []
        self.atividadesHabilidades = []


class Habilidade:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.pessoasHabilidades = []
        self.atividadesHabilidades = []


class AtividadeHabilidade:
    def __init__(self, atividadeId, habilidadeId):
        self.atividadeId = atividadeId
        self.habilidadeId = habilidadeId

    def setAtividade(self, atividade):
        self.atividade = atividade

    def setHabilidade(self, habilidade):
        self.habilidade = habilidade


class PessoaAtividade:
    def __init__(self, pessoaId, atividadeId, preferencia):
        self.pessoaId = pessoaId
        self.atividadeId = atividadeId
        self.preferencia = preferencia

    def setPessoa(self, pessoa):
        self.pessoa = pessoa

    def setAtividade(self, atividade):
        self.atividade = atividade


class PessoaHabilidade:
    def __init__(self, pessoaId, habilidadeId, nota):
        self.pessoaId = pessoaId
        self.habilidadeId = habilidadeId
        self.nota = nota

    def setPessoa(self, pessoa):
        self.pessoa = pessoa

    def setHabilidade(self, habilidade: Habilidade):
        self.habilidade = habilidade


class Dados:
    def __init__(self, pessoas, habilidades, atividades):
        self.pessoas = pessoas
        self.habilidades = habilidades
        self.atividades = atividades


class Cromossomo:
    def __init__(self, pessoas, atividade):
        self.pessoas = pessoas
        self.atividade = atividade
        self.nota_ff = self.funcao_fitness()

    def funcao_fitness(self):
        soma_habilidades = 0
        soma_preferencias = 0
        for i in range(len(self.pessoas)):
            # Somatórios
            soma_habilidades
            soma_preferencias


class Selecao:
    def __init__(self, cromossomos):
        self.cromossomos = cromossomos

# Tarefas

# Parametros de entrada:

# O tamanho de cada cromossomo
# A quantidade de gerações
# Definir o tamanho da populacao maxima, ex: populacao inical = 20, cada geracao tem que ter 20 cromossomos, se deu 40, tem q matar os 20 piores

# 1 . Pop inical -> criar json com os dados e buscar eles - Ravi
# - While geracoes_requisitadas >= geracoes_atuais:
# 2 . aplicar a ff -> Laercio
# 3 . Selecionar quem vai fazer o cruzamento (os pais):  roleta viciada -> Badaró
# 4 . Gerar máscara e aplicar o cruzamento -> Badaró e Ravi
# 5 . Matar população - Ravi
# - EndWhile
