import pandas as pd  # extrai
import pandera as pa  # valida

valores_ausentes = ['', '**', '###!', '####', '****', '*****', 'NULL']

# Dataframe
df = pd.read_csv("ocorrencia.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)

# Validação
schema = pa.DataFrameSchema(
    columns = {
        "codigo":pa.Column(pa.Int, required=False),
        "codigo_ocorrencia":pa.Column(pa.Int),
        "codigo_ocorrencia2":pa.Column(pa.Int),
        "ocorrencia_classificacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String, pa.Check.str_length(2, 3), nullable=True),
        "ocorrencia_aerodromo":pa.Column(pa.String, nullable=True),
        "ocorrencia_dia":pa.Column(pa.DateTime),
        "ocorrencia_hora":pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])?$'), nullable=True),
        "total_recomendacoes":pa.Column(pa.Int)
    }
)

schema.validate(df)  # valida se os valores são dos tipos

# Transformando

# criando nova coluna juntando data e hora
df['ocorrencia_dia_hora'] = pd.to_datetime(df.ocorrencia_dia.astype(str) + ' ' + df.ocorrencia_hora)

# filtros
df.loc[df.ocorrencia_aerodromo.isnull()]  # mostra os labels nulos
df.loc[df.total_recomendacoes > 10]  # baseado na quantidade
df.loc[df.total_recomendacoes > 10, 'ocorrencia_cidade']  # baseado na qtde e cidade
df.loc[df.total_recomendacoes > 10, ['ocorrencia_cidade', 'total_recomendacoes']]  # baseado na qtde e colunas
df.loc[df.total_recomendacoes > 10 & df.ocorrencia_uf == 'SP']  # baseado na qtde e


filtro1 = df.ocorrencia_classificacao.isin(['INCIDENTE GRAVE', 'INCIDENTE'])
filtro2 = df.ocorrencia_uf == 'SP'
df.loc[filtro1 & filtro2]  # funciona apenas com variaveis declaradas
df.loc[filtro1 | filtro2]  # funciona apenas com variaveis declaradas

filtro = df.ocorrencia_cidade.str[0] == 'C'  # começa
filtro = df.ocorrencia_cidade.str[-1] == 'A'  # termina
filtro = df.ocorrencia_cidade.str[-2:] == 'MA'  # termina
filtro = df.ocorrencia_cidade.str.contains('MA')  # contém
filtro = df.ocorrencia_cidade.str.contains('MA|AL')  # contém
filtro = (df.ocorrencia_dia.dt.year == 2015) & (df.ocorrencia_dia.dt.month == 12) & (df.ocorrencia_dia.dt.day == 8)

# Criando um novo dataframe
filtro1 = df.ocorrencia_dia.dt.year == 2015
filtro2 = df.ocorrencia_dia.dt.month == 3
df201503 = df.loc[filtro1 & filtro2]

filtro1 = df.ocorrencia_dia.dt.year == 2010
filtro2 = df.ocorrencia_uf.isin(['SP', 'MG', 'ES', 'RJ'])
dfsudeste2010 = df.loc[filtro1 & filtro2]

filtro = dfsudeste2010.total_recomendacoes > 0

# agrupando
df201503.groupby(['ocorrencia_classificacao']).size()
dfsudeste2010.groupby(['ocorrencia_classificacao', 'ocorrencia_uf']).size()
dfsudeste2010.loc[filtro].groupby(['ocorrencia_cidade']).total_recomendacoes.sum().sort_values(ascending=False)
print(dfsudeste2010.loc[filtro].groupby(['ocorrencia_cidade', dfsudeste2010.ocorrencia_dia.dt.month]).total_recomendacoes.sum())
