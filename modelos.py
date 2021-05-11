
RELEVANCIA_HABILIDADE = 10
RELEVANCIA_PREFERENCIA = 1


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
        self.habilidades = []


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
        self.preferencia = 1

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

        habilidadesAtividade = self.atividade.atividadesHabilidades

        for pessoa in self.pessoas:
            for habilidadePessoa in pessoa.pessoasHabilidades:
                for habilidadeAtividade in habilidadesAtividade:
                    if habilidadePessoa.habilidadeId == habilidadeAtividade.habilidadeId:
                        soma_habilidades += ((habilidadePessoa.nota * RELEVANCIA_HABILIDADE) + (
                            habilidadePessoa.preferencia * RELEVANCIA_PREFERENCIA))
        return soma_habilidades

    def __str__(self):
        return str(self.nota_ff)

    def comparaCromossomos(self, c2):
        if len(self.pessoas) != len(c2.pessoas):
            return False

        for i in self.pessoas:
            if i not in c2.pessoas:
                return False

        return True


class Selecao:
    def __init__(self, cromossomos):
        self.cromossomos = cromossomos
