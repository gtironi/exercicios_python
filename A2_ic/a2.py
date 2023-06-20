import pandas as pd

AUTORES = ['Gustavo Tironi', 'Gustavo Tironi']

def questao_1(datadatapath):
    df = pd.read_csv(datadatapath)
    print(len(df))
    return len(df)

def questao_2(datadatapath):
    df = pd.read_csv(datadatapath)
    df_municipio = df.groupby('ID_MUNICIP').count()['SG_UF']
    print(df_municipio)
    return df_municipio

def questao_3(datadatapath):
    df = pd.read_csv(datadatapath)
    # criei um dataframe com a contagem por sexo, vale notar que aqui temos 'M', 'F' e 'I'.
    df_sexo = df.groupby("CS_SEXO").count()['SG_UF']
    # transformo o dataframe em um dicionário
    dicionario_sexo = dict(df_sexo)
    # removo a chave 'I' do dicionario, já que foi pedido apenas 'M' e 'F'
    del dicionario_sexo['I']
    sexo_mais_numeroso = max(dicionario_sexo, key=dicionario_sexo.get)
    print((sexo_mais_numeroso, dicionario_sexo))
    return (sexo_mais_numeroso, dicionario_sexo)


def questao_4(datapath):
    df = pd.read_csv(datadatapath)
    pass

def questao_5(datapath):
    df = pd.read_csv(datadatapath)
    pass

def questao_6(datapath):
    df = pd.read_csv(datadatapath)
    pass

def questao_7(datapath):
    df = pd.read_csv(datadatapath)
    pass

def questao_8(datapath):
    df = pd.read_csv(datadatapath)
    pass

def questao_9(datapath):
    df = pd.read_csv(datadatapath)
    pass

def questao_10(datapath):
    df = pd.read_csv(datadatapath)
    pass

# questao_1('A2_ic/Leptospirose.csv')
# questao_2('A2_ic/Leptospirose.csv')
questao_3('A2_ic/Leptospirose.csv')