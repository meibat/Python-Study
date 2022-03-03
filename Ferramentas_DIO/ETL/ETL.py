import pandas as pd  # extrai
import pandera as pa  # valida


# Manipulação de Dados

# Dataframe
df = pd.read_csv("ocorrencia.csv", sep=";", parse_dates=['ocorrencia_dia'], dayfirst=True)
df.head(10)  # mostra as 10 primeiras linhas

df.dtypes  # mostra o tipo dos dados
df.ocorrencia_dia.dt.month  # extrai o mês da

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

df.codigo_ocorrencia.is_unique  # valida se os dados são unicos

# Localiza dados
df.loc[1, 'ocorrencia_cidade']  # dado especifico
df.loc[3]  # linha inteira
df.loc[1:3]  # várias linhas
df.loc[[10, 40]]  # duas ou mais linhas
df.loc[:, 'ocorrencia_cidade']  # coluna especifica
df.loc[df.ocorrencia_uf == 'SP', 'ocorrencia_classificacao']  # coluna especifica

df.set_index('codigo_ocorrencia', inplace=True)  # transforma em indice
df.reset_index(drop=True, inplace=True)  # reseta o index

# Alterando valores
df.loc[0, 'ocorrencia_aerodromo'] = ''  # dado especifico
df.loc[1] = 20  # linha inteira
df.loc[:, 'total_recomendacoes'] = 10  # colua especifica
df.loc[df.ocorrencia_uf == 'SP', ['ocorrencia_classificacao']] = 'GRAVE'

# Backup
df['ocorrencia_uf_bkp'] = df.ocorrencia_uf


# Limpeza de Dados

df.loc[df.ocorrencia_aerodromo == '****', ['ocorrencia_aerodromo']] = pd.NA  # especifica
df.replace(['', '**', '###!', '####', '****', '*****', 'NULL', '20'], pd.NA, inplace=True)

# dados não informados
df.isna().sum()  # conta
df.isnull().sum()  # conta

df.fillna(0, inplace=True)  # muda os dados nulos
df.fillna(value={'total_recomendacoes':0}, inplace=True)

# Exclusão de Dados
df.drop(['ocorrencia_uf_bkp'], axis=1, inplace=True)  # exclui coluna
df.dropna(subset=['ocorrencia_uf'])  # exclui linhas vazias
df.drop_duplicates()  # exclui dados duplicados


# Transformação de Dados




print(df)