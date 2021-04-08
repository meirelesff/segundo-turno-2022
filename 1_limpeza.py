from datetime import datetime
import pandas as pd
import numpy as np

# Carrega os dados e filtra: nacional e segundo turno
bd = pd.read_csv("raw_data/pesquisas.csv", sep = ";")
bd = bd.loc[(bd["unidades_federativas_id"] == 6) & (bd["turno"] == 2)]

# Casting
vars = ["pesquisa_id", "cenario_id", "candidatos_id"]
bd[vars] = bd[vars].astype(str)
bd.data_pesquisa = bd.data_pesquisa.astype('datetime64[ns]')

# Calcula o erro das pesquisas
bd["percentual"] = bd.percentual / 100
bd["erro"] = (bd.percentual * (1 - bd.percentual)) / bd.qtd_entrevistas
bd["erro"] = np.sqrt(bd.erro)

# Filtra apenas eleicoes com figuras selecionadas
bd = bd[bd.candidato.isin(["Bolsonaro", "Lula"])]
bd = bd[bd.groupby(["cenario_id"]).transform("count").pesquisa_id == 2]

# Cria a variavel que indica dias ateh a eleicao
bd["dias_eleicao"] = (datetime.today() - bd.data_pesquisa).astype('timedelta64[D]').astype(int)

# Cria o dicionario para o stan
dados = {
    "T" : max(bd.dias_eleicao),
    "C" : len(bd.candidato.unique()),
    "N" : bd.shape[0],
    "delta" : bd.percentual.values,
    "index_c" : bd.candidatos_id.values,
    "index_t" : bd.dias_eleicao.values,
    "omega" : bd.erro.values
}
