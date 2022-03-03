import pandas as pd  # extrai
import pandera as pa  # valida

# Dataframe
df = pd.read_csv("ocorrencia.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
df.head(10)  # mostra as 10 primeiras linhas

# Validação
schema = pa.DataFrameSchema(
    columns = {
        "codigo":pa.Column(pa.Int, required=False),
        "codigo_ocorrencia":pa.Column(pa.Int),
        "codigo_ocorrencia2":pa.Column(pa.Int),
        "ocorrencia_classificacao":pa.Column(pa.String),
        "ocorrencia_cidade":pa.Column(pa.String),
        "ocorrencia_uf":pa.Column(pa.String, pa.Check.str_length(2, 3)),
        "ocorrencia_aerodromo":pa.Column(pa.String),
        "ocorrencia_dia":pa.Column(pa.DateTime),
        "ocorrencia_hora":pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])?$'),nullable=True),
        "total_recomendacoes":pa.Column(pa.Int)
    }
)

schema.validate(df)  # valida se os valores são dos tipos especificados


# Limpeza de Dados

df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA  # especifica
df.replace(['', '**', '###!', '####', '****', '*****', 'NULL', '20'], pd.NA, inplace=True)

# dados não informados
df.isna().sum()  # conta
df.isnull().sum()  # conta
df.cout() # conta todos os items

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


df.fillna(0, inplace=True)  # muda os dados nulos
df.fillna(value={'total_recomendacoes':0}, inplace=True)

# Exclusão de Dados
df.drop(['ocorrencia_uf_bkp'], axis=1, inplace=True)  # exclui coluna
df.dropna(subset=['ocorrencia_uf'])  # exclui linhas vazias
df.drop_duplicates()  # exclui dados duplicados