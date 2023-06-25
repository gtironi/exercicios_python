import pandas as pd

AUTORES = ['Gustavo Tironi', 'Gustavo Tironi']

def questao_1(datapath):
    df = pd.read_csv(datapath)
    print(len(df))
    return int(len(df))

def questao_2(datapath):
    df = pd.read_csv(datapath)
    df_municipio = df.groupby('ID_MUNICIP').count()['SG_UF_NOT']
    print(df_municipio)
    return df_municipio

def questao_3(datapath):
    df = pd.read_csv(datapath)
    # criei um dataframe com a contagem por sexo, vale notar que aqui temos 'M', 'F' e 'I'.
    df_sexo = df.groupby("CS_SEXO").count()['SG_UF_NOT']
    # transformo o dataframe em um dicionário
    dicionario_sexo = dict(df_sexo)
    # removo a chave 'I' do dicionario, já que foi pedido apenas 'M' e 'F'
    del dicionario_sexo['I']
    sexo_mais_numeroso = max(dicionario_sexo, key=dicionario_sexo.get)
    print((sexo_mais_numeroso, dicionario_sexo))
    return (sexo_mais_numeroso, dicionario_sexo)


def questao_4(datapath):
    df = pd.read_csv(datapath)
    print(df['idade'].mean())
    return df['idade'].mean()

def questao_5(datapath):
    df = pd.read_csv(datapath)
    df_estado = df.groupby('SG_UF_NOT').count()['CS_SEXO']
    dicionario_estado = dict(df_estado)
    estado_mais_numeroso = max(dicionario_estado, key=dicionario_estado.get)
    print(estado_mais_numeroso)
    print(dicionario_estado)
    return dicionario_estado

def questao_6(datapath):
    df = pd.read_csv(datapath)
    df_filtrado = df[df['CS_SEXO'] == 'M']
    df_estado_masc = df_filtrado.groupby('SG_UF_NOT').count()['CS_SEXO']
    dicionario_estado_masc = dict(df_estado_masc)
    print(dicionario_estado_masc)
    return dicionario_estado_masc

def questao_7(datapath):
    df = pd.read_csv(datapath)
    pass

def questao_8(datapath):
    df = pd.read_csv(datapath)
    pass

def questao_9(datapath):
    df = pd.read_csv(datapath)
    pass

def questao_10(datapath):
    df = pd.read_csv(datapath)
    pass

# questao_1('A2_ic/Leptospirose_2018.csv')
# questao_2('A2_ic/Leptospirose_2018.csv')
# questao_3('A2_ic/Leptospirose_2018.csv')
# questao_4('A2_ic/Leptospirose_2018.csv')
# questao_5('A2_ic/Leptospirose_2018.csv')
# questao_6('A2_ic/Leptospirose_2018.csv')
questao_7('A2_ic/Leptospirose_2018.csv')