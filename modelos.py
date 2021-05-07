class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Atividade:
    def __init__(self, nome, habilidades_necessarias):
        self.nome = nome
        self.habilidades_necessarias = habilidades_necessarias


class Habilidade:
    def __init__(self, nome):
        self.nome = nome


class PessoaAtividade:
    def __init__(self, nome_pessoa, nome_atividade, preferencia):
        self.nome_pessoa = nome_pessoa
        self.nome_atividade = nome_atividade
        self.preferencia = preferencia


class PessoaHabilidade:
    def __init__(self, nome_pessoa, nome_habilidade, nota):
        self.nome_pessoa = nome_pessoa
        self.nome_habilidade = nome_habilidade
        self.nota = nota


class Cromossomo:
    def __init__(self, pessoas, atividade):
        self.pessoas = pessoas
        self.atividade = atividade

    def funcao_fitness(self):
        soma_habilidades = 0
        soma_preferencias = 0
        for i in range(len(self.pessoas)):
            # Somatórios
            soma_habilidades++
            soma_preferencias++


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
