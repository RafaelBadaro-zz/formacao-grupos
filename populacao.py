import json
from modelos import *

def thanos():
    return 0

def pegarDados():
    with open('dados.json') as json_file:
        data = json.load(json_file)

    # mapeando dados json em objetos
    pessoas = list(map(lambda p: Pessoa(p['id'], p['nome']), data['pessoas']))
    habilidades = list(map(lambda h: Habilidade(h['id'], h['nome']), data['habilidades']))
    atividades = list(map(lambda a: Atividade(a['id'], a['nome']), data['atividades']))
    pessoasHabilidades = list(map(lambda ph: PessoaHabilidade(ph['pessoaId'], ph['habilidadeId'], ph['nota']), data['pessoasHabilidades']))
    pessoasAtividades = list(map(lambda pa: PessoaAtividade(pa['pessoaId'], pa['atividadeId'], pa['preferencia']), data['pessoasAtividades']))
    atividadesHabilidades = list(map(lambda ah: AtividadeHabilidade(ah['atividadeId'], ah['habilidadeId']), data['atividadesHabilidades']))

    # adicionando as referencias
    for pessoaHabilidade in pessoasHabilidades:
        for pessoa in pessoas:
            if pessoaHabilidade.pessoaId == pessoa.id:
                pessoaHabilidade.setPessoa(pessoa=pessoa)
                pessoa.pessoasHabilidades.append(pessoaHabilidade)
        
        for habilidade in habilidades:
            if pessoaHabilidade.habilidadeId == habilidade.id:
                pessoaHabilidade.setHabilidade(habilidade=habilidade)
                habilidade.pessoasHabilidades.append(pessoaHabilidade)

    for pessoaAtividade in pessoasAtividades:
        for pessoa in pessoas:
            if pessoaAtividade.pessoaId == pessoa.id:
                pessoaAtividade.setPessoa(pessoa)
                pessoa.pessoasAtividades.append(pessoaAtividade)

        for atividade in atividades:
            if pessoaAtividade.atividadeId == atividade.id:
                pessoaAtividade.setAtividade(atividade)
                atividade.pessoasAtividades.append(pessoaAtividade)

    for atividadeHabilidade in atividadesHabilidades:
        for atividade in atividades:
            if atividadeHabilidade.atividadeId == atividade.id:
                atividadeHabilidade.setAtividade(atividade)
                atividade.atividadesHabilidades.append(atividadeHabilidade)

        for habilidade in habilidades:
            if atividadeHabilidade.habilidadeId == habilidade.id:
                atividadeHabilidade.setHabilidade(habilidade)
                habilidade.atividadesHabilidades.append(habilidade)

    return Dados(pessoas, habilidades, atividades)

def iniciarPopulacao(dados: Dados):
    return list()