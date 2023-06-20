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
    df = le_csv(datapath)
    pass


def questao_4(datapath):
    df = le_csv(datapath)
    pass

def questao_5(datapath):
    df = le_csv(datapath)
    pass

def questao_6(datapath):
    df = le_csv(datapath)
    pass

def questao_7(datapath):
    df = le_csv(datapath)
    pass

def questao_8(datapath):
    df = le_csv(datapath)
    pass

def questao_9(datapath):
    df = le_csv(datapath)
    pass

def questao_10(datapath):
    df = le_csv(datapath)
    pass

# questao_1('A2_ic/Leptospirose.csv')
questao_2('A2_ic/Leptospirose.csv')