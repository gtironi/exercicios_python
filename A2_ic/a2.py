import pandas as pd
from matplotlib import pyplot as plt

AUTORES = ['Gustavo Tironi', 'Gustavo Tironi']

def questao_1(datapath):
    df = pd.read_csv(datapath)

    return int(len(df))

def questao_2(datapath):
    df = pd.read_csv(datapath)
    df_municipio = df.groupby('ID_MUNICIP').count()['SG_UF_NOT']

    return df_municipio

def questao_3(datapath):
    df = pd.read_csv(datapath)

    df_sexo = df.groupby("CS_SEXO").count()['SG_UF_NOT']
    dicionario_sexo = dict(df_sexo)

    del dicionario_sexo['I']

    sexo_mais_numeroso = max(dicionario_sexo, key=dicionario_sexo.get)

    return (sexo_mais_numeroso, dicionario_sexo)


def questao_4(datapath):
    df = pd.read_csv(datapath)
    media = float(df['idade'].mean())

    return media

def questao_5(datapath):
    df = pd.read_csv(datapath)

    df_estado = df.groupby('SG_UF_NOT').count()['CS_SEXO']
    dicionario_estado = dict(df_estado)

    estado_mais_numeroso = max(dicionario_estado, key=dicionario_estado.get)

    return dicionario_estado

def questao_6(datapath):
    df = pd.read_csv(datapath)

    df_filtrado = df[df['CS_SEXO'] == 'M']
    df_estado_masc = df_filtrado.groupby('SG_UF_NOT').count()['CS_SEXO']
    dicionario_estado_masc = dict(df_estado_masc)

    estado_mais_numeroso_masc = max(dicionario_estado_masc, key=dicionario_estado_masc.get)

    return dicionario_estado_masc

def questao_7(datapath):
    df = pd.read_csv(datapath)

    municipios_por_estado_codigo = {12: 22, 27: 102, 16: 16, 13: 62, 29: 417, 23: 184, 32: 78, 52: 246, 21: 217, 51: 141, 50: 79, 31: 853, 15: 144, 25: 223, 41: 399, 26: 184, 22: 224, 24: 167, 43: 497, 33: 92, 11: 52, 14: 15, 42: 295, 35: 645, 28: 75, 17: 139, 53: 1}
    
    df_municipios_totais = pd.DataFrame.from_dict(municipios_por_estado_codigo, orient='index').sort_index()
    df_municipio_por_estado = pd.Series(df.groupby('SG_UF_NOT')['ID_MUNICIP'].nunique().sort_index())

    df_juntos = pd.merge(df_municipio_por_estado, df_municipios_totais, left_index=True, right_index=True).rename(columns = {0:'total', 'ID_MUNICIP': 'notificados'})

    diconario_proporcoes = dict(df_juntos['notificados']*100/df_juntos['total'])

    return diconario_proporcoes

def questao_8(datapath):
    df = pd.read_csv(datapath)
    df['DT_NOTIFICACAO'] = pd.to_datetime(df['DT_NOTIFIC'], format = '%Y%m%d')
    df['DT_SINTOMAS'] = pd.to_datetime(df['DT_SIN_PRI'], format = '%Y%m%d')
    df['ATRASO_NOT'] = df['DT_NOTIFICACAO'] - df['DT_SINTOMAS']

    df_atraso = df[['DT_NOTIFICACAO', 'DT_SINTOMAS', 'ATRASO_NOT']]

    return df_atraso

def questao_9(datapath):
    df = pd.read_csv(datapath)
    df['DT_NOTIFICACAO'] = pd.to_datetime(df['DT_NOTIFIC'], format = '%Y%m%d')
    df['DT_SINTOMAS'] = pd.to_datetime(df['DT_SIN_PRI'], format = '%Y%m%d')
    df['ATRASO_NOT'] = df['DT_NOTIFICACAO'] - df['DT_SINTOMAS']
    df = df[['SG_UF_NOT', 'ATRASO_NOT']]
    df['ATRASO_NOT'] = df['ATRASO_NOT'].dt.days

    df_media = df.groupby('SG_UF_NOT').mean()
    df_desvio_padrao = df.groupby('SG_UF_NOT').std()

    df_juntos = pd.merge(df_media, df_desvio_padrao, left_index=True, right_index=True).rename(columns={'ATRASO_NOT_x': 'media', 'ATRASO_NOT_y': 'desvio_padrao'})
    dicionario = df_juntos.to_dict()

    valor_media_dp = zip(dicionario['media'].values(), dicionario['desvio_padrao'].values())
    estado_media_dp = zip(dicionario['media'].keys(), valor_media_dp)

    dicionario_final = dict(estado_media_dp)
    return dicionario_final

def questao_10(datapath):
    df = pd.read_csv(datapath)

    df['DT_NOTIFICACAO'] = pd.to_datetime(df['DT_NOTIFIC'], format = '%Y%m%d')
    df['DT_SINTOMAS'] = pd.to_datetime(df['DT_SIN_PRI'], format = '%Y%m%d')
    df['ATRASO_NOT'] = df['DT_NOTIFICACAO'] - df['DT_SINTOMAS']
    df['ATRASO_NOT'] = df['ATRASO_NOT'].dt.days

    df_municipio = questao_2(datapath)
    df_media_por_municipio = df.groupby('ID_MUNICIP')['ATRASO_NOT'].mean()

    df_juntos = pd.merge(df_municipio, df_media_por_municipio, left_index=True, right_index=True).rename(columns={'SG_UF_NOT': 'contagem', 'ATRASO_NOT': 'media'})

    df_juntos.plot.scatter('contagem', 'media')
    plt.show()

    return df_media_por_municipio