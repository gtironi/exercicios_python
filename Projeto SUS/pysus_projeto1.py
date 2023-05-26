from pysus.online_data import SINAN
from pysus.preprocessing.decoders import decodifica_idade_SINAN
import pandas as pd

# path = SINAN.download('Leptospirose', 2018)
# dataframe = pd.read_parquet(path)
# dataframe['DT_NOTIFIC'] = pd.to_datetime(dataframe['DT_NOTIFIC'])
# dataframe.to_csv('Leptospirose.csv', index=False)

dataframe_lepto_2018 = pd.read_csv('Leptospirose.csv')
dataframe_lepto_2018['DT_NOTIFIC'] = pd.to_datetime(dataframe_lepto_2018['DT_NOTIFIC'])
dataframe_lepto_2018.set_index('DT_NOTIFIC', inplace = True)
dataframe_lepto_2018 = dataframe_lepto_2018[['ID_MUNICIP', 'SG_UF', 'NU_IDADE_N', 'CS_SEXO', 'CS_RACA']]
# print(dataframe_lepto_2018)


# Ano

# print(len(dataframe_lepto_2018.index))

# Municipio

agrupado_por_municipio = dataframe_lepto_2018.groupby('ID_MUNICIP').count().sort_values('SG_UF', ascending=False)
# print(agrupado_por_municipio['SG_UF'])

# Estado

agrupado_por_estado = dataframe_lepto_2018.groupby('SG_UF').count().sort_values('ID_MUNICIP', ascending=False)
# print(agrupado_por_estado['ID_MUNICIP'])

# Mês

agrupado_por_mês = dataframe_lepto_2018.resample('M').count()
# print(agrupado_por_mês['SG_UF'])

# Faixa etária

dataframe_lepto_2018['idade'] = decodifica_idade_SINAN(dataframe_lepto_2018.NU_IDADE_N)
dataframe_lepto_2018['idade'] = dataframe_lepto_2018['idade'].round(2)
agrupado_por_idade = dataframe_lepto_2018.groupby('idade').count().sort_values('SG_UF', ascending=False)
print(agrupado_por_idade['SG_UF'])

# Sexo
agrupado_por_sexo = dataframe_lepto_2018.groupby('CS_SEXO').count().sort_values('SG_UF', ascending=False)
# print(agrupado_por_sexo['SG_UF'])

# Raça e cor
agrupado_por_raca = dataframe_lepto_2018.groupby('CS_RACA').count().sort_values('SG_UF', ascending=False)
# print(agrupado_por_raca['SG_UF'])
