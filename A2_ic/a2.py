import pandas as pd
from matplotlib import pyplot as plt

AUTORES = ['Gustavo Tironi', 'Gustavo Tironi']

def questao_1(datapath):
    df = pd.read_csv(datapath)
    print(len(df))
    return int(len(df))

def questao_2(datapath):
    df = pd.read_csv(datapath)
    df_municipio = df.groupby('ID_MUNICIP').count()['SG_UF_NOT']
    # print(df_municipio)
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
    estado_mais_numeroso_masc = max(dicionario_estado_masc, key=dicionario_estado_masc.get)
    print(estado_mais_numeroso_masc)
    print(dicionario_estado_masc)
    return dicionario_estado_masc

def questao_7(datapath):
    df = pd.read_csv(datapath)

    #determinado através da wikipedia
    municipios_por_estado_codigo = {12: 22, 27: 102, 16: 16, 13: 62, 29: 417, 23: 184, 32: 78, 52: 246, 21: 217, 51: 141, 50: 79, 31: 853, 15: 144, 25: 223, 41: 399, 26: 184, 22: 224, 24: 167, 43: 497, 33: 92, 11: 52, 14: 15, 42: 295, 35: 645, 28: 75, 17: 139, 53: 1}
    df_municipios_totais = pd.DataFrame.from_dict(municipios_por_estado_codigo, orient='index').sort_index().rename(columns = {0:'total'})

    '''
    municipios_por_estado = {'MG': 853, 'SP': 645, 'RS': 497, 'BA': 417, 'PR': 399, 'SC': 295, 'GO': 246, 'PI': 224, 'PB': 223, 'MA': 217, 'PE': 184, 'CE': 184, 'RN': 167, 'PA': 144, 'MT': 141, 'TO': 139, 'AL': 102, 'RJ': 92, 'MS': 79, 'ES': 78, 'SE': 75, 'AM': 62, 'RO': 52, 'AC': 22, 'AP': 16, 'RR': 15}
    dicionario_estados = {12: 'AC', 27: 'AL', 16: 'AP', 13: 'AM', 29: 'BA', 23: 'CE', 53: 'DF', 32: 'ES', 52: 'GO', 21: 'MA', 51: 'MT', 50: 'MS', 31: 'MG', 15: 'PA', 25: 'PB', 41: 'PR', 26: 'PE', 22: 'PI', 24: 'RN', 43: 'RS', 33: 'RJ', 11: 'RO', 14: 'RR', 42: 'SC', 35: 'SP', 28: 'SE', 17: 'TO'}
    dicionario = {}
    for chave_original, valores in dicionario_estados.items():
        for chave in municipios_por_estado.keys():
            if chave == valores:
                dicionario[chave_original] = municipios_por_estado[chave]
    '''

    df_municipio_por_estado = pd.Series(df.groupby('SG_UF_NOT')['ID_MUNICIP'].nunique()).rename('notificados')
    df_juntos = pd.merge(df_municipio_por_estado, df_municipios_totais, left_index=True, right_index=True)
    diconario_proporcoes = dict(df_juntos['notificados']*100/df_juntos['total'])
    print(diconario_proporcoes)
    return diconario_proporcoes

def questao_8(datapath):
    df = pd.read_csv(datapath)
    df['DT_NOTIFICACAO'] = pd.to_datetime(df['DT_NOTIFIC'], format = '%Y%m%d')
    df['DT_SINTOMAS'] = pd.to_datetime(df['DT_SIN_PRI'], format = '%Y%m%d')
    df['ATRASO_NOT'] = df['DT_NOTIFICACAO'] - df['DT_SINTOMAS']
    df_atraso = df[['DT_NOTIFICACAO', 'DT_SINTOMAS', 'ATRASO_NOT']]
    print(df_atraso)
    return df_atraso

def questao_9(datapath):
    df = pd.read_csv(datapath)
    df['DT_NOTIFICACAO'] = pd.to_datetime(df['DT_NOTIFIC'], format = '%Y%m%d')
    df['DT_SINTOMAS'] = pd.to_datetime(df['DT_SIN_PRI'], format = '%Y%m%d')
    df['ATRASO_NOT'] = df['DT_NOTIFICACAO'] - df['DT_SINTOMAS']
    df = df[['SG_UF_NOT', 'ATRASO_NOT']]
    df['ATRASO_NOT'] = df['ATRASO_NOT'].dt.days # Transforma em inteiro
    df_media = df.groupby('SG_UF_NOT').mean()
    df_desvio_padrao = df.groupby('SG_UF_NOT').std()
    '''
    df[df['ATRASO_NOT'] < 1500] corrige os outliers
    '''
    df_juntos = pd.merge(df_media, df_desvio_padrao, left_index=True, right_index=True).rename(columns={'ATRASO_NOT_x': 'media', 'ATRASO_NOT_y': 'desvio_padrao'})
    dicionario = df_juntos.to_dict()
    valor_media_dp = zip(dicionario['media'].values(), dicionario['desvio_padrao'].values())
    estado_media_dp = zip(dicionario['media'], valor_media_dp)
    dicionario_final = dict(estado_media_dp)
    print(dicionario_final)
    return dicionario_final

def questao_10(datapath):
    df = pd.read_csv(datapath)
    df['DT_NOTIFICACAO'] = pd.to_datetime(df['DT_NOTIFIC'], format = '%Y%m%d')
    df['DT_SINTOMAS'] = pd.to_datetime(df['DT_SIN_PRI'], format = '%Y%m%d')
    df['ATRASO_NOT'] = df['DT_NOTIFICACAO'] - df['DT_SINTOMAS']
    df['ATRASO_NOT'] = df['ATRASO_NOT'].dt.days
    # df = df[df['ATRASO_NOT'] < 1500] corrige os outliers
    df_municipio = questao_2(datapath)
    df_media_por_municipio = df.groupby('ID_MUNICIP')['ATRASO_NOT'].mean()
    df_juntos = pd.merge(df_municipio, df_media_por_municipio, left_index=True, right_index=True).rename(columns={'SG_UF_NOT': 'contagem', 'ATRASO_NOT': 'media'})
    df_juntos.plot.scatter('contagem', 'media')
    plt.show()
    print(df_media_por_municipio)
    return df_media_por_municipio

# questao_1('A2_ic/Leptospirose_2018.csv')
# questao_2('A2_ic/Leptospirose_2018.csv')
# questao_3('A2_ic/Leptospirose_2018.csv')
# questao_4('A2_ic/Leptospirose_2018.csv')
# questao_5('A2_ic/Leptospirose_2018.csv')
# questao_6('A2_ic/Leptospirose_2018.csv')
# questao_7('A2_ic/Leptospirose_2018.csv')
# questao_8('A2_ic/Leptospirose_2018.csv')
# questao_9('A2_ic/Leptospirose_2018.csv')
# questao_10('A2_ic/Leptospirose_2018.csv')